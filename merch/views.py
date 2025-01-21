from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product, Basket, BasketItem, Order, OrderItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def product_list(request, category_slug=None):
    """Отображение списка товаров с фильтрацией по категории"""
    category = None
    products = Product.objects.filter(available=True, stock__gt=0)

    # Поиск товаров
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # Фильтрация по категории
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Пагинация
    paginator = Paginator(products, 12)  # По 12 товаров на страницу
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, возвращаем первую страницу
        products = paginator.page(1)
    except EmptyPage:
        # Если страница за пределами допустимого диапазона, возвращаем последнюю страницу
        products = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'products': products,
        'search_query': search_query
    }
    return render(request, 'merch/product/list.html', context)


def product_detail(request, slug):
    """Детальная страница товара"""
    product = get_object_or_404(Product, slug=slug, available=True, stock__gt=0)
    related_products = Product.objects.filter(category=product.category, available=True, stock__gt=0).exclude(id=product.id)[:4]
    context = {
        'product': product,
        'related_products': related_products
    }
    return render(request, 'merch/product/detail.html', context)


@login_required
def cart_detail(request):
    """Просмотр корзины"""
    basket = request.user.basket
    context = {'basket': basket}
    return render(request, 'merch/cart/detail.html', context)


@login_required
def cart_add(request, product_id):
    """Добавление товара в корзину"""
    product = get_object_or_404(Product, id=product_id)
    if not product.is_available():
        messages.error(request, 'Товар недоступен')
        return redirect('merch:product_detail', slug=product.slug)

    basket = request.user.basket
    quantity = int(request.POST.get('quantity', 1))

    # Проверка наличия на складе
    if product.stock < quantity:
        messages.error(request, 'Недостаточно товара на складе')
        return redirect('merch:cart_detail')

    # Добавление или обновление товара в корзине
    basket_item, created = BasketItem.objects.get_or_create(
        basket=basket,
        product=product,
        defaults={'quantity': quantity, 'price_item': product.current_price}
    )
    if not created:
        basket_item.quantity += quantity
        basket_item.save()

    messages.success(request, 'Товар добавлен в корзину')
    return redirect('merch:product_detail', slug=product.slug)


@login_required
def cart_remove(request, product_id):
    """Удаление товара из корзины"""
    basket = request.user.basket
    BasketItem.objects.filter(
        basket=basket,
        product_id=product_id
    ).delete()
    messages.success(request, 'Товар удален из корзины')
    return redirect('merch:cart_detail')


@login_required
def order_list(request):
    """Список заказов пользователя"""
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'merch/order/list.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    """Детали заказа"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'merch/order/detail.html', {'order': order})


@login_required
def order_create(request):
    """Создание заказа"""
    basket = request.user.basket

    # Проверка корзины
    if not basket.basketitem_set.exists():
        messages.error(request, 'Ваша корзина пуста')
        return redirect('merch:cart_detail')

    # Проверка наличия товаров
    for item in basket.basketitem_set.all():
        if item.quantity > item.product.stock:
            messages.error(
                request,
                f'Товар "{item.product.name}" недоступен в запрошенном количестве'
            )
            return redirect('merch:cart_detail')

    # Проверка наличия средств
    if request.user.wallet < basket.total_price:
        messages.error(request, 'Недостаточно средств для оплаты заказа')
        return redirect('merch:cart_detail')

    # Создание заказа
    order = Order.objects.create(
        user=request.user,
        total_price=basket.total_price
    )

    # Перенос товаров в заказ
    for item in basket.basketitem_set.all():
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price_item=item.price_item
        )
        # Уменьшаем количество товара на складе
        item.product.stock -= item.quantity
        item.product.save()

    # Очистка корзины и списание средств
    basket.basketitem_set.all().delete()
    request.user.wallet -= order.total_price
    request.user.save()

    messages.success(request, f'Заказ №{order.id} успешно создан')
    return redirect('merch:order_detail', order_id=order.id)
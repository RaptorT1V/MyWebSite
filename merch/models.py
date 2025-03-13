from django.db import models
from users.models import CustomUser
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название категории")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Описание категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")

    description = models.TextField(blank=True, verbose_name="Описание товара")
    size = models.CharField(max_length=50, blank=True, verbose_name="Размер")
    color = models.CharField(max_length=50, blank=True, verbose_name="Цвет")
    weight = models.CharField(max_length=50, blank=True, verbose_name="Вес")

    # Цены и наличие
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Цена"
    )
    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=None,
        null=True,
        verbose_name="Цена со скидкой"
    )
    stock = models.PositiveIntegerField(default=0, verbose_name="Количество на складе")
    available = models.BooleanField(default=True, verbose_name="Доступен для покупки")

    # Медиафайлы
    main_image = models.ImageField(
        upload_to='merch/products/%Y/%m/%d',
        verbose_name="Главное изображение"
    )

    # Метаданные
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    featured = models.BooleanField(default=False, verbose_name="Рекомендуемый товар")

    class Meta:
        ordering = ['-created']
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    @property
    def current_price(self):
        """Возвращает актуальную цену (со скидкой, если она есть)"""
        return self.discount_price if self.discount_price else self.price

    def is_available(self):
        """Проверяет доступность товара"""
        return self.available and self.stock > 0

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    @property
    def total_price(self):
        """Подсчитывает общую стоимость корзины"""
        return sum(item.subtotal for item in self.items.all())

    @property
    def total_items(self):
        """Подсчитывает общее количество товаров в корзине"""
        return sum(item.quantity for item in self.items.all())

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, verbose_name="Корзина")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.IntegerField(default=1, verbose_name="Количество")
    price_item = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за единицу")

    @property
    def subtotal(self):
        """Подсчитывает стоимость позиции"""
        return self.quantity * self.price_item

    def __str__(self):
        return f"{self.quantity} x {self.product.name} в корзине {self.basket.user.username}"

    class Meta:
        verbose_name = "Элемент корзины"
        verbose_name_plural = "Элементы корзины"


class Order(models.Model):
    STATUS_CHOICES = (
        ('created', 'Создан'),
        ('processing', 'В обработке'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('canceled', 'Отменен'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created', verbose_name="Статус")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость")

    def __str__(self):
        return f"Заказ №{self.id} от {self.order_date.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.IntegerField(verbose_name="Количество")
    price_item = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за единицу")

    def __str__(self):
        return f"{self.quantity} x {self.product.name} в заказе №{self.order.id}"

    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural = "Элементы заказа"


@receiver(pre_save, sender=Category)
def generate_category_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


@receiver(pre_save, sender=Product)
def generate_product_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
from django.urls import path
from . import views

app_name = 'merch'

urlpatterns = [
    # Список товаров
    path('', views.product_list, name='index'),
    path('category/<slug:category_slug>/', views.product_list, name='category_detail'),

    # Детальная страница товара
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

    # Корзина
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

    # Заказы
    path('orders/', views.order_list, name='order_list'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/create/', views.order_create, name='order_create'),
]
from django.contrib import admin
from .models import Product, Basket, BasketItem, Order, OrderItem, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'discount_price', 'stock', 'available', 'featured')
    list_filter = ('category', 'available', 'featured', 'created')
    list_editable = ('price', 'discount_price', 'stock', 'available', 'featured')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created'

    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'slug', 'category')
        }),
        ('Описание и характеристики', {
            'fields': ('description', 'size', 'color', 'weight')
        }),
        ('Цены и наличие', {
            'fields': ('price', 'discount_price', 'stock', 'available')
        }),
        ('Медиафайлы', {
            'fields': ('main_image',)
        }),
        ('Дополнительно', {
            'fields': ('featured',)
        }),
    )

    actions = ['make_available', 'make_unavailable']

    def make_available(self, request, queryset):
        queryset.update(available=True)
    make_available.short_description = "Сделать выбранные товары доступными"

    def make_unavailable(self, request, queryset):
        queryset.update(available=False)
    make_unavailable.short_description = "Сделать выбранные товары недоступными"


class BasketItemInline(admin.TabularInline):
    model = BasketItem
    extra = 1
    raw_id_fields = ['product']


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)
    raw_id_fields = ('user',)
    inlines = [BasketItemInline]


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('basket', 'product', 'quantity', 'price_item')
    list_filter = ('basket__user',)
    search_fields = ('product__name', 'basket__user__username')
    raw_id_fields = ('product', 'basket')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'status', 'total_price')
    list_filter = ('status', 'order_date')
    search_fields = ('user__username', 'id')
    date_hierarchy = 'order_date'
    readonly_fields = ('order_date',)
    raw_id_fields = ('user',)
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price_item')
    list_filter = ('order__status',)
    search_fields = ('product__name', 'order__user__username')
    raw_id_fields = ('product', 'order')
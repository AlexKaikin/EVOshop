from django.contrib import admin

from .models import Product, ProductImage, Order, Category, Review, OrderItem


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_editable = ['status']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'status']
    list_editable = ['price', 'stock', 'status']
    list_filter = ['category', 'status']
    inlines = [ProductImageInline]
    search_fields = ['name']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'status', 'created']

    def has_module_permission(self, request):  # скрыть модель из админки
        return False


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['description', 'profile', 'status']
    list_editable = ['status']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'id', 'status', 'paid', 'created', 'updated']
    list_editable = ['status', 'paid']
    list_filter = ['status', 'paid']
    inlines = [OrderItemInline]


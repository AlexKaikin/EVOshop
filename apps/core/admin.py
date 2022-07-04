from django.contrib import admin

from .models import Product, ProductImage, Order, Profile, Category, Review, OrderItem


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_editable = ['is_active']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'is_active']
    list_editable = ['price', 'stock', 'is_active']
    list_filter = ['category']
    inlines = [ProductImageInline]
    search_fields = ['name']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'is_active', 'created']

    def has_module_permission(self, request):  # скрыть модель из админки
        return False


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['description', 'author', 'status']
    list_editable = ['status']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'status', 'paid', 'created', 'updated']
    list_editable = ['status', 'paid']
    list_filter = ['status', 'paid']
    inlines = [OrderItemInline]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_logged']


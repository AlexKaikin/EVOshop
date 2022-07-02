from django.contrib import admin

from .models import Product, ProductImage, StatusOrder, Order, Profile, Category, Review


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


@admin.register(StatusOrder)
class StatusOrderAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = StatusOrder

    def has_module_permission(self, request):  # скрыть модель из админки
        return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'status', 'created', 'updated']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_logged']


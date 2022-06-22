from django.contrib import admin

from .models import Product, ProductImage, StatusOrder, Order, Profile, Category


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    inlines = [ProductImageInline]
    search_fields = ['name']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'is_active', 'created']

    def has_module_permission(self, request):  # скрыть модель из админки
        return False


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

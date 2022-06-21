from django.contrib import admin

from .models import Product, ProductImage, StatusOrder, Order


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


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


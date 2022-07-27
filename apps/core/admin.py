from django.contrib import admin

from .models import Product, ProductImage, Order, Category, Review, OrderItem, Setting


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'published']
    list_editable = ['published']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created', 'updated']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'stock', 'published']
    list_editable = ['price', 'stock', 'published']
    list_filter = ['category', 'published']
    inlines = [ProductImageInline]
    search_fields = ['name']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created', 'updated']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'published', 'created']

    def has_module_permission(self, request):  # скрыть модель из админки
        return False


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'profile', 'published']
    list_editable = ['published']
    list_display_links = ['description']
    readonly_fields = ['created']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'surname', 'name', 'status', 'paid', 'created', 'updated']
    list_editable = ['status', 'paid']
    list_filter = ['status', 'paid']
    inlines = [OrderItemInline]
    list_display_links = ['surname']
    readonly_fields = ['created', 'updated']


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'delivery', 'delivery_free']
    list_editable = ['delivery', 'delivery_free']
    list_display_links = ['name']


admin.site.site_title = 'EVO'
admin.site.site_header = 'EVO администрирование'

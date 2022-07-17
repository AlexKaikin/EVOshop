from apps.core.models import Product


def get_product_list(self):
    product_list = Product.objects.all().select_related('category')
    return product_list

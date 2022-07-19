from apps.core.models import Product


def get_product_list(self):
    """
    Вернет список товаров по фильтру:
    - slug категории
    - активные товары
    """
    slug = self.kwargs['slug']
    product_list = Product.objects.filter(category__slug=slug).filter(status='yes')
    return product_list

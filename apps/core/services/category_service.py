from apps.core.models import Product


def get_product_list(self):
    """
    Вернет список товаров по фильтру:
    - slug категории
    - активные товары
    - остаток на складе больше 0
    """
    slug = self.kwargs['slug']
    product_list = Product.objects.filter(category__slug=slug).filter(published='yes', stock__gt=0)
    return product_list

from apps.core.models import Product


def get_favourite_list(self):
    """
    Вернет список товаров по фильтру:
    - slug категории
    - активные товары
    - остаток на складе больше 0
    """
    product_list = Product.objects.filter(favourite=self.request.user, published='yes', stock__gt=0)
    return product_list

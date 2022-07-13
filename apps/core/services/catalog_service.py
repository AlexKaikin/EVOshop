from apps.core.models import Category


def get_product_list(self):
    """
    Вернет список товаров по фильтру:
    - slug категории
    - активные товары
    """
    slug = self.kwargs['slug']
    category = Category.objects.get(slug=slug)
    product_list = category.products.filter(is_active=True)

    return product_list

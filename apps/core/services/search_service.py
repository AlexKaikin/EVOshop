from apps.core.models import Product


def get_search_list(self):
    """
    Вернет список товаров по фильтру:
    - совпадение слова в заголовке товара
    - активные товары
    """
    product_list = Product.objects.filter(name__icontains=self.request.GET.get('q'), status='yes')
    return product_list

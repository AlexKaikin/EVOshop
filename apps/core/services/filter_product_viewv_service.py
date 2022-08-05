from django.db.models import Q

from apps.core.models import Product


def get_filter_queryset(self):
    """
    Вернет список товаров по фильтру совпадения:
    - категории
    - метки
    """

    product_list = Product.objects.filter(
            Q(category__name__in=self.request.GET.getlist("category")) |
            Q(tag__name__in=self.request.GET.getlist("tag")), published='yes'
        ).distinct()
    return product_list




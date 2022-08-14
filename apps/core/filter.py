import django_filters

from apps.core.models import Product


class ProductFilter(django_filters.FilterSet):
    """ Фильтры для товаров """

    name = django_filters.CharFilter(field_name='name', lookup_expr='in')

    class Meta:
        model = Product
        fields = ['name']

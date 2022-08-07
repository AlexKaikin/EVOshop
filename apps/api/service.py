from django_filters import rest_framework as filters

from apps.core.models import Product


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    """  """
    pass


class ProductFilter(filters.FilterSet):
    """ Фильтры для товаров """
    category = CharFilterInFilter(field_name='category__name', lookup_expr='in')
    country = CharFilterInFilter(field_name='country', lookup_expr='in')
    price = filters.RangeFilter()
    tag = CharFilterInFilter(field_name='tag__name', lookup_expr='in')
    year = filters.RangeFilter()

    class Meta:
        model = Product
        fields = ('category', 'country', 'price', 'tag', 'year',)

from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

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


class Paginator(PageNumberPagination):
    """ Пагинация """
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })

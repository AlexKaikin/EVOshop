from django_filters import rest_framework as filters

from apps.core.models import Product, Category, Review


def get_product_list():
    return Product.objects.filter(published='yes', stock__gt=0)


def get_category_for_product(pk):
    return Category.objects.get(pk=pk)


def get_reviews_for_product(pk):
    return Review.objects.filter(product=pk)


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    """  """
    pass


class ProductFilter(filters.FilterSet):
    """ Фильтры для товаров """
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    category = CharFilterInFilter(field_name='category__name', lookup_expr='in')
    country = CharFilterInFilter(field_name='country', lookup_expr='in')
    price = filters.RangeFilter()
    tag = CharFilterInFilter(field_name='tag__name', lookup_expr='in')
    year = filters.RangeFilter()

    class Meta:
        model = Product
        fields = ('name', 'category', 'country', 'price', 'tag', 'year',)


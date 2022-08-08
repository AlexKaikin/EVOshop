from django_filters import rest_framework as filters

from apps.core.models import Category


def get_category_list():
    return Category.objects.filter(published='yes')


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    """  """
    pass


class CategoryFilter(filters.FilterSet):
    """ Фильтры для товаров """
    name = CharFilterInFilter(field_name='name', lookup_expr='in')

    class Meta:
        model = Category
        fields = ('name',)

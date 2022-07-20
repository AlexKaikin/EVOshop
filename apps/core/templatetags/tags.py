from django import template
from apps.core.models import Category

register = template.Library()


@register.simple_tag()
def get_category_tag():
    """
    Вернет список категорий по фильтру:
    - активные
    """
    return Category.objects.filter(published='yes')

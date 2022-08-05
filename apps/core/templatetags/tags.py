from django import template

from apps.core.forms import SubscribeForm
from apps.core.models import Category

register = template.Library()


@register.simple_tag()
def get_category_tag():
    """
    Вернет список категорий по фильтру:
    - активные
    """
    return Category.objects.filter(published='yes')


@register.inclusion_tag('tags/subscribe.html')
def subscribe_form():
    """  Форма подписки на новостную рассылку """
    return {'subscribe_form': SubscribeForm()}

from apps.core.models import Category


def get_category_list():
    """
    Вернет список категорий по фильтру:
    - активные
    """
    category_list = Category.objects.filter(status='yes')
    return category_list

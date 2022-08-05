from apps.core.models import Category, Tag


def get_filter_category_list():
    """
    Вернет список товаров по фильтру:
    - совпадение слова в заголовке товара
    - активные товары
    """
    category_list = Category.objects.filter(published='yes')
    return category_list


def get_filter_tag_list():
    """ Вернет список меток к товарам """

    tag_list = Tag.objects.filter()
    return tag_list



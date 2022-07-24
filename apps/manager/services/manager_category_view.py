from apps.core.models import Category


def get_category_list():
    category_list = Category.objects.all()
    return category_list

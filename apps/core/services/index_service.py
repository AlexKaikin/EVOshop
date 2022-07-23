from django.db.models import Count, Sum, Q

from apps.core.models import Category, Product


def get_category_list():
    """
    Вернет список категорий по фильтру:
    - активные
    """
    category_list = Category.objects.filter(published='yes')
    return category_list


def get_popular_list():
    """
    Вернет список товаров по фильтру:
    - к каждому товару добавлено поле "количество заказов" на данный товар
    - сортировка по убыванию поле "количество заказов" на товар
    - отфильтруем опубликованные товары
    """
    products = Product.objects.all().annotate(count=Count("order_items")).annotate(rating=Sum('reviews__rating', filter=Q(reviews__published='yes')) / Count('reviews', filter=Q(reviews__published='yes')))
    popular_list = products.order_by('-count').filter(published='yes')[:7]
    return popular_list

from django.db.models import Count, Sum, Q

from apps.core.models import Category, Product


def get_category_list():
    """
    Вернет список категорий по фильтру:
    - активные
    """
    category_list = Category.objects.filter(published='yes')
    return category_list


def get_new_product_list():
    """
    Вернет список новых товаров:
    - активные
    """
    product_list = Product.objects.filter(published='yes').order_by('-updated', '-created')
    return product_list


def get_popular_list():
    """
    Вернет список товаров по фильтру:
    - отфильтруем опубликованные товары
    - остаток на складе больше 0
    - к каждому товару добавлено поле "количество заказов" на данный товар
    - добавляем рейтинг
    - сортировка по убыванию поле "количество заказов" на товар
    """

    products = Product.objects.filter(published='yes', stock__gt=0)\
        .annotate(count_order=Count('order_items', distinct=True))
    products = products.annotate(rating=Sum('reviews__rating', filter=Q(reviews__published='yes', reviews__rating__gt=0)) / Count('reviews__rating', filter=Q(reviews__published='yes', reviews__rating__gt=0)))
    popular_list = products.order_by('-count_order').select_related('category')[:7]
    return popular_list

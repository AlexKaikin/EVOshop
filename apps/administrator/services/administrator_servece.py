from apps.core.models import Review, Order


def get_count_review():
    """
    Вернет количество новых не проверенных отзывов:
    """
    count_review = Review.objects.all().filter(status=False).count()
    return count_review


def get_count_order():
    """
    Вернет количество новые заказы на обработку:
    """
    count_order = Order.objects.all().filter(status=1).count()
    return count_order

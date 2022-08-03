from django.db.models import Count, Sum, F, Q
from django.db.models.functions import TruncDay, TruncMonth

from apps.core.models import Review, Order, OrderItem


def get_count_review():
    """ Вернет количество новых не проверенных отзывов: """
    count_review = Review.objects.all().filter(published='checking').count()
    return count_review


def get_count_order():
    """ Вернет количество новые заказы на обработку: """
    count_order = Order.objects.all().filter(status=1).count()
    return count_order


def get_orders_day():
    """ Вернет количество заказов в день: """
    orders_day = (Order.objects.all()
                  .annotate(day=TruncDay('created'))
                  .values('day')
                  .annotate(count_order=Count('created'))
                  .annotate(count_order_cancelled=Count('created', filter=Q(status='2')))
                  .annotate(count_order_paid=Count('created', filter=Q(paid='yes')))
                  .values('day', 'count_order', 'count_order_cancelled', 'count_order_paid')
                  .order_by('day')
                  )
    return orders_day


def get_orders_month():
    """ Вернет количество заказов в месяц: """
    orders_month = (Order.objects.all()
                    .annotate(month=TruncMonth('created'))
                    .values('month')
                    .annotate(count_order=Count('created'))
                    .annotate(count_order_cancelled=Count('created', filter=Q(status='2')))
                    .annotate(count_order_paid=Count('created', filter=Q(paid='yes')))
                    .values('month', 'count_order', 'count_order_cancelled', 'count_order_paid')
                    .order_by('month')
                    )
    return orders_month


def get_profit_day():
    """ Вернет сумму заказов в день: """
    orders_month = (OrderItem.objects.all()
                    .annotate(day=TruncDay('created'))
                    .values('day')
                    .annotate(count_profit=Sum(F('price')*F('quantity')))
                    .annotate(count_profit_cancelled=Sum(F('price') * F('quantity'), filter=Q(order__status='2')))
                    .annotate(count_profit_paid=Sum(F('price') * F('quantity'), filter=Q(order__paid='yes')))
                    .values('day', 'count_profit', 'count_profit_cancelled', 'count_profit_paid')
                    .order_by('day')
                    )
    return orders_month


def get_profit_month():
    """ Вернет сумму заказов в месяц: """
    orders_month = (OrderItem.objects.all()
                    .annotate(month=TruncMonth('created'))
                    .values('month')
                    .annotate(count_profit=Sum(F('price')*F('quantity')))
                    .annotate(count_profit_cancelled=Sum(F('price') * F('quantity'), filter=Q(order__status='2')))
                    .annotate(count_profit_paid=Sum(F('price') * F('quantity'), filter=Q(order__paid='yes')))
                    .values('month', 'count_profit', 'count_profit_cancelled', 'count_profit_paid')
                    .order_by('month')
                    )
    return orders_month

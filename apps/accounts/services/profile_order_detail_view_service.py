from django.db.models import Sum, F, FloatField

from apps.core.models import Order, Setting, OrderItem


def get_order(self):
    """ Вернёт ордер """
    pk = self.kwargs['pk']
    order = Order.objects.get(pk=pk)
    return order


def get_delivery_free():
    """ Вернёт сумму бесплатной доставки """
    number = Setting.objects.get(pk=1)
    delivery_free = number.delivery_free
    return delivery_free


def get_product_list(self):
    """ Вернёт список товаров в заказе """
    pk = self.kwargs['pk']
    product_list = (OrderItem.objects.filter(order__pk=pk).select_related('product')
                    .annotate(total_cost=Sum(F('price')*F('quantity')))
                    )
    return product_list

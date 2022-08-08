from apps.core.models import Order


def get_order_list():
    order_list = Order.objects.all()
    return order_list

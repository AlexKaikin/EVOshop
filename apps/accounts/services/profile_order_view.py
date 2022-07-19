from apps.core.models import Order


def get_order_list(self):
    pk = self.kwargs['pk']
    order_list = Order.objects.filter(profile_id=pk)
    return order_list

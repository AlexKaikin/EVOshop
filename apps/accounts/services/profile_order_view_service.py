from apps.core.models import Order


def get_order_list(self):
    slug = self.kwargs['slug']
    order_list = Order.objects.filter(profile__slug=slug)
    return order_list

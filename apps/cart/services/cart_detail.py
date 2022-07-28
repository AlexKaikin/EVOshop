from apps.core.models import Setting


def get_delivery_free():
    number = Setting.objects.get(pk=1)
    delivery_free = number.delivery_free
    return delivery_free


def get_delivery():
    number = Setting.objects.get(pk=1)
    delivery = number.delivery
    return delivery

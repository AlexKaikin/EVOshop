from apps.core.models import Setting


def get_setting_delivery():
    setting_delivery = Setting.objects.get(pk=1)
    return setting_delivery


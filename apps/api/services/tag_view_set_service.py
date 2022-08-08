from apps.core.models import Tag


def get_tag_list():
    return Tag.objects.all()
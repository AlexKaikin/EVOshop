from apps.core.models import Review


def get_review_list():
    return Review.objects.filter(published='yes')
from apps.core.models import Review


def get_review_list(self):
    review_list = Review.objects.all().select_related('profile').select_related('product')
    return review_list

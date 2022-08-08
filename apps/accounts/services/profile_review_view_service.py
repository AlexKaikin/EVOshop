from apps.core.models import Review


def get_review_list(self):
    slug = self.kwargs['slug']
    review_list = Review.objects.filter(profile__slug=slug).select_related('product')
    return review_list

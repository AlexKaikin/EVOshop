from apps.core.models import Review


def get_review_list(self):
    pk = self.kwargs['pk']
    review_list = Review.objects.filter(profile_id=pk).select_related('product')
    return review_list

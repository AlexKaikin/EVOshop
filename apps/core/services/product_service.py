from django.db.models import Count, Q, Sum
from apps.core.models import Review, ProductImage, Product


def get_product(self):
    """ Вернет товар, количество у него опубликованных отзывов и рейтинг"""
    slug = self.kwargs['slug']
    return (Product.objects.filter(slug=slug)
            .annotate(count_review=Count('reviews', filter=Q(reviews__published='yes', reviews__rating__gt=0)))
            .annotate(rating=Sum('reviews__rating', filter=Q(reviews__published='yes', reviews__rating__gt=0)) / Count('reviews', filter=Q(reviews__published='yes', reviews__rating__gt=0)))
            .prefetch_related('tag')
            )


def get_review_list(self):
    """
    Вернет список отзывов по фильтру:
    - опубликованные
    """
    slug = self.kwargs['slug']
    review_list = Review.objects.filter(product__slug=slug, published='yes', parent__isnull=True).select_related('profile')
    return review_list


def get_images_list(self):
    """ Вернет список фотографий """
    slug = self.kwargs['slug']
    image_list = ProductImage.objects.filter(product__slug=slug).all()
    return image_list

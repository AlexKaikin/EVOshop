from django.db.models import Count, Q
from apps.core.models import Review, ProductImage, Product


def get_product(self):
    """ Вернет товар и количество у него опубликованных отзывов """
    slug = self.kwargs['slug']
    return Product.objects.filter(slug=slug).annotate(count=Count('reviews', filter=Q(reviews__status='2')))


def get_review_list(self):
    """
    Вернет список отзывов по фильтру:
    - опубликованные
    """
    slug = self.kwargs['slug']
    review_list = Review.objects.filter(product__slug=slug, status='2').select_related('profile')
    return review_list


def get_images_list(self):
    """ Вернет список фотографий """
    slug = self.kwargs['slug']
    image_list = ProductImage.objects.filter(product__slug=slug).all()
    return image_list

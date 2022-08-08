from django.http import JsonResponse
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .services.category_view_set_service import get_category_list, CategoryFilter
from .services.product_view_set_service import get_product_list, get_category_for_product, get_reviews_for_product, \
    ProductFilter
from .services.review_view_st_service import get_review_list
from .utils import Paginator
from .services.tag_view_set_service import get_tag_list
from .services.validate_email_service import get_email_validate
from .services.validate_username_service import get_username_validate
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, \
    TagSerializer, ReviewCreateSerializer, ProductCreateSerializer


def validate_username(request):
    """ Проверка доступности логина """
    response = {'username_taken': get_username_validate(request)}
    return JsonResponse(response)


def validate_email(request):
    """ Проверка доступности e-mail """
    response = {'email_taken': get_email_validate(request)}
    return JsonResponse(response)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """ Представление категорий """
    queryset = get_category_list()
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer
    pagination_class = Paginator
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter


class CategoryCreateView(generics.CreateAPIView):
    """ Представление добавления категории """
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """ Представление товаров """
    queryset = get_product_list()
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    pagination_class = Paginator
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        category = get_category_for_product(pk)
        return Response({'category': category.name})

    @action(methods=['get'], detail=True)
    def reviews(self, request, pk=None):
        reviews = get_reviews_for_product(pk)
        return Response({'reviews': [review.description for review in reviews]})


class ProductCreateView(generics.CreateAPIView):
    """ Представление добавления товара """
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductCreateSerializer


class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    """ Представление отзывов """
    queryset = get_review_list()
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = ReviewSerializer
    pagination_class = Paginator


class ReviewCreateView(generics.CreateAPIView):
    """ Добавление отзыва """
    serializer_class = ReviewCreateSerializer


class TagViewSet(viewsets.ModelViewSet):
    """ Представление меток к товарам """
    queryset = get_tag_list()
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = TagSerializer
    pagination_class = Paginator

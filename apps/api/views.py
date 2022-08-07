from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from apps.core.models import Category, Product, Review, Tag

from .service import ProductFilter
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, \
    TagSerializer, ReviewCreateSerializer, ProductCreateSerializer


class Paginator(PageNumberPagination):
    """ Пагинация """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """ Представление категорий """
    queryset = Category.objects.filter(published='yes')
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer
    pagination_class = Paginator


class CategoryCreateView(generics.CreateAPIView):
    """ Представление категорий """
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """ Представление товаров """
    queryset = Product.objects.filter(published='yes', stock__gt=0)
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductSerializer
    pagination_class = Paginator
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        category = Category.objects.get(pk=pk)
        return Response({'category': category.name})

    @action(methods=['get'], detail=True)
    def reviews(self, request, pk=None):
        reviews = Review.objects.filter(product=pk)
        return Response({'reviews': [review.description for review in reviews]})


class ProductCreateView(generics.CreateAPIView):
    """ Представление добавления товара """
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductCreateSerializer


class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    """ Представление отзывов """
    queryset = Review.objects.filter(published='yes')
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = ReviewSerializer
    pagination_class = Paginator


class ReviewCreateView(generics.CreateAPIView):
    """ Добавление отзыва """
    serializer_class = ReviewCreateSerializer


class TagViewSet(viewsets.ModelViewSet):
    """ Представление меток к товарам """
    queryset = Tag.objects.all()
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = TagSerializer
    pagination_class = Paginator

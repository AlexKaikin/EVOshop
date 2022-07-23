from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from apps.core.models import Category, Product, Review

from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer


class Paginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer
    pagination_class = Paginator


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductSerializer
    pagination_class = Paginator

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        category = Category.objects.get(pk=pk)
        return Response({'category': category.name})

    @action(methods=['get'], detail=True)
    def reviews(self, request, pk=None):
        reviews = Review.objects.filter(product=pk)
        return Response({'reviews': [review.description for review in reviews]})


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = ReviewSerializer
    pagination_class = Paginator

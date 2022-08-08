from django.urls import path
from rest_framework import routers

from . import views
from .views import CategoryViewSet, ProductViewSet, ReviewViewSet, TagViewSet

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)
router.register('review', ReviewViewSet)
router.register('tag', TagViewSet)

urlpatterns = [
                  path('category_create/', views.CategoryCreateView.as_view()),
                  path('product_create/', views.ProductCreateView.as_view()),
                  path('review_create/', views.ReviewCreateView.as_view()),

                  path('validate_username/', views.validate_username, name='validate_username'),
                  path('validate_email/', views.validate_email, name='validate_email'),
              ] + router.urls

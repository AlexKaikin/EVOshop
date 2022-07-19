from django.urls import path
from apps.core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='category'),
    path('category/product/<slug:slug>/', views.ProductView.as_view(), name='product'),
    path('search/', views.SearchView.as_view(), name='search'),
    # static
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]

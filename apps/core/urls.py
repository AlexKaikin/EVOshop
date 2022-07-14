from django.urls import path, re_path
from apps.core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='main'),
    path('catalog/<slug:slug>/', views.CatalogView.as_view(), name='catalog'),
    path('catalog/product/<slug:slug>/', views.ProductView.as_view(), name='product'),
    path('search/', views.SearchView.as_view(), name='search'),
    re_path(r'^create/$', views.order_create, name='order_create'),
    # static
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('404-page/', views.no_page, name='no_page'),
]

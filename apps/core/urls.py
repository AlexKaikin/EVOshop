from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('filter/', views.FilterProductView.as_view(), name='filter'),
    path('favourite/<int:id>', views.favourite_add, name='favourite_add'),
    path('favourite/', views.FavouriteView.as_view(), name='favourite_list'),
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='category'),
    path('category/product/<slug:slug>/', views.ProductView.as_view(), name='product'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('contacts/', views.ContactView.as_view(), name='contacts'),
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    path('about/', views.about, name='about'),
]

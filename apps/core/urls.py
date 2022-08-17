from django.urls import path, re_path

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

    # path('compare/', views.compare_list, name='compare_list'),
    # path('compare/add/', views.add_compare_list, name='add_compare_list'),
    # path('compare/remove/', views.remove_compare_list, name='remove_compare_list'),
    # path('compare/delete/', views.delete_compare_list, name='delete_compare_list'),
    # path('compare/api/', views.compare_api, name='compare_api'),

    re_path(r'^compare/$', views.compare_detail, name='compare_detail'),
    re_path(r'^compare/add/(?P<product_id>\d+)/$', views.compare_add, name='compare_add'),
    re_path(r'^compare/remove/(?P<product_id>\d+)/$', views.compare_remove, name='compare_remove'),

    path('about/', views.about, name='about'),
]

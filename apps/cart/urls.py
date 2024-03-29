from django.urls import re_path

from apps.cart import views

urlpatterns = [
    re_path(r'^$', views.cart_detail, name='cart_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    re_path(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    re_path(r'^create/$', views.order_create, name='order_create'),
]

from django.urls import path
from main.views import index, about, contacts, tea, coffee, spices, product

urlpatterns = [
    path('', index, name='main'),
    path('about.html', about, name='about'),
    path('contacts.html', contacts, name='contacts'),
    path('catalog/tea/', tea, name='tea'),
    path('catalog/coffee/', coffee, name='coffee'),
    path('catalog/spices/', spices, name='spices'),
    path('catalog/product/<int:id>', product, name='product'),
]

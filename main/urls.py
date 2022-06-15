from django.urls import path
from main.views import index, about, contacts, tea, coffee, spices

urlpatterns = [
    path('', index, name='main'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/tea/', tea, name='tea'),
    path('catalog/coffee/', coffee, name='coffee'),
    path('catalog/spices/', spices, name='spices'),
]

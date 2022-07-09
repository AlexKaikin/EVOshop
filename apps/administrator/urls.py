from django.urls import path
from apps.administrator import views

urlpatterns = [
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    path('catalog/product/<slug:slug>/edit_product/', views.EditProductView.as_view(), name='edit_product'),
    path('catalog/product/<slug:slug>/delete_product/', views.delete_product, name='delete_product'),
]
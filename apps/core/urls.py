from django.urls import path
from apps.core import views

urlpatterns = [
    # accounts
    path('register/', views.RegisterForm.as_view(), name='register'),
    path('login/', views.LoginForm.as_view(), name='login'),
    path('logout/', views.LogOutForm.as_view(), name='logout'),
    # apps core
    path('', views.IndexView.as_view(), name='main'),
    path('catalog/<slug:slug>/', views.CatalogView.as_view(), name='catalog'),
    path('catalog/product/<slug:slug>/', views.product_detail, name='product'),
    # path('catalog/product/<slug:slug>/', views.ProductView.as_view(), name='product'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    # edit
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    path('catalog/product/<slug:slug>/edit_product/', views.EditProductView.as_view(), name='edit_product'),
    path('catalog/product/<slug:slug>/delete_product/', views.delete_product, name='delete_product'),
    # static
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]

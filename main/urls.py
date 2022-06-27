from django.urls import path
from main import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.RegisterForm.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('', views.index, name='main'),
    path('about.html', views.about, name='about'),
    path('contacts.html', views.contacts, name='contacts'),
    path('catalog/tea/', views.tea, name='tea'),
    path('catalog/coffee/', views.coffee, name='coffee'),
    path('catalog/spices/', views.spices, name='spices'),
    path('catalog/product/<int:pk>', views.ProductView.as_view(), name='product'),
    path('catalog/product/<int:pk>', views.AddReviewView.as_view(), name='view'),
]

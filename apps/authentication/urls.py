from django.urls import path
from apps.authentication import views

urlpatterns = [
    path('register/', views.RegisterForm.as_view(), name='register'),
    path('login/', views.LoginForm.as_view(), name='login'),
    path('logout/', views.LogOutForm.as_view(), name='logout'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/update_profile/', views.UpdateProfileView.as_view(), name='update_profile'),
]

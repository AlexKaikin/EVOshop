from django.urls import path
from apps.accounts import views

urlpatterns = [
    path('register/', views.RegisterForm.as_view(), name='register'),
    path('login/', views.LoginForm.as_view(), name='login'),
    path('logout/', views.LogOutForm.as_view(), name='logout'),

    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/order/', views.ProfileOrderView.as_view(), name='profile_order'),
    path('profile/order/<int:pk>', views.ProfileOrderDetailView.as_view(), name='profile_order_detail'),
    path('profile/<int:pk>/review/', views.ProfileReviewView.as_view(), name='profile_review'),
]

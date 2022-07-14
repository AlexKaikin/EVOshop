from django.urls import path
from apps.administrator import views

urlpatterns = [
    path('', views.administrator, name='administrator'),

    path('category/', views.AdminCategoryView.as_view(), name='admin_category'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('category/<slug:slug>/update_category/', views.UpdateCategoryView.as_view(), name='update_category'),
    path('category/<slug:slug>/delete_category/', views.delete_category, name='delete_category'),

    path('product/', views.AdminProductView.as_view(), name='admin_product'),
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    path('product/<slug:slug>/update_product/', views.UpdateProductView.as_view(), name='update_product'),
    path('product/<slug:slug>/delete_product/', views.delete_product, name='delete_product'),

    path('review/', views.AdminReviewView.as_view(), name='admin_review'),
    path('review/<int:pk>/update_review/', views.UpdateReviewView.as_view(), name='update_review'),
    path('review/<int:pk>/delete_review/', views.delete_review, name='delete_review'),

    path('order/', views.AdminOrderView.as_view(), name='admin_order'),
    path('order/<int:pk>/update_order/', views.UpdateOrderView.as_view(), name='update_order'),
    path('order/<int:pk>/delete_order/', views.delete_order, name='delete_order'),
]
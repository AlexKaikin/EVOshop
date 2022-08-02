from django.urls import path
from apps.manager import views

urlpatterns = [
    path('', views.manager, name='manager'),

    path('category/', views.ManagerCategoryView.as_view(), name='manager_category'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('category/<slug:slug>/update_category/', views.UpdateCategoryView.as_view(), name='update_category'),
    path('category/<slug:slug>/delete_category/', views.delete_category, name='delete_category'),

    path('product/', views.ManagerProductView.as_view(), name='manager_product'),
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    path('product/<slug:slug>/update_product/', views.UpdateProductView.as_view(), name='update_product'),
    path('product/<slug:slug>/delete_product/', views.delete_product, name='delete_product'),

    path('review/', views.ManagerReviewView.as_view(), name='manager_review'),
    path('review/<int:pk>/update_review/', views.UpdateReviewView.as_view(), name='update_review'),
    path('review/<int:pk>/delete_review/', views.delete_review, name='delete_review'),

    path('order/', views.ManagerOrderView.as_view(), name='manager_order'),
    path('order/<int:pk>/update_order/', views.UpdateOrderView.as_view(), name='update_order'),
    path('order/<int:pk>/delete_order/', views.delete_order, name='delete_order'),

    path('setting/<int:pk>', views.ManagerSettingView.as_view(), name='manager_setting'),
]

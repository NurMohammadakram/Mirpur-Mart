from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_product/', views.add_product, name='add_product'),
    path('all_products/', views.all_products, name='all_products'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
]
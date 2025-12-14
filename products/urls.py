from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_product/', views.add_product, name='add_product'),
    path('all_products/', views.all_products, name='all_products'),
]
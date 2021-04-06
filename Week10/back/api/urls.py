from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', greet),
    path('products/', get_products),
    path('products/<int:product_id>/', get_product_details),
    path('categories/', get_categories),
    path('categories/<int:category_id>/', get_category)
]
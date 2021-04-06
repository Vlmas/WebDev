from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *

def greet(request):
    return HttpResponse('<p style="text-align: center; margin-top: 220px; font-size: 25px; text-decoration: underline;">Hello, World!</p>')

def get_products(request):
    products = ProductItem.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False, status=200)

def get_product_details(request, product_id):
    try:
        product = ProductItem.objects.get(id=product_id).to_json()
        return JsonResponse(product)
    except ProductItem.DoesNotExist as dne:
        return JsonResponse({'message': str(dne)}, status=400)

def get_categories(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False, status=200)

def get_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id).to_json()
        return JsonResponse(category)
    except Category.DoesNotExist as dne:
        return JsonResponse({'message': str(dne)}, status=400)
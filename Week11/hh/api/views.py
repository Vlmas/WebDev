from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json

def greet(request):
    return HttpResponse('<p style="text-align: center; margin-top: 220px; font-size: 25px; text-decoration: underline;">Hello, Django!</p>')

@csrf_exempt
def manage_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            company = Company.objects.create(
                name=data['name'], 
                description=data['description'], 
                city=data['city'],
                address=data['address']
            )
        except Exception as exc:
            return JsonResponse({'message': exc.__str__()}, status=400)
        
        return JsonResponse(company.to_json())

@csrf_exempt
def manage_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as exc:
        return JsonResponse({'message': exc.__str__()}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        company.name = data['name']
        company.description = data['description']
        company.city = data['city']
        company.address = data['address']
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message': 'deleted'})

@csrf_exempt
def manage_vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            vacancy = Vacancy.objects.create(
                name=data['name'],
                description=data['description'],
                salary=data['salary'],
                company=data['company']
            )
        except Exception as exc:
            return JsonResponse({'message': exc.__str__()}, status=400)
        
        return JsonResponse(vacancy.to_json())

@csrf_exempt
def manage_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as exc:
        return JsonResponse({'message': exc.__str__()}, status=400)
    
    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        vacancy.name = data['name']
        vacancy.description = data['description']
        vacancy.salary = data['salary']
        vacancy.company = data['company']
        vacancy.save()
        return JsonResponse(vacancy.to_json())
    elif reqeust.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'message': 'deleted'})

def get_vacancies_by_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as exc:
        return JsonResponse({'message': exc.__str__()}, status=400)
    
    vacancies = Vacancy.objects.filter(company=company)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def get_top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)
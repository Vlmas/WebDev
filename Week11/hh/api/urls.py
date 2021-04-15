from django.urls import path
from .views import *

urlpatterns = [
    path('', greet),
    path('companies/', manage_companies),
    path('companies/<int:company_id>/', manage_company),
    path('companies/<int:company_id>/vacancies/', get_vacancies_by_company),
    path('vacancies/', manage_vacancies),
    path('vacancies/<int:vacancy_id>/', manage_vacancy),
    path('vacancies/top_ten/', get_top_ten_vacancies),
]
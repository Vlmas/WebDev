from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def respond(request):
    return HttpResponse('<p>Test</p>')

def default(request):
    return HttpResponse('<p>Default</p>')
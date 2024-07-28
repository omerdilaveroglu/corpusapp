from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request=request,template_name='index.html')

def hour_production(request):
    return render(request=request,template_name='hour_production.html')
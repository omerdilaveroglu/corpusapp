from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('',views.index,name='home_page'),
    path('hour_production',views.hour_production,name='hour_production'),
]
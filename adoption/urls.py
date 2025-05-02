from django import views
from django.contrib import admin
from django.urls import path
import adoption

urlpatterns = [

    path('adopt/', adoption.views.adoption_request, name='adopt'),
    path('adoption-success/', views.adoption_success, name='adoption_success'),
    ]

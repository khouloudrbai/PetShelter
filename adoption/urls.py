from django.contrib import admin
from django.urls import path
from .views import PetsListView,AdoptPet
urlpatterns = [
    path('pets/', PetsListView.as_view(), name='pets-list'),
    path('adopt/<str:pet_name>/', AdoptPet, name='adopt-pet'),
    ]

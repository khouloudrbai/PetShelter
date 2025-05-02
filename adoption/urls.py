from django import views
from django.contrib import admin
from django.urls import path
import adoption
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('adopt/', adoption.views.adoption_request, name='adopt'),
    path('adopt/<int:pet_id>/', adoption.views.adopt_pet, name='adopt_pet'),

    path('home/', adoption.views.home, name='home'),
    path('about/', adoption.views.about, name='about'),
    path('pets/', adoption.views.Pets, name='Pets'),
    path('volunteer/', adoption.views.volunteer, name='volunteer'),
    path('contact/', adoption.views.contact, name='contact'),

    path('adoption-success/', views.adoption_success, name='adoption_success'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

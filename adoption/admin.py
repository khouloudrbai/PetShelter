from django.contrib import admin
from adoption.models import Shelter,Adoption,Pet
# Register your models here.
admin.site.register(Shelter)
admin.site.register(Adoption)
admin.site.register(Pet)

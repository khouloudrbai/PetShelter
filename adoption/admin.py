from django.contrib import admin
from adoption.models import Shelter,Adoption,Pet,Note,Volunteer
# Register your models here.
admin.site.register(Shelter)
admin.site.register(Adoption)
admin.site.register(Pet)
admin.site.register(Note)
admin.site.register(Volunteer)

from django import forms
from .models import Adoption

class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = ['adopter_name', 'phone_number', 'pet', 'adoption_date']


from datetime import timezone
from django import forms
from .models import Adoption, Volunteer

class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = ['adopter_name', 'phone_number', 'pet', 'adoption_date']




class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'help_description': forms.Textarea(attrs={'rows': 4}),
            'donation_date': forms.DateInput(attrs={'type': 'date'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].initial = 'Sousse'
       
        # Make fields required conditionally
        self.fields['amount'].required = False
        self.fields['card_number'].required = False
        self.fields['donation_date'].required = False
        self.fields['start_date'].required = False
        self.fields['end_date'].required = False
        self.fields['help_description'].required = False
        self.fields['availability'].required = False


    def clean(self):
        cleaned_data = super().clean()
        help_type = cleaned_data.get('help_type')
       
        if help_type == 'money':
            if not cleaned_data.get('amount'):
                self.add_error('amount', 'This field is required for donations')
            if not cleaned_data.get('donation_date'):
                self.add_error('donation_date', 'This field is required for donations')
            if not cleaned_data.get('card_number'):
                self.add_error('card_number', 'This field is required for donations')
       
        if help_type == 'help':
            if not cleaned_data.get('start_date'):
                self.add_error('start_date', 'This field is required for volunteering')
            if not cleaned_data.get('end_date'):
                self.add_error('end_date', 'This field is required for volunteering')
            if cleaned_data.get('start_date') and cleaned_data.get('end_date'):
                if cleaned_data['start_date'] > cleaned_data['end_date']:
                    self.add_error('end_date', 'End date must be after start date')
                if cleaned_data['start_date'] < timezone.now().date():
                    self.add_error('start_date', 'Start date cannot be in the past')


        return cleaned_data
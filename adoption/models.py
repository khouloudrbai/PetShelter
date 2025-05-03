from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator,RegexValidator
from django.forms import ValidationError
from django.utils import timezone
class Shelter(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    age = models.IntegerField()
    available_for_adoption = models.BooleanField()
    image=models.ImageField(upload_to='shelter_logo/',null=True,blank=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)

    def __str__(self):
        return  self.name

class Adoption(models.Model):
    adopter_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    adoption_date = models.DateTimeField()
    def __str__(self):
        return f"{self.adopter_name} adopted {self.pet.name}"



class Note(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"
    


class Volunteer(models.Model):
    HELP_CHOICES = [
        ('money', 'Financial Donation'),
        ('help', 'Volunteer Time (Cleaning & Animal Care)'),
    ]
   
    AVAILABILITY_CHOICES = [
        ('1-5', '1-5 hours'),
        ('5-10', '5-10 hours'),
        ('10-20', '10-20 hours'),
        ('20+', '20+ hours'),
    ]


    # Personal Info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100, default='Sousse')
    state = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', "Phone number must be entered in the format: '+999999999'.")]
    )
    email = models.EmailField()
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(120)]
    )


    # Shelter related
    shelter = models.ForeignKey('Shelter', on_delete=models.CASCADE)


    # Volunteering Info
    help_type = models.CharField(max_length=10, choices=HELP_CHOICES)
    help_description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        null=True,
        blank=True
    )


    # Financial donation
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    donation_date = models.DateField(null=True, blank=True)
    card_number = models.CharField(max_length=16, null=True, blank=True)


    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)  # Sera automatiquement rempli


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_help_type_display()}"


    def clean(self):
        super().clean()
        if self.help_type == 'money':
            if not self.amount:
                raise ValidationError({'amount': 'Amount is required for financial donations'})
            if not self.donation_date:
                raise ValidationError({'donation_date': 'Donation date is required'})
            if not self.card_number:
                raise ValidationError({'card_number': 'Card number is required'})
       
        if self.help_type == 'help':
            if not self.start_date:
                raise ValidationError({'start_date': 'Start date is required'})
            if not self.end_date:
                raise ValidationError({'end_date': 'End date is required'})
            if self.start_date and self.end_date and self.start_date > self.end_date:
                raise ValidationError({'end_date': 'End date must be after start date'})

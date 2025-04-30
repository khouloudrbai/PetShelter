from django.db import models





class Shelter(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    age = models.IntegerField(max_length=30)
    available_for_adoption = models.BooleanField()
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    def __str__(self):
        return  self.name

class Adoption(models.Model):
    adopter_name = models.CharField(max_length=30)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    adoption_date = models.DateTimeField()
    def __str__(self):
        return f"{self.adopter.username} adopted {self.pet.name}"


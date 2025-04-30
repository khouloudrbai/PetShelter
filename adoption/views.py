from datetime import timezone
from django.shortcuts import render, get_object_or_404, redirect
from adoption.models import Pet,Adoption
from django.views.generic import ListView
from django.http import HttpResponse

# Create your views here.
#afficher liste des pets available 
class PetsListView(ListView):
    model = Pet
    template_name = 'adoption/pet_list.html'
    context_object_name = 'pets'

    def get_List(self):
        return Pet.objects.filter(available_for_adoption=True)[:5]

def AdoptPet(request,pet_name):
     # Get the pet to be adopted
    pet = get_object_or_404(Pet, name=pet_name)

    if request.method == "POST":
        adopter_name = request.POST.get("adopter_name")
        adoption_date = request.POST.get("adoption_date") or timezone.now().date()
    
        # Create a new adoption entry
        adoption=Adoption.objects.create(
            pet=pet, 
            adopter_name=adopter_name,
              adoption_date=request.POST.get("adoption_date"))
    
        pet.available_for_adoption=False
        pet.save()

        return HttpResponse('Adoption Successfull')

    return render(request, 'adoption/adopt_pet.html', {'pet': pet})

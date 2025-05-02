from django.shortcuts import get_object_or_404, render, redirect

from .models import Pet


from .forms import AdoptionForm


def adoption_request(request):
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adoption_success')  
    else:
        form = AdoptionForm()
    return render(request, 'Adoption.html', {'form': form})



def adopt_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            adoption = form.save(commit=False)
            adoption.pet = pet
            adoption.save()
            # Redirect or show success
    else:
        form = AdoptionForm(initial={'pet': pet})

    return render(request, 'Adoption.html', {'form': form, 'pet': pet})

def home(request):
    
    return render(request, 'index.html')

def about(request):
    
    return render(request, 'about.html')

def Pets(request):
    pets = Pet.objects.filter(available_for_adoption=False)
    return render(request, 'Pets.html', {'pets': pets})



def dogs(request):
    
    return render(request, 'dogs.html')

def contact(request):
    
    return render(request, 'contact.html')

def volunteer(request):
    
    return render(request, 'volunteer.html')

def adoption_success(request):
    return render(request, 'adoption_success.html')


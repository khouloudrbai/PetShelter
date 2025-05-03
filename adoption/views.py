from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect

from .models import Pet,Note, Shelter, Volunteer

from django.contrib import messages

from .forms import AdoptionForm, VolunteerForm


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



def submit_note(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Note.objects.create(name=name, email=email, subject=subject, message=message)
        return redirect('home') 
    return render(request, 'index.html')

    
def home(request):
    notes = Note.objects.all().order_by('-id')[:5]  # latest 5
    return render(request, 'index.html', {'notes': notes})



    


def about(request):
    
    return render(request, 'about.html')

def Pets(request):
    pets = Pet.objects.filter(available_for_adoption=True)
    return render(request, 'Pets.html', {'pets': pets})



def dogs(request):
    
    return render(request, 'dogs.html')

def contact(request):
    
    return render(request, 'contact.html')

def volunteer(request):
    shelters = Shelter.objects.all()
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Thank you for your submission!')
                return redirect('home')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
        else:
            # Affichez les erreurs de validation
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = VolunteerForm()
   
    return render(request, 'volunteer.html', {
        'form': form,
        'shelters': shelters  # Corrigé de 'shelter' à 'shelters'
    })






def adoption_success(request):
    return render(request, 'index.html')


from django.shortcuts import render, redirect


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


def adoption_success(request):
    return render(request, 'adoption_success.html')
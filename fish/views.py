from django.shortcuts import render, redirect
from .models import FirstTable
from .forms import FirstTableForm
# Create your views here.


def fish_home(request):
    fish = FirstTable.objects.all()
    if request.method == 'POST':
        if fish.is_valid():
            fish.save()
            return redirect('/fish')
    return render(request, 'fish/fish_home.html', {'fish': fish})


def create(request):
    error = ''
    if request.method == 'POST':
        form = FirstTableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('/fish')

        else:
            error = "Incorrect form of filling in"
    form = FirstTableForm()
    data = {'form': form,
            'error': error}
    return render(request, 'fish/create.html', data)




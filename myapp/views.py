from django.shortcuts import redirect, render
from .models import AddsForm, FirstCat, FirstCatForm, SecondCat, Adds, SecondCatForm

def home(request):
    return render(request, 'home.html')

def first_cat_view(request):
    if request.method == 'POST':
        form = FirstCatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('first_cat')
    else:
        form = FirstCatForm()

    first_cats = FirstCat.objects.all()
    return render(request, 'first_cat.html', {'first_cats': first_cats, 'form': form})

def second_cat_view(request):
    if request.method == 'POST':
        form = SecondCatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('second_cat')
    else:
        form = SecondCatForm()

    second_cats = SecondCat.objects.all()
    return render(request, 'second_cat.html', {'second_cats': second_cats, 'form': form})

def adds_view(request):
    if request.method == 'POST':
        form = AddsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adds')
    else:
        form = AddsForm()

    adds = Adds.objects.all()
    return render(request, 'adds.html', {'adds': adds, 'form' : form})
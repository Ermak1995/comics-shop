from django.shortcuts import render, redirect
from .forms import *
from .models import *


def index(request):
    model = Comics.objects.all()
    return render(request, 'home/index.html', {'model': model})


def comics(request):
    return render(request, 'home/comics.html')


def add_comics(request):
    if request.method == 'POST':
        form = ComicsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ComicsForm()

    return render(request, 'home/add_comics.html', {'form': form})


def cart(request):
    model = Comics.objects.filter(buy_status=True)
    return render(request, 'home/cart.html', {'model': model})

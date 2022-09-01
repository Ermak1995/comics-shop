from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *

count = Comics.objects.filter(buy_status=True).count


def index(request):
    model = Comics.objects.all()

    return render(request, 'home/index.html', {'model': model, 'count': count})


def dccomics(request):
    model = Comics.objects.filter(publisher='DC Comics')
    return render(request, 'home/dccomics.html', {'model': model})


def add_comics(request):
    if request.method == 'POST':
        form = ComicsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ComicsForm()

    return render(request, 'home/add_comics.html', {'form': form})


def add_publisher(request):
    if request.method == 'POST':
        form = PublishersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_comics')
    else:
        form = PublishersForm()
    return render(request, 'home/add_publisher.html', {'form': form})


def cart(request):
    model = Comics.objects.filter(buy_status=True)
    return render(request, 'home/cart.html', {'model': model, 'count': count})


def view_comics(request, view_comics_id):
    # if request.method == 'POST':
    buy_comics = Comics.objects.get(pk=view_comics_id)
    buy_comics.buy_status = True
    buy_comics.save()
    return redirect('index')
    # return HttpResponse(f'Страница с номером: {view_comics_id}')

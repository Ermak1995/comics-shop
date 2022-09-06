from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView

count = Comics.objects.filter(buy_status=True).count


class IndexView(ListView):
    model = Comics
    template_name = 'home/index.html'
    extra_context = {'count': count}


# def index(request):
#     model = Comics.objects.all()
#
#     return render(request, 'home/index.html', {'model': model, 'count': count})

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
    return render(request, 'home/cart.html', {'count': count})


def view_comics(request, view_comics_id):
    product = Comics.objects.get(pk=view_comics_id)
    if 'add' in request.POST:
        product.buy_status = True
    elif 'purchased' in request.POST:
        product.buy_status = False
    product.save()
    return redirect('index')


# return HttpResponse(f'Страница с номером: {view_comics_id}')


# def delete_comics_from_cart(request, delete_comics_from_cart_id):
#     delete_comics = Comics.objects.get(pk=delete_comics_from_cart_id)
#     delete_comics.buy_status = False
#     delete_comics.save()
#     return redirect('cart')

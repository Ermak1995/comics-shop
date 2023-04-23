from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import Comics_create_json
from django.views.generic import ListView, DetailView
from django.contrib import messages


count = Comics_create_json.objects.filter(buy_status=True).count


# class IndexView(ListView):
#     model = Comics_create_json
#     template_name = 'home/index.html'

# def pop_items(self, request):
#     if 'pop_items' in request.post:
#         model = Comics.objects.order_by('quantity_purchased')

class ReadMore(DetailView):
    model = Comics_create_json
    template_name = 'home/readmore.html'
    pk_url_kwarg = 'readmore_id'
    context_object_name = 'm'



def index(request):
    if 'title' in request.POST:
        model = Comics_create_json.objects.order_by('title')
    elif 'price' in request.POST:
        model = Comics_create_json.objects.order_by('price')
    else:
        model = Comics_create_json.objects.all()

    return render(request, 'home/index.html', {'model': model})


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
    model = Comics_create_json.objects.filter(buy_status=True)
    return render(request, 'home/cart.html', {'model': model})


def view_comics(request, view_comics_id):
    product = Comics_create_json.objects.get(pk=view_comics_id)
    if 'add' in request.POST:
        product.buy_status = True
        product.save()
        return redirect('index')
    elif 'purchased' in request.POST:
        product.buy_status = False
        product.save()
        return redirect('index')
    elif 'refusal' in request.POST:
        product.buy_status = False
        product.save()
        return redirect('cart')





def registration(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Ошибка регистрации!')
    else:
        form = RegisterUserForm()
    return render(request, 'home/registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли')
            return redirect('index')
    else:
        form = LoginUserForm()
    return render(request, 'home/login.html', {'form': form})


def profile(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')
    return render(request, 'home/profile.html')

# return HttpResponse(f'Страница с номером: {view_comics_id}')


# def delete_comics_from_cart(request, delete_comics_from_cart_id):
#     delete_comics = Comics.objects.get(pk=delete_comics_from_cart_id)
#     delete_comics.buy_status = False
#     delete_comics.save()
#     return redirect('cart')

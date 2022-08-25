from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('comics/', comics, name='comics'),
    path('add_comics/', add_comics, name='add_comics'),
    path('cart/', cart, name='cart')
]

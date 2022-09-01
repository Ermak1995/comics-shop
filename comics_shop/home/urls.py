from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('/<int:view_comics_id>', view_comics, name='view_comics'),
    path('add_comics/', add_comics, name='add_comics'),
    path('add_publisher/', add_publisher, name='add_publisher'),
    path('cart/', cart, name='cart')
]

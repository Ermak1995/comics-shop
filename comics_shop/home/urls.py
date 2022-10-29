from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('/<int:view_comics_id>', view_comics, name='view_comics'),
    path('/readmore/<int:readmore_id>', ReadMore.as_view(), name='readmore'),
    path('add_comics/', add_comics, name='add_comics'),
    path('add_publisher/', add_publisher, name='add_publisher'),
    path('cart/', cart, name='cart'),
    path('registration/', registration, name='registration'),
    path('login/', user_login, name='login'),
    path('profile/', profile, name='profile'),
]

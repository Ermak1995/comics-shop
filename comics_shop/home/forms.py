from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ComicsForm(forms.ModelForm):
    class Meta:
        model = Comics
        fields = '__all__'
        picture = forms.ImageField()

class PublishersForm(forms.ModelForm):
    class Meta:
        model = Publishers
        fields = '__all__'

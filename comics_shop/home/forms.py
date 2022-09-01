from django import forms
from .models import *

class ComicsForm(forms.ModelForm):
    class Meta:
        model = Comics
        fields = '__all__'
        picture = forms.ImageField()

class PublishersForm(forms.ModelForm):
    class Meta:
        model = Publishers
        fields = '__all__'

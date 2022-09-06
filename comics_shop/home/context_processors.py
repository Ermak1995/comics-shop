from .models import *

def extras(request):
    model = Comics.objects.all()
    publishers = Publishers.objects.all()
    return {'model': model, 'publishers': publishers}
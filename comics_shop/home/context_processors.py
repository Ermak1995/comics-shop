from .models import *

def extras(request):
    count = Comics.objects.filter(buy_status=True).count
    model = Comics.objects.all()
    publishers = Publishers.objects.all()
    return {'model': model, 'publishers': publishers, 'count': count}
from django.db import models
from django.urls import reverse


class Comics(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey('Publishers', models.PROTECT)
    picture = models.ImageField()
    price_default = models.FloatField()
    price_now = models.FloatField()
    time_purchase = models.DateTimeField(auto_now=True)
    buy_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Comics'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_comics', kwargs={'view_comics_id': self.pk})



class Publishers(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

# from home.models import *

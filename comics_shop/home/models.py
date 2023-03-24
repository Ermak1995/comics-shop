from django.db import models
from django.urls import reverse
import json


class Comics(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey('Publishers', models.PROTECT)
    description = models.TextField(default='description')
    quantity_purchased = models.IntegerField(default=0)  # Количество покупок
    quantity_pages = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    in_stock = models.IntegerField(default=0)  # В наличии
    picture = models.ImageField()
    price_default = models.FloatField()
    price_now = models.FloatField()
    time_purchase = models.DateTimeField(auto_now=True)
    buy_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Comics'

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return f'/{self.id}'
    def get_absolute_url(self):
        # return f'{self.pk}'
        return reverse('view_comics', kwargs={'view_comics_id': self.pk})


class Publishers(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


# class Comics_from_json(models.Model):
# with open('home/other/comics.json', encoding='utf-8') as file:
#     data = json.load(file)
# print(data)

# from home.models import *
class Comics_from_json(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey('Publishers', models.PROTECT)
    author = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    age_rating = models.CharField(max_length=255)
    description = models.TextField(default='description')
    quantity_pages = models.IntegerField(default=0)
    size = models.CharField(max_length=255)
    cover = models.ImageField()
    price = models.FloatField()
    buy_status = models.BooleanField(default=False)

    # class Meta:
        # verbose_name_plural = 'Comics'

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return f'/{self.id}'
    # def get_absolute_url(self):
    #     # return f'{self.pk}'
    #     return reverse('view_comics', kwargs={'view_comics_id': self.pk})

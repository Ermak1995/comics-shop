from django.db import models


class Comics(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    picture = models.ImageField()
    price_default = models.IntegerField()
    price_now = models.IntegerField()
    buy_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Comics'
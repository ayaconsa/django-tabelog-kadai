from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=20, default='')
    catch_copy = models.CharField(max_length=30, default='')
    explanation = models.CharField(max_length=200, default='')
    price_min = models.PositiveIntegerField(default='0')
    price_max = models.PositiveIntegerField(default='0')
    address = models.CharField(max_length=200, default='')
    tel = models.CharField(max_length=11, default='')
    open_time = models.CharField(max_length=5, default='')
    close_time = models.TimeField(default='')
    close_day = models.TimeField(default='')
    img = models.ImageField(blank=True, default="img/noImage.png")
    
    class Meta:
        app_label = 'NagoyameshiApp'

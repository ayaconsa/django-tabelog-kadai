from django.db import models
from NagoyameshiApp.models.custom_user import CustomUser
from NagoyameshiApp.models.restaurant import Restaurant


class Booking(models.Model):
    TIME = (
        ('10:00'), ('10:30'), ('11:00'), ('11:30'), ('12:00'), ('12:30'), ('13:00'), ('13:30'), ('14:00'), ('14:30'), ('15:00'), ('15:30'), ('16:00'), ('16:30'),('17:00'), ('17:30'), ('18:00'), ('18:30'), ('19:00'), ('19:30'), ('20:00'), ('20:30'),
    )
    

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    date = models.DateTimeField(default='', verbose_name="予約日")
    time = models.TimeField(choices=TIME, default='', verbose_name="予約時間")
    number_of_persons = models.PositiveIntegerField(max_length=2, default='', verbose_name="人数")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    
    class Meta:
        app_label = 'NagoyameshiApp'

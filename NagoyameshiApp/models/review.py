from django.db import models
from NagoyameshiApp.models.user import User
from NagoyameshiApp.models.restaurant import Restaurant


class Review(models.Model):
    RATE = (
        (1), (2), (3), (4), (5),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    rate = models.PositiveIntegerField(choices=RATE, max_length=1, default='', verbose_name="評価")
    comment = models.TextField(max_length=300, default='', verbose_name="コメント")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    
    class Meta:
        app_label = 'NagoyameshiApp'

from django.db import models
from NagoyameshiApp.models.custom_user import CustomUser
from NagoyameshiApp.models.restaurant import Restaurant


class Favorite(models.Model):
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    
    class Meta:
        app_label = 'NagoyameshiApp'

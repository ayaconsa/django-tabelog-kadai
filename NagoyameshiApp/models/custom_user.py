from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    # user = models.OneToOneField(User, on_delete=models.CASCADE)    
    # username = models.CharField(max_length=50, default='', verbose_name="氏名")
    
    furigana = models.CharField(max_length=50, default='', verbose_name="フリガナ")
    birthday = models.DateField(default='', verbose_name="生年月日")
    zipcode = models.CharField(max_length=8, default='', verbose_name="郵便番号")
    address = models.CharField(max_length=100, default='', verbose_name="住所")
    tel = models.CharField(max_length=13, default='', verbose_name="電話番号")
    works = models.CharField(blank=True, max_length=20, default='', verbose_name="ご職業")
    
    subscription = models.BooleanField(default='False', verbose_name="サブスク契約")
    
    # admin = models.BooleanField(default='False', verbose_name="管理者権限")
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")
    # updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    
    def __str__(self):
       # return self.user.username
       return self.username
    
    class Meta:
        app_label = 'NagoyameshiApp'


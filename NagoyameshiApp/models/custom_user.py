from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    username = models.CharField(_('username'), max_length=150, default='')
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=50, default='', verbose_name="氏名")
    furigana = models.CharField(max_length=50, default='', verbose_name="フリガナ")
    birthday = models.DateField(default='2000-01-01', verbose_name="生年月日")
    zipcode = models.CharField(max_length=8, default='', verbose_name="郵便番号")
    address = models.CharField(max_length=100, default='', verbose_name="住所")
    tel = models.CharField(max_length=13, default='', verbose_name="電話番号")
    works = models.CharField(blank=True, max_length=20, default='', verbose_name="ご職業")
    subscription = models.BooleanField(default=False, verbose_name="サブスク契約")
    stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="StripeサブスクリプションID")

    # dummy_user実行時はauto_now_addとauto_nowをFalseにする
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    cancellation_date = models.DateField(null=True, blank=True, verbose_name="退会日")

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('top')
        
    class Meta:
        app_label = 'NagoyameshiApp'
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

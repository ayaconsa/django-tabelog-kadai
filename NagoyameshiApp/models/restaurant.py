from django.db import models
from NagoyameshiApp.models.category import Category
from django.urls import reverse

class Restaurant(models.Model):
    
    name = models.CharField(max_length=100, default='', verbose_name="店舗名")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="カテゴリ")
    price_max = models.PositiveIntegerField(default='0', verbose_name="価格（最大）")
    price_min = models.PositiveIntegerField(default='0', verbose_name="価格（最小）")
    seat = models.PositiveIntegerField(default='0', verbose_name="座席数")
    address = models.CharField(max_length=200, default='', verbose_name="住所")
    tel = models.CharField(max_length=11, default='', verbose_name="電話番号")
    open_time = models.TimeField(default='', verbose_name="営業時間(開始)")
    close_time = models.TimeField(default='', verbose_name="営業時間(終了)")
    close_day = models.CharField(max_length=20, default='', verbose_name="定休日")
    catch_copy = models.CharField(max_length=30, default='', verbose_name="キャッチコピー")
    explanation = models.TextField(max_length=300, default='', verbose_name="説明")
    img = models.ImageField(blank=True, default="img/noImage.png", upload_to='photos', verbose_name="店舗画像")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    
    def get_absolute_url(self):
        return reverse('admin_restaurant_detail', args=[self.pk])
    
    def __str__(self):
        return self.title

    class Meta:
        app_label = 'NagoyameshiApp'

from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100, default='', verbose_name="店舗名")
    category = models.CharField(max_length=20, default='', verbose_name="カテゴリー")
    catch_copy = models.CharField(max_length=30, default='', verbose_name="キャッチコピー")
    explanation = models.CharField(max_length=200, default='', verbose_name="説明文")
    price_min = models.PositiveIntegerField(default='0', verbose_name="価格（最低）")
    price_max = models.PositiveIntegerField(default='0', verbose_name="価格（最大）")
    address = models.CharField(max_length=200, default='', verbose_name="住所")
    tel = models.CharField(max_length=11, default='', verbose_name="電話番号")
    open_time = models.CharField(max_length=5, default='', verbose_name="開店時間")
    close_time = models.TimeField(default='', verbose_name="閉店時間")
    close_day = models.TimeField(default='', verbose_name="定休日")
    img = models.ImageField(blank=True, default="img/noImage.png", verbose_name="イメージ画像")
    
    class Meta:
        app_label = 'NagoyameshiApp'

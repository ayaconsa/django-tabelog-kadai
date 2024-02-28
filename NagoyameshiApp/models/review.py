from django.db import models
from NagoyameshiApp.models.custom_user import CustomUser
from NagoyameshiApp.models.restaurant import Restaurant


class Review(models.Model):
    SCORE = (
        (1, '★'), 
        (2, '★★'), 
        (3, '★★★'), 
        (4, '★★★★'), 
        (5, '★★★★★'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    score = models.PositiveSmallIntegerField(choices=SCORE, default='3', verbose_name="評価")
    comment = models.TextField(blank=False, default='', verbose_name="コメント")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    
    class Meta:
        app_label = 'NagoyameshiApp'
        # 一人のユーザーが同じ店に対して2つ以上のレビューを書けないようにする
        unique_together = ('restaurant', 'user')
        
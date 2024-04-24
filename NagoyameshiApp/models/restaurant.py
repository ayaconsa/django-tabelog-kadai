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

    def get_average(self):
        # 最初に書くとインポートエラーが生じるためこちらに移動
        from NagoyameshiApp.models.review import Review

        # 自レストランidに一致するレビューレコードを取得、平均算出
        reviews = Review.objects.filter(restaurant=self)
        if reviews.exists():
            total_score = sum(review.score for review in reviews)
            average_score = total_score / len(reviews)
            # 平均評価を小数点以下2桁まで丸める
            average_score = round(average_score, 2)
            # タプルで（平均, 件数）を返す
            return (average_score, len(reviews))
        else:
            return (0, 0)
        
    # 評価の高い順の表示のため、評価順のリストをカスタムコマンド実行時に取得するようにする（1日1回とかもできる）    
    @staticmethod
    def get_top_rated_restaurants():
        from NagoyameshiApp.models.review import Review
        return Restaurant.objects.annotate(avg_score=models.Avg('review__score')).order_by('-avg_score')

    def get_favorite_count(self):
        from NagoyameshiApp.models.favorite import Favorite
        # 自店舗に対するお気に入り登録件数を取得
        return self.favorited_by.count()

    def get_booking_data(self):
        from NagoyameshiApp.models.booking import Booking
        # 自店舗に対する予約データを取得
        bookings = Booking.objects.filter(restaurant=self)
        for booking in bookings:
            # 予約に紐づいたユーザー名を取得し、予約データに追加
            booking.user_name = booking.user.name
        return bookings
    
    def get_reviews(self):
        from NagoyameshiApp.models.review import Review
        reviews = Review.objects.filter(restaurant=self)
        for review in reviews:
            # 予約に紐づいたユーザー名を取得し、予約データに追加
            review.user_name = review.user.name
        return reviews
    
    @staticmethod
    def get_latest_restaurants():
        return Restaurant.objects.order_by('-created_at')


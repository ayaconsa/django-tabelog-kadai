from django.core.management.base import BaseCommand
from NagoyameshiApp.models.review import Review
from NagoyameshiApp.models.restaurant import Restaurant
from NagoyameshiApp.models.custom_user import CustomUser
from faker import Faker
import numpy as np
# 四捨五入
from decimal import Decimal, ROUND_HALF_UP

class Command(BaseCommand):
    help = "Creates dummy review data"

    def handle(self, *args, **options):

        # Fakerオブジェクトを作成
        fake = Faker('ja-JP') # 日本語対応

        # レストランとユーザーのクエリセットを取得
        restaurants = Restaurant.objects.all()
        users = CustomUser.objects.all()

        # 各レストランごとにレビューデータを生成
        for restaurant in restaurants:
            for user in users:
                # レビュー数をランダムに設定（平均0.01、標準偏差0.4）
                review_count = int(round(np.random.normal(loc=0.01, scale=0.4)))

                # レビュー数が0以上の場合、レビューを生成
                if review_count > 0:
                    for _ in range(review_count):
                        # 評価データをランダムに生成（平均3.5、標準偏差0.8）
                        u = 3.5
                        s = 0.8
                        x = np.random.normal(u, s)
                        rating_value = 1 if x < 1 else 5 if x > 5 else Decimal(str(x)).quantize(Decimal('0'), ROUND_HALF_UP)

                        # レビュー内容をランダムに生成
                        # レビューコメントの生成をランダムな確立で決定（確率0.5）
                        if np.random.normal() < 0.5:
                            comment = fake.text()
                        else:
                            comment = ''

                        Review.objects.create(
                            restaurant = restaurant, 
                            user = user, 
                            score = rating_value, 
                            comment = comment
                        )

        self.stdout.write(self.style.SUCCESS('Successfully created dummy review data'))
from django.core.management.base import BaseCommand, CommandParser
from NagoyameshiApp.models.review import Review
from NagoyameshiApp.models.restaurant import Restaurant
from NagoyameshiApp.models.custom_user import CustomUser
from faker import Faker
import numpy as np
# 四捨五入
from decimal import Decimal, ROUND_HALF_UP

class Command(BaseCommand):
    help = "Creates dummy review data"

    def add_arguments(self, parser):
        parser.add_argument('--review_mean', type=float, default=0.01, help='Mean value for the number of reviews')
        parser.add_argument('--review_std', type=float, default=0.4, help='Standard deviation for the number of reviews')
        parser.add_argument('--rating_mean', type=float, default=3.5, help='Mean value for the rating score')
        parser.add_argument('--rating_std', type=float, default=0.8, help='Standard deviation for the rating score')
        parser.add_argument('--comment_prob', type=float, default=0.5, help='Probability of generating a comment')

    def handle(self, *args, **options):

        # Fakerオブジェクトを作成
        fake = Faker('ja-JP') # 日本語対応

        # レストランとユーザーのクエリセットを取得
        restaurants = Restaurant.objects.all()
        users = CustomUser.objects.all()

        # 各レストランごとにレビューデータを生成
        for restaurant in restaurants:
            for user in users:
                # レビュー数をランダムに設定（デフォルト値：平均0.01、標準偏差0.4）
                review_count = int(round(np.random.normal(loc=options['review_mean'], scale=options['review_std'])))

                # レビュー数が0以上の場合、レビューを生成
                if review_count > 0:
                    for _ in range(review_count):
                        # 評価データをランダムに生成（デフォルト値：平均3.5、標準偏差0.8）
                        x = np.random.normal(options['rating_mean'], options['rating_std'])
                        rating_value = 1 if x < 1 else 5 if x > 5 else Decimal(str(x)).quantize(Decimal('0'), ROUND_HALF_UP)

                        # レビュー内容をランダムに生成
                        # レビューコメントの生成をランダムな確立で決定（確率のデフォルト値：0.5）
                        if np.random.normal() < options['comment_prob']:
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
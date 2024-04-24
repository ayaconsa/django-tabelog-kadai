from django.core.management.base import BaseCommand
from NagoyameshiApp.models.booking import Booking
from NagoyameshiApp.models.restaurant import Restaurant
from NagoyameshiApp.models.custom_user import CustomUser
from faker import Faker
import numpy as np
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = "Creates dummy booking data"

    def handle(self, *args, **options):

        # Fakerオブジェクトを作成
        fake = Faker('ja-JP') # 日本語対応

        # レストランとユーザーのクエリセットを取得
        restaurants = Restaurant.objects.all()
        users = CustomUser.objects.all()

        for _ in range(100): # 100件のデータを生成
            restaurant = np.random.choice(restaurants)
            user = np.random.choice(users)
            date = fake.date_time_this_year() # 今年の日時をランダム生成
            # 予約時間をランダムに生成
            time = fake.random_element(elements=Booking.TIME_Sorted)[0]
            # 人数を1から10の範囲でランダムに生成
            number_of_persons = np.random.randint(1, 10)

            Booking.objects.create(
                restaurant = restaurant,
                user = user,
                date = date,
                time = time,
                number_of_persons = number_of_persons
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully created dummy booking data'))
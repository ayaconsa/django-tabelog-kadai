from django.core.management.base import BaseCommand
from NagoyameshiApp.models.favorite import Favorite
from NagoyameshiApp.models.restaurant import Restaurant
from NagoyameshiApp.models.custom_user import CustomUser
import random

class Command(BaseCommand):
    help = "Creates dummy favorite data"

    def handle(self, *args, **options):
        restaurants = Restaurant.objects.all()
        users = CustomUser.objects.all()

        for restaurant in restaurants:
            for user in users:
                # ランダムな確立でお気に入り登録を行う
                if random.random() <= 0.06:
                    # すでにお気に入り登録されていない場合のみ新しいお気に入りを追加
                    if not Favorite.objects.filter(user=user, restaurant=restaurant).exists():
                        Favorite.objects.create(user=user, restaurant=restaurant)

        self.stdout.write(self.style.SUCCESS('Successfully created dummy favorite data'))

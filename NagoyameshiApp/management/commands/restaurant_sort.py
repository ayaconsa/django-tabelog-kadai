from django.core.management.base import BaseCommand
from NagoyameshiApp.models.restaurant import Restaurant

class Command(BaseCommand):
    help = "Get average rating and review count for a restaurant, and list top rated restaurants"

    def handle(self, *args, **options):
        # レストランを取得
        restaurant = Restaurant.objects.get(pk=1)
        
        # 平均評価とレビュー件数を取得
        average, review_count = restaurant.get_average()
        self.stdout.write(self.style.SUCCESS(f"平均評価: {average}, レビュー件数: {review_count}"))

        # 評価の高い順のレストランリストを取得
        top_rated_restaurants = Restaurant.get_top_rated_restaurants()
        self.stdout.write(self.style.SUCCESS("評価の高い順のレストランリスト:"))
        for index, restaurant in enumerate(top_rated_restaurants, start=1):
            self.stdout.write(self.style.SUCCESS(f"{index}. {restaurant.name}: {restaurant.avg_score}"))

from typing import Any
from faker import Faker
from django.core.management.base import BaseCommand
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = "テストコマンド"

    def handle(self, *args: Any, **options: Any):

        # Fakerオブジェクトを作成
        fake = Faker('ja-JP') # 日本語対応

        # ランダムな過去の日時から未来の日時までの範囲内で日時を生成
        past_date = datetime.now() - timedelta(days=365) # 1年前の日時
        future_date = datetime.now() # 現在の日時

        print(fake.date_time())
        print(fake.date_time_between(start_date=past_date, end_date=future_date))

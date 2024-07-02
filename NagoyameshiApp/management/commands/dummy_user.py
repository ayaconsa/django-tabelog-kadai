from django.core.management.base import BaseCommand, CommandParser
from NagoyameshiApp.models.custom_user import CustomUser
from faker import Faker
from django.contrib.auth.hashers import make_password
import numpy as np
from datetime import datetime, timedelta
import MeCab
import ipadic

def KanaFromKanji(kanji):
    mecab = MeCab.Tagger(ipadic.MECAB_ARGS)
    kana = ''
    items = mecab.parse(kanji).split('\n')
    
    for item in items:
        words = item.split(',')
        if len(words) == 9:
            kana += words[7] + ' '

    kana = kana[:-1]
    
    return kana

class Command(BaseCommand):
    help = "Creates 100 dummy users"

    def add_arguments(self, parser):
        # サブスク契約の確率。デフォルトは0.3
        parser.add_argument('--subscription_prob', type=float, default=0.3, help='Probability of subscription')
        # 退会する確率。デフォルトは0.2（5人に1人が退会）
        parser.add_argument('--cancellation_prob', type=float, default=0.2, help='Probability of cancellation')
        # 平均退会期間（月）。デフォルトは6ヶ月
        parser.add_argument('--cancellation_timeframe', type=int, default=6, help='Average months to cancellation')

    def handle(self, *args, **options):
        # Fakerオブジェクトの作成
        fake = Faker('ja-JP')  # 日本語対応

        for _ in range(100):  # 100行のダミーデータを生成
            name = fake.name()
            furigana = KanaFromKanji(name)
            email = fake.email()
            birthday = fake.date_of_birth(minimum_age=18, maximum_age=60)
            zipcode = fake.zipcode()
            address = fake.address()
            tel = fake.phone_number()
            works = fake.job()
            password = make_password(fake.password())
            created_at = fake.date_time_between(start_date="-3y", end_date="now")
            updated_at = created_at
            subscription = np.random.choice([True, False], p=[options['subscription_prob'], 1 - options['subscription_prob']])
            
            # 退会日の設定
            cancellation_date = None
            # 退会確率が --cancellation_prob より低い場合に退会日を設定
            if np.random.rand() < options['cancellation_prob']:
                # 退会日はユーザー作成日から --cancellation_timeframe（月）に基づいてランダムに設定
                cancellation_date = created_at + timedelta(days=int(np.random.exponential(scale=options['cancellation_timeframe'] * 30)))

                # 退会日が現在より後になる場合、退会日は現在にする
                if cancellation_date > datetime.now():
                    cancellation_date = datetime.now()
                # 退会したユーザーの subscription を False に設定
                subscription = False

            # ユーザーの作成
            CustomUser.objects.create(
                name=name, 
                furigana=furigana, 
                email=email, 
                birthday=birthday, 
                zipcode=zipcode, 
                address=address, 
                tel=tel, 
                works=works, 
                password=password, 
                created_at=created_at, 
                updated_at=updated_at, 
                subscription=subscription,
                cancellation_date=cancellation_date,
            )
            
        self.stdout.write(self.style.SUCCESS('Successfully created dummy users'))

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
        parser.add_argument('--subscription_prob', type=float, default=0.3, help='Probability of subscription')

    def handle(self, *args, **options):

        # Fakerオブジェクトを作成
        fake = Faker('ja-JP') # 日本語対応

        # ダミーデータを生成してSQLite3データベースに保存
        for _ in range(100):  # 100行のダミーデータを生成
            name = fake.name()
            furigana = KanaFromKanji(name)
            email = fake.email()
            birthday = fake.date_of_birth()
            zipcode = fake.zipcode()
            address = fake.address()
            tel = fake.phone_number()
            works = fake.job()
            password = make_password(fake.password())
            created_at = fake.date_time_between(start_date="-3y", end_date="now")
            updated_at = created_at
            # サブスク契約（確率：デフォルト値0.3）
            subscription = np.random.choice([True, False], p=[options['subscription_prob'], 1 - options['subscription_prob']])

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
                )
            
        self.stdout.write(self.style.SUCCESS('Successfully created dummy users'))




# if __name__=='__main__':
#     print(KanaFromKanji('江上 彩名'))
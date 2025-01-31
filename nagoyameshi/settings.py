from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u&n&ko&(pp)mi%03e!2wov7c(!n$a6^q+=r!dd^*qz88xs%nv^'

# SECURITY WARNING: don't run with debug turned on in production!
if os.path.exists('.is_debug'):
    DEBUG = True
else:
    DEBUG = False
# 開発環境としてMariaDB使う時は
# 「.is_debug（空ファイル）」をmanage.pyと同じところに作る（SQLite時は削除）

# Herokuデプロイのために変更
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_bootstrap5',
    'NagoyameshiApp',
    'storages', # S3を使うために追加
]

AUTH_USER_MODEL = "NagoyameshiApp.CustomUser"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Herokuデプロイのために追加
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nagoyameshi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nagoyameshi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if DEBUG == False:          # 本番環境(Heroku)の場合
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:                       # デバッグ環境(ローカル)の場合
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nagoyameshi',                      # データベース名
            'USER': os.environ['MARIADB_USER'],         # MariaDBのユーザー名
            'PASSWORD': os.environ['MARIADB_PASSWORD'], # パスワード
            'HOST': os.environ['MARIADB_HOST'],         # DBホスト名
            'PORT': os.environ['MARIADB_PORT'],         # DBポート番号
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/



# ==CSSとJSファイルの設定==
# 開発環境（ローカルを参照）
if DEBUG:
    # ブラウザからアクセスする際のURL
    STATIC_URL = '/static/'

    # プロジェクトのアプリで使うstaticファイルを格納している、サーバ内の場所を指定
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "NagoyameshiApp/static")
    ]

    # collectstaticコマンドを実行した際に収集されたstaticファイルを配置する場所の設定）
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 本番環境
else:
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_URL = 'https://aws-egami-test-nagoyameshi.s3.ap-northeast-1.amazonaws.com/'
    # S3にはディレクトリ概念がないため、バケット直下のフォルダを参照している（以下同）

# ==Mediaファイル（投稿画像）の設定（開発環境も本番環境もS3を参照）==
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = 'https://aws-egami-test-nagoyameshi.s3.ap-northeast-1.amazonaws.com/'



# S3の設定
# アクセスキーID
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']

# シークレットアクセスキー
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

# バケット名
AWS_STORAGE_BUCKET_NAME = 'aws-egami-test-nagoyameshi'
# バケットを2つに分けることを試みたが、カスタムストレージバックエンドの設定が必要らしく、後回し（以下ChatGPTより）
    # Djangoでは、デフォルトで静的ファイルとメディアファイルをローカルディスクに保存します。
    # しかし、S3バケットを使用する場合は、Djangoがどのバケットを使用するかを知る必要があります。
    # デフォルトの設定では、静的ファイルとメディアファイルを同じバケットに保存するようにしか設定できません。


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'top'
LOGOUT_REDIRECT_URL = 'top'


# Stripeの設定
STRIPE_SECRET_KEY = os.environ['STRIPE_SECRET_KEY']
STRIPE_PUBLISHABLE_KEY = os.environ['STRIPE_PUBLISHABLE_KEY']
STRIPE_WEBHOOK_SECRET = os.environ.get('STRIPE_WEBHOOK_SECRET')


if not STRIPE_SECRET_KEY:
    raise ValueError("STRIPE_SECRET_KEY is not set in .env_STRIPE file")

if not STRIPE_PUBLISHABLE_KEY:
    raise ValueError("STRIPE_PUBLISHABLE_KEY is not set in .env_STRIPE file")

if not STRIPE_WEBHOOK_SECRET:
    raise ValueError("STRIPE_WEBHOOK_SECRET is not set in .env_STRIPE file")


# 環境ごとのドメイン設定
if DEBUG:
    YOUR_DOMAIN = 'http://127.0.0.1:8000'
else:
    YOUR_DOMAIN = 'https://floating-cliffs-94629-07a3203fd75b.herokuapp.com'


# メール設定
EMAIL_BCKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
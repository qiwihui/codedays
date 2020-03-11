# coding: utf-8
SECRET_KEY = '{SECRET_KEY}'

DEBUG = False

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'NAME': 'codedays',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'codedays',
        'PASSWORD': '{DATABASE_PASSWORD}',
        'HOST': 'codedays-db',
        'PORT': '3306',
    }
}

MAILGUN_API_KEY = "{MAILGUN_API_KEY}"

ANYMAIL = {
    "MAILGUN_API_KEY": '{MAILGUN_API_KEY}',
    "MAILGUN_SENDER_DOMAIN": "mail.codedays.app"
}

ENCRYPT_KEY = b'{ENCRYPT_KEY}'

# redis
BROKER_URL = 'redis://codedays-redis:6379/0'
# store task results in redis
CELERY_RESULT_BACKEND = 'redis://codedays-redis:6379/0'

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
        'NAME': 'codeaday',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'codeaday',
        'PASSWORD': '{DATABASE_PASSWORD}',
        'HOST': 'codeaday-db',
        'PORT': '3306',
    }
}

MAILGUN_API_KEY = "{MAILGUN_API_KEY}"

ANYMAIL = {
    "MAILGUN_API_KEY": '{MAILGUN_API_KEY}',
    "MAILGUN_SENDER_DOMAIN": "mail.qiwihui.com"
}

ENCRYPT_KEY = b'{ENCRYPT_KEY}'

# redis
BROKER_URL = 'redis://codeaday-redis:6379/6'
# store task results in redis
CELERY_RESULT_BACKEND = 'redis://codeaday-redis:6379/6'

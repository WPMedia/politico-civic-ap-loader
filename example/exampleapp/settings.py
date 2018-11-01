import os

import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.getenv("SECRET_KEY", "SECRET")

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "entity",
    "geography",
    "government",
    "election",
    "vote",
    "almanac",
    "raceratings",
    "aploader",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "exampleapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "exampleapp.wsgi.application"


DATABASES = {}
if "DATABASE_URL" in os.environ:
    DATABASES["default"] = dj_database_url.config()
else:
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = "/static/"

#########################
# aploader settings

APLOADER_SECRET_KEY = ""
APLOADER_AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", None)
APLOADER_AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", None)
APLOADER_AWS_REGION = "us-east-1"
# APLOADER_AWS_S3_BUCKET = "interactives.politico.com"
APLOADER_AWS_S3_BUCKET = "staging.interactives.politico.com"
APLOADER_CLOUDFRONT_ALTERNATE_DOMAIN = ""
APLOADER_S3_UPLOAD_ROOT = ""
APLOADER_RESULTS_STATIC_DIR = "static_results"

CIVIC_SLACK_TOKEN = os.getenv("SLACK_TOKEN")
CIVIC_SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CIVIC_TWITTER_CONSUMER_KEY = os.getenv("CIVIC_TWITTER_CONSUMER_KEY")
CIVIC_TWITTER_CONSUMER_SECRET = os.getenv("CIVIC_TWITTER_CONSUMER_SECRET")
CIVIC_TWITTER_ACCESS_TOKEN_KEY = os.getenv("CIVIC_TWITTER_ACCESS_TOKEN_KEY")
CIVIC_TWITTER_ACCESS_TOKEN_SECRET = os.getenv(
    "CIVIC_TWITTER_ACCESS_TOKEN_SECRET"
)

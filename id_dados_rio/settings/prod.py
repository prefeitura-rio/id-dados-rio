# -*- coding: utf-8 -*-
from os import getenv

from .base import *

ALLOWED_HOSTS = [
    getenv("DJANGO_ALLOWED_HOST"),
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    getenv("CORS_ALLOWED_ORIGIN_REGEX"),
]
CORS_ORIGIN_ALLOW_ALL = False
CSRF_COOKIE_DOMAIN = getenv("CSRF_COOKIE_DOMAIN")
CSRF_TRUSTED_ORIGINS = [getenv("CSRF_TRUSTED_ORIGIN")]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": getenv("DB_NAME"),
        "USER": getenv("DB_USER"),
        "PASSWORD": getenv("DB_PASSWORD"),
        "HOST": getenv("DB_HOST"),
        "PORT": getenv("DB_PORT"),
    }
}
DEBUG = False
ADMIN_URL = getenv("ADMIN_URL")
RECAPTCHA_SITE_KEY = getenv("RECAPTCHA_SITE_KEY")
RECAPTCHA_SECRET_KEY = getenv("RECAPTCHA_SECRET_KEY")
SECRET_KEY = getenv("DJANGO_SECRET_KEY")
SESSION_COOKIE_DOMAIN = getenv("SESSION_COOKIE_DOMAIN")

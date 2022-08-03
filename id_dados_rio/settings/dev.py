# -*- coding: utf-8 -*-
from os import getenv

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-)p0jd9&gp=ijfvsn1+!1r=^w!ph&c3o68_j57mh5%j#+nsx3=u"

ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True

RECAPTCHA_SITE_KEY = getenv("RECAPTCHA_SITE_KEY")
RECAPTCHA_SECRET_KEY = getenv("RECAPTCHA_SECRET_KEY")

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

import os
from .base import *

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False #꼭 필요합니다.

ALLOWED_HOSTS = secrets['ALLOWED_HOSTS_DEPLOY']

DATABASES = {
    'default': secrets['DB_SETTINGS']
}

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
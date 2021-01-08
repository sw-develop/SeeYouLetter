import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default' : secrets['LOCAL_SETTINGS']
}


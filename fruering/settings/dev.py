from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from .base import *

SECURE_SSL_REDIRECT = False
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

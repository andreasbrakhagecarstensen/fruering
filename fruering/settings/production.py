from .base import *
import django_heroku

DEBUG = False
SECURE_SSL_REDIRECT = True

django_heroku.settings(locals())

try:
    from .local import *
except ImportError:
    pass

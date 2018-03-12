from .base import *
import django_heroku

DEBUG = False

django_heroku.settings(locals())

try:
    from .local import *
except ImportError:
    pass

from .base import *
import django_heroku

django_heroku.settings(locals(), allowed_hosts=False)

DEBUG = True
ALLOWED_HOSTS = ['fruering-qa.herokuapp.com']

try:
    from .local import *
except ImportError:
    pass

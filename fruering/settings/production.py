from .base import *

DEBUG = False
SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = ['fruering.herokuapp.com', 'fruering.dk']
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_LOCATION = 'production'

try:
    from .local import *
except ImportError:
    pass

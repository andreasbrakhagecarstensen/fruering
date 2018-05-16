from .base import *

DEBUG = False
SECURE_SSL_REDIRECT = True

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

try:
    from .local import *
except ImportError:
    pass

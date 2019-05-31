from .base import *

SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = ['fruering-qa.herokuapp.com']
AWS_LOCATION = 'qa'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
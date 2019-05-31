from .base import *

DEBUG = os.getenv('IS_DEBUG', False)
SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = ['fruering-qa.herokuapp.com']
AWS_LOCATION = 'qa'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

if 'HOST_NAME' not in os.environ:
    HOST_NAME = '{}.herokuapp.com'.format(os.getenv('HEROKU_APP_NAME'))

try:
    from .local import *
except ImportError:
    pass

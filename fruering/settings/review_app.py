from .base import *

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')
HEROKU_PARENT_APP_NAME = os.getenv('HEROKU_PARENT_APP_NAME')
DEBUG = os.getenv('IS_DEBUG', False)
SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = ['{}.herokuapp.com'.format(HEROKU_APP_NAME)]
AWS_LOCATION = 'review_app'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

HOST_NAME = '{}.herokuapp.com'.format(HEROKU_APP_NAME)
BASE_URL = 'https://{}/'.format(HOST_NAME)

try:
    from .local import *
except ImportError:
    pass

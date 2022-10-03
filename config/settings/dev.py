from config.settings.base import *

DEBUG = True

INTERNAL_IPS = ('127.0.0.1')


STATIC_URL = f"https://ddshs.s3.ap-northeast-2.amazonaws.com/static"
STATICFILES_STORAGE = "utils.storages.StaticRootS3Boto3Storage"

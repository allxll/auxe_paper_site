
from .base import *

DEBUG = False
STATIC_ROOT = '/var/www/paper.axue.de/static'
MEDIA_ROOT = '/var/www/paper.axue.de/media'
ALLOWED_HOSTS = [ 'paper.axue.de', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf',
        },
    }
}
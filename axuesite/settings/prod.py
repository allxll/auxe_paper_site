from axuesite.settings.base import *

DEBUG = False
STATIC_URL = '/var/www/paper.axue.de/static'
MEDIA_ROOT = BASE_DIR.joinpath('/var/www/paper.axue.de/media')
ALLOWED_HOSTS = [ 'paper.axue.de' ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'axuesite',
        'USER': 'axue',
        'PASSWORD': 'xuwowuyou1',
    }
}
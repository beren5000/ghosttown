from settings import *

TEMPLATE_DIRS = (
    '/home/beren5000/webapps/ghosttown/ghosttown/imagemap/templates/',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/home/beren5000/webapps/ghosttown/ghosttown/imagemap/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = '/home/beren5000/webapps/ghosttown_media'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = 'http://www.republicadelosfantasmas.co/media/'
# END MEDIA CONFIGURATION

STATIC_ROOT = '/home/beren5000/webapps/ghosttown_static'
STATIC_URL = 'http://www.republicadelosfantasmas.co/static/'

DEBUG = False
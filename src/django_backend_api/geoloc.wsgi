import os
from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.django_backend_api.django_backend_api.settings')
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
"""
WSGI config for django-test-04 project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-test-04.settings')

application = get_wsgi_application()

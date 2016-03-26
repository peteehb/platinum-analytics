"""
WSGI config for pnmdb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
import sys
import os

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/opt/platinum/db')
sys.path.insert(1, '/opt/platinum/db/pnmdb')

os.environ["DJANGO_SETTINGS_MODULE"] = "pnmdb.settings"

application = get_wsgi_application()

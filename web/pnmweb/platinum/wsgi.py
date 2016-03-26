"""
WSGI config for platinum project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/opt/platinum/web/pnmweb')
sys.path.insert(1, '/opt/platinum/web/pnmweb/platinum')

os.environ["DJANGO_SETTINGS_MODULE"] = "platinum.settings"

application = get_wsgi_application()

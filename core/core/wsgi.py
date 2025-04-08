"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
>>>>>>> 508fb6559e942b3801c1fb4cc9f5ed312879794c
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

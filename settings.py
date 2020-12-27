import os
import django_heroku

# Build paths for Heroku
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Activate Django-Heroku.
django_heroku.settings(locals())
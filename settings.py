import os
import django_heroku

# Build paths for Heroku
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Activate Django-Heroku.
django_heroku.settings(locals())
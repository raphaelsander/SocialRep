#!/bin/bash

# Collect static files
# Reference: https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/
# echo "Collect static files"
# python manage.py collectstatic --noinput

# Apply database migrations
# Reference: https://docs.djangoproject.com/en/3.2/topics/migrations/
echo "Apply database migrations"
python manage.py migrate

# Start server
# Reference: https://docs.djangoproject.com/en/3.2/ref/django-admin/#runserver
echo "Starting server"
python manage.py runserver 0.0.0.0:8000 --noreload

#!/bin/bash
python manage.py makemigrations
python manage.py migrate --noinput
python manage.py createsuperuser
python manage.py collectstatic --no-input
gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000
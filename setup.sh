#!/bin/bash

read -p "username: " username

# Setup environment
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=$(which python3)
source $(which virtualenvwrapper.sh)

mkvirtualenv portfolio-venv --python=python3.12
pip install -r requirements.txt
python manage.py collectstatic

echo "SECRET_KEY='$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')'" > .env
echo "DEBUG='False'" >> .env

cd portfolio
echo "ALLOWED_HOSTS += ['${username}.pythonanywhere.com']" >> settings.py
echo "CSRF_TRUSTED_ORIGINS += ['https://${username}.pythonanywhere.com']" >> settings.py

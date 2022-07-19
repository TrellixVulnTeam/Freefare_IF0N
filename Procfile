pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

release: python Sal_django_site/manage.py migrate
web: gunicorn Sal_website.wsgi --log file--

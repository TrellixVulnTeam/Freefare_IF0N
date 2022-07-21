release: python Sal_django_site/manage.py migrate
release: pip install -r requirements.txt
web: gunicorn --chdir Sal_django_site Sal_website.wsgi --log file--

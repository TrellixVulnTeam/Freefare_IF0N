release: python Sal_django_site/manage.py migrate
web: gunicorn --chdir Sal_django_site Sal_website.wsgi --log file--

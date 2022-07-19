pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
cd Sal_django_site/env/bin source activate

release: python Sal_django_site/manage.py migrate
web: gunicorn Sal_website.wsgi --log file--

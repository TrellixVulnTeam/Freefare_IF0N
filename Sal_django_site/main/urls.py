"""Sal_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.urls import path, include
from django.conf.urls import url, include
from . import views
from django.contrib import admin
from .tokens import user_tokenizer

# from django.contrib.auth import views as auth_views

app_name = 'main'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("contact", views.contact, name="contact"),
    path("signup", views.signup, name="signup"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("account_activation_sent", views.account_activation_sent, name='account_activation_sent'),
    path("email-test", views.email_test, name="email-test"),
    path('confirm-email', views.account_activation_sent, name='confirm_email_sent'),


    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
    # path('activate/<uidb64>/<token>/', views.activate, name='activate')
    # path('activate', views.activate, name='activate'),
    # path("activate/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})",
    #     views.activate, name="activate"),

]

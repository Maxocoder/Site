from django.contrib import admin
from django.conf.urls import url, include
from car_shop.views import *

urlpatterns = [
    url(r'home/$', main, name='main'),
    url(r'home/registration', registration, name='registration'),
]

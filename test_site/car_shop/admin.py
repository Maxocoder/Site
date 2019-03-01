from django.contrib import admin
from car_shop.models import *
from datetime import datetime


class AdminSuccess(admin.ModelAdmin):
    date_hierarchy = 'date'

    fields = ('lastname', 'firstname', 'reporting', 'email', 'auto', 'profi', 'date')


admin.site.register(BaseRegister, AdminSuccess)

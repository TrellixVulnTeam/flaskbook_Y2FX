#login/admin.py
from django.contrib import admin
from . import models

admin.site.register(models.User)


# Register your models here.

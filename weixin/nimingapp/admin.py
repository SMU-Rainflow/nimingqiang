from django.contrib import admin

# Register your models here.

from nimingapp import models

admin.site.register(models.Message)

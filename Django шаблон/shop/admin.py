from django.contrib import admin
from shop import models

# Register your models here.
admin.site.register(models.Shop)
admin.site.register(models.Category)
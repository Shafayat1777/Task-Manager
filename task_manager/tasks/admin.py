from django.contrib import admin

# Register your models here.

from .models import Task, Image

admin.site.register(Task)
admin.site.register(Image)
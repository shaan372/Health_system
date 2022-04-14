from django.contrib import admin
from mainapp.models import Readings


# Register your models here.

class Adminprod(admin.ModelAdmin):
    list_display = ['temp', 'pulse', 'date', 'time']

admin.site.register(Readings, Adminprod)

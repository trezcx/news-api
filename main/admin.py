from django.contrib import admin
from .models import News, Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name']
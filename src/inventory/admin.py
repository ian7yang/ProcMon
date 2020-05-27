from django.contrib import admin
from .models import Website, Crawler

from django.contrib.admin import AdminSite

AdminSite.site_header = 'ProcMon Console'
AdminSite.site_title = 'ProcMon'


@admin.register(Crawler)
class CrawlerAdmin(admin.ModelAdmin):
    list_display = ('name', 'hostname', 'is_active')


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('url', 'is_active')

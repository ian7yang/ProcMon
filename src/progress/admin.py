from django.contrib import admin
from .models import CrawlingRecord


@admin.register(CrawlingRecord)
class CrawlingRecordAdmin(admin.ModelAdmin):
    list_display = (
        'website', 'user', 'created_at', 'created_by', 'is_complete',
        'is_successful', 'is_loaded')

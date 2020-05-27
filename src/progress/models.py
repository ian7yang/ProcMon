from django.db import models
from src.inventory.models import Website, Crawler


class CrawlingRecord(models.Model):
    website = models.ForeignKey(Website, related_name='website',
                                on_delete=models.SET_NULL, null=True)
    user = models.CharField(max_length=50)
    file_path = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Crawler, related_name='crawler',
                                   on_delete=models.SET_NULL, null=True)
    complete_at = models.DateTimeField(auto_now_add=False, auto_now=False,
                                       null=True, blank=True)
    is_successful = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    is_loaded = models.BooleanField(default=False)

    def __str__(self):
        return self.website.url

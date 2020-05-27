from django.db import models
from inventory.models import Website, Crawler


class CrawlingRecord(models.Model):
    website = models.ForeignKey(Website, related_name='website',
                                on_delete=models.SET_NULL, null=True)
    user = models.CharField(max_length=50, blank=True)
    file_path = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    created_by = models.ForeignKey(Crawler, related_name='crawler',
                                   on_delete=models.SET_NULL, null=True,
                                   blank=True)
    complete_at = models.DateTimeField(auto_now_add=False, auto_now=False,
                                       null=True, blank=True)
    is_successful = models.BooleanField(default=False, blank=True)
    is_complete = models.BooleanField(default=False, blank=True)
    is_loaded = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.website.url

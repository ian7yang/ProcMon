from django.db import models
from inventory.models import Website, Crawler


class CrawlingRecord(models.Model):
    website = models.ForeignKey(Website, related_name='website',
                                on_delete=models.SET_NULL, null=True)
    user = models.CharField(max_length=50)
    file_path = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Crawler, related_name='crawler',
                                   on_delete=models.SET_NULL, null=True)
    complete_at = models.DateTimeField(auto_now_add=False, auto_now=False,
                                       null=True)
    is_successful = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    is_loaded = models.BooleanField(default=False)

    def __str__(self):
        return self.website.url


class Dashboard(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=0)
    created_at = models.DateTimeField()
    website = models.CharField(max_length=100)
    loaded = models.IntegerField()
    successful = models.IntegerField()
    completed = models.IntegerField()
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'dashboard'
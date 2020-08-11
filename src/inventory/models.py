from django.db import models
from django.db.models import Sum, IntegerField

# Create your models here.
class Website(models.Model):
    url = models.URLField(primary_key=True)
    is_active = models.BooleanField(default=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    is_alexa = models.BooleanField(default=False)

    def __str__(self):
        return self.url


class Crawler(models.Model):
    name = models.CharField(max_length=50, primary_key=True)  # hostname-number
    hostname = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    # @property
    def get_current_info(self):
        instances = self.crawler.filter(is_complete=False).order_by('-created_at')
        ret = {'msg': '', 'status': 'running'}
        if len(instances) > 1:
            ret['msg'] = 'More than one running instance'
        elif len(instances) == 0:
            ret['status'] = 'idle' if self.is_active else 'down'
            return ret
        instance = instances[0]
        ret['url'] = instance.website.url
        ret['started_at'] = instance.created_at
        return ret

    def get_stat_info(self):
        return self.crawler.values('created_by').annotate(
            completed=Sum('is_complete', output_field=IntegerField()),
            successful=Sum('is_successful', output_field=IntegerField()),
            loaded=Sum('is_loaded', output_field=IntegerField()))

    def get_history(self):
        return self.crawler.filter(created_by=self).order_by('-created_at')
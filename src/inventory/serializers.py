from .models import Website, Crawler
from rest_framework import serializers


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = '__all__'


class CrawlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crawler
        fields = '__all__'

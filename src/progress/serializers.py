from .models import Crawler, CrawlingRecord
from rest_framework import serializers


class CrawlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crawler
        fields = '__all__'


class CrawlingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrawlingRecord
        fields = '__all__'

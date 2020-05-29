from .models import CrawlingRecord
from rest_framework import serializers


class CrawlingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrawlingRecord
        fields = '__all__'

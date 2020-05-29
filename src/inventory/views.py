from .serializers import WebsiteSerializer, CrawlerSerializer
from .models import Website, Crawler

from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404


class CrawlerViewSet(viewsets.ModelViewSet):
    queryset = Crawler.objects.all()
    serializer_class = CrawlerSerializer
    filterset_fields = '__all__'


class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    filterset_fields = '__all__'

    def retrieve(self, request, *args, **kwargs):
        website = get_object_or_404(Website, url=request.GET['pk'])
        serializer = WebsiteSerializer(website)
        return Response(serializer.data)

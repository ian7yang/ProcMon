from .serializers import CrawlingRecordSerializer
from .models import CrawlingRecord
from inventory.models import Website, Crawler

from rest_framework import viewsets, status
from rest_framework.response import Response

from django.db.models import Sum, IntegerField
from django.shortcuts import render, get_object_or_404


# Create your views here.
class CrawlingRecordViewSet(viewsets.ModelViewSet):
    queryset = CrawlingRecord.objects.all()
    serializer_class = CrawlingRecordSerializer
    filterset_fields = '__all__'

    def create(self, request, *args, **kwargs):
        data = request.data
        website = data['website']
        Website.objects.get_or_create(url=website)
        crawler = data['created_by']
        hostname = crawler.split('-')[0]
        c, created = Crawler.objects.get_or_create(name=crawler)
        if created:
            c.hostname = hostname
        c.is_active = True
        c.save()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


def index(request):
    crawlers = Crawler.objects.all().prefetch_related('crawler')
    stats = CrawlingRecord.objects.values(
        'created_by').annotate(
        completed=Sum('is_complete', output_field=IntegerField()),
        successful=Sum('is_successful', output_field=IntegerField()),
        loaded=Sum('is_loaded', output_field=IntegerField()))

    context = {
        'stats': stats,
        'crawlers': crawlers
    }
    return render(request, 'index.html', context=context)


def detail(request, name):
    crawler = get_object_or_404(Crawler, name=name)
    context = {
        'crawler': crawler
    }
    return render(request, 'detail.html', context=context)

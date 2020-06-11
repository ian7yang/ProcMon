from .serializers import CrawlingRecordSerializer
from .models import CrawlingRecord, Dashboard
from inventory.models import Website, Crawler

from rest_framework import viewsets, status
from rest_framework.response import Response

from django.db.models import Sum, IntegerField
from django.shortcuts import render
from django.db import connection
from django.core.paginator import Paginator

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
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
    # crawlers = Crawler.objects.all().prefetch_related('crawler')
    # stats = CrawlingRecord.objects.values(
    #     'created_by').annotate(
    #     completed=Sum('is_complete', output_field=IntegerField()),
    #     successful=Sum('is_successful', output_field=IntegerField()),
    #     loaded=Sum('is_loaded', output_field=IntegerField()))
    tiles = Dashboard.objects.all()
    overall_stat = CrawlingRecord.objects.values('is_complete').annotate(
        completed=Sum('is_complete', output_field=IntegerField()),
        successful=Sum('is_successful', output_field=IntegerField()),
        loaded=Sum('is_loaded', output_field=IntegerField()))
    context = {
        'tiles': tiles,
        'overall_stat': overall_stat[0],
    }
    return render(request, 'index.html', context=context)


def detail(request, name):
    # records = get_list_or_404(CrawlingRecord, created_by_id=name)
    records = CrawlingRecord.objects.filter(created_by_id=name).order_by('-created_at')
    paginator = Paginator(records, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'detail.html', context=context)

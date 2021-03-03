import os
import re

from django.conf import settings
from django.http import StreamingHttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from reports.models import Reports
from reports.serializer import ReportsModelSerializer
from reports.utils import format_output, get_file_contents


class ReportsViewSet(ModelViewSet):
    """
    list:
    获取报告列表数据

    create:
    创建报告

    destroy:
    删除报告

    update:
    完整更新报告

    partial_update:
    部分更新报告

    retrieve:
    获取报告详情数据

    """
    queryset = Reports.objects.filter(is_delete=False)
    serializer_class = ReportsModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ('id', 'name')

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['results'] = format_output(response.data['results'])
        return response

    @action(detail=True)
    def download(self, request, pf=None):
        instance = self.get_object()
        html = instance.html
        name = instance.name
        mtch = re.match(r'(.*_)\d+', name)
        if mtch:
            mtch = mtch.group(1)

        report_dir = os.path.join(settings.BASE_DIR,'reports')
        report_path = os.path.join(report_dir, mtch)
        response = StreamingHttpResponse(get_file_contents(report_path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachmen; filename*=UTF-8" "{}'.format(name)
        return response
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from envs.models import Envs
from envs.serializer import EnvsModelSerializer


class EnvsViewSet(viewsets.ModelViewSet):
    """
    list:
    获取接口列表数据

    create:
    创建接口

    destroy:
    删除接口

    update:
    完整更新接口

    partial_update:
    部分更新接口

    retrieve:
    获取接口详情数据

    names:
    获取所有接口ID和接口名


    """
    queryset = Envs.objects.filter(is_delete=False)
    serializer_class = EnvsModelSerializer
    filter_fields = ['id', 'name', 'tester']
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()  # 逻辑删除
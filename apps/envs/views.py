from django.core.serializers import get_serializer
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from envs.models import Envs
from envs.serializer import EnvsModelSerializer, EnvsNameSerializer
from envs.utils import handle_env


class EnvsViewSet(viewsets.ModelViewSet):
    """
    list:
    获取环境变量列表数据

    create:
    创建环境变量

    destroy:
    删除环境变量

    update:
    完整更新环境变量

    partial_update:
    部分更新环境变量

    retrieve:
    获取环境变量详情数据

    names:
    获取所有环境变量ID和接口名

    """
    queryset = Envs.objects.filter(is_delete=False)
    serializer_class = EnvsModelSerializer
    filter_fields = ['id', 'name']
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ('id', 'name')
    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()  # 逻辑删除

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response['results'] = handle_env(response.data['results'])
        return response

    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = EnvsNameSerializer(instance=queryset, many=True)
        # serializer = get_serializer(instance=queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'names':
            return EnvsNameSerializer
        else:
            return EnvsModelSerializer
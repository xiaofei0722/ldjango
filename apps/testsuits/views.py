from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from testsuits.models import Testsuits
from testsuits.serializer import TestSuitsModelSerializer, TestSuitsNameSerializer
from testsuits.utils import handle_testsuit


class TestSuitsViewSet(viewsets.ModelViewSet):
    """
    list:
    获取套件列表数据

    create:
    创建套件

    destroy:
    删除套件

    update:
    完整更新套件

    partial_update:
    部分更新套件

    retrieve:
    获取套件详情数据

    names:
    获取所有套件ID和接口名


    """
    queryset = Testsuits.objects.filter(is_delete=False)
    serializer_class = TestSuitsModelSerializer
    filter_fields = ['id', 'name']
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()  # 逻辑删除

    def list(self, request, *args, **kwargs):
        #过滤查询集的创建
        # queryset = self.filter_queryset(self.get_queryset())
        # #分页查询集的创建
        # page = self.paginate_queryset(queryset)
        # #如果要分页就把分页信息以及分页后处理的逻辑返回
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     datas = serializer.data
        #     datas = get_count_by_interface(datas)
        #     return self.get_paginated_response(datas)
        # #如果不分页就直接返回查询集信息
        # serializer = self.get_serializer(queryset, many=True)
        # datas = serializer.data
        # datas = get_count_by_interface(datas)
        # return Response(datas)
        response = super().list(request,*args,**kwargs)
        response.data['results'] = handle_testsuit(response.data['results'])
        return response

    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TestSuitsNameSerializer(instance=queryset, many=True)
        return Response(serializer.data)
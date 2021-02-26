from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework import mixins, permissions
from rest_framework.response import Response

from interfaces.models import Interfaces
from configures.models import Configures
from testcases.models import Testcases
from interfaces.serializer import InterfacesModelSerializer, InterfacesNameSerializer
from rest_framework import viewsets

#
# class InterfaceList(mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    GenericAPIView):
#     # 指定查询集
#     queryset = Interfaces.objects.all()
#     # 指定需要使用到的序列化器类
#     serializer_class = InterfaceModelSerializer
#     #在视图类中制定过滤引擎
#     # filter_backends = [filters.OrderingFilter]
#     #制定需要排序的字段
#     ordering_fields = ['id']
#     #制定类视图中制定过滤引擎
#     # filter_backends = [DjangoFilterBackend]
#     #制定需要过滤的字段
#     filterset_fields = ['name','project_id','tester']
#     #在某个视图中制定分页类
#     # pagination_class = PageNumberPaginationManual
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#
# class InterfaceDetail(mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      GenericAPIView):
#     queryset = Interfaces.objects.all()
#     serializer_class = InterfaceModelSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
#
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
#
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)
from interfaces.utils import get_count_by_interface


class InterfacesViewSet(viewsets.ModelViewSet):
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
    queryset = Interfaces.objects.filter(is_delete=False)
    serializer_class = InterfacesModelSerializer
    filter_fields = ['id', 'name', 'tester']
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()  # 逻辑删除

    def list(self, request, *args, **kwargs):
        #过滤查询集的创建
        queryset = self.filter_queryset(self.get_queryset())
        #分页查询集的创建
        page = self.paginate_queryset(queryset)
        #如果要分页就把分页信息以及分页后处理的逻辑返回
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            datas = serializer.data
            datas = get_count_by_interface(datas)
            return self.get_paginated_response(datas)
        #如果不分页就直接返回查询集信息
        serializer = self.get_serializer(queryset, many=True)
        datas = serializer.data
        datas = get_count_by_interface(datas)
        return Response(datas)

    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = InterfacesNameSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path='configures')
    def configures(self, request, pk=None):
        configure_objs = Configures.objects.filter(interface_id=pk, is_delete=False)
        one_list = []
        for obj in configure_objs:
            one_list.append({
                'id': obj.id,
                'name': obj.name
            })
        return Response(data=one_list)

    @action(methods=['get'], detail=False)
    def testcases(self, request, pk=None):
        testcase_objs = Testcases.objects.filter(interface_id=pk, is_delete=False)
        one_list = []
        for obj in testcase_objs:
            one_list.append({
                'id': obj.id,
                'name': obj.name
            })
        return Response(data=one_list)


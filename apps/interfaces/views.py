from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from interfaces.models import Interface
from interfaces.serializer import InterfaceModelSerializer


class InterfaceList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   GenericAPIView):
    # 指定查询集
    queryset = Interface.objects.all()
    # 指定需要使用到的序列化器类
    serializer_class = InterfaceModelSerializer
    #在视图类中制定过滤引擎
    # filter_backends = [filters.OrderingFilter]
    #制定需要排序的字段
    ordering_fields = ['id']
    #制定类视图中制定过滤引擎
    # filter_backends = [DjangoFilterBackend]
    #制定需要过滤的字段
    filterset_fields = ['name','project_id','tester']
    #在某个视图中制定分页类
    # pagination_class = PageNumberPaginationManual

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class InterfaceDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericAPIView):
    queryset = Interface.objects.all()
    serializer_class = InterfaceModelSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


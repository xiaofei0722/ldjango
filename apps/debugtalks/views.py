from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from debugtalks.models import Debugtalks
from debugtalks.serializer import DebugtalksModelSerializer

class DebugTalksViewSet(mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
    '''
    list:
    返回debugtalk（多个）列表数据

    update:
    更新（全）debugtalk

    partial_update:
    更新（部分）debugtalk
    '''
    queryset = Debugtalks.objects.filter(is_delete=False)
    serializer_class = DebugtalksModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ('id', 'project_id')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data_dict = {
            'id': instance.id,
            'debugtalk': instance.debugtalk
        }
        return Response(data_dict)
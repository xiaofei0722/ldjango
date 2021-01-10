from rest_framework import serializers
from interfaces.models import Interface
class InterfaceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface
        fields = "__all__"


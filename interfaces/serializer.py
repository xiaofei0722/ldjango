from rest_framework import serializers
from interfaces.models import Interface
class InterfaceModelSerializer(serializers.ModelSerializer):
    # project = serializers.StringRelatedField(slug_field='tester',queryset=)
    class Meta:
        model = Interface
        fields = "__all__"


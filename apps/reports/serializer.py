from datetime import datetime

from rest_framework import serializers
from interfaces.models import Interfaces
from projects.models import Projects
from reports.models import Reports
from testsuits.models import Testsuits


class ReportsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testsuits
        # fields = ('id','name','project','project_id','create_time','update_time','include')
        exclude = ('update_time', 'is_delete')
        extra_kwarge = {
            'create_time': {
                "read_only": True
            },
            'html': {
                'read_noly': True
            }
        }

    def create(self, validated_data):
        report_name = validated_data['name']
        validated_data['name'] = report_name + '_' + datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        report = Reports.objects.create(**validated_data)
        return report


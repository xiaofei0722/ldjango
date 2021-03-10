import re
from django.db.models import Count

from interfaces.models import Interfaces
from testcases.models import Testcases
from testsuits.models import Testsuits

def handle_testsuit(datas):
    datas_list = []
    for item in datas:
        mtch = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        item['create_time'] = mtch.group(1)+' '+mtch.group(2)
        mtcht = re.search(r'(.*)T(.*)\..*?', item['update_time'])
        item['update_time'] = mtcht.group(1) + ' ' + mtcht.group(2)

        # project_id = item['id']
        #
        #
        #
        #
        #
        #
        #
        # # Interfaces.objects.filter(project_id=project_id, is_delete=False)
        # #testcases表示model的模型类名称的全小写
        # # 计算用例数量
        # interfaces_testcases_objs = Interfaces.objects.values('id').annotate(testcases = Count('testcases')).filter(project_id=project_id, is_delete=False)
        #
        # # interfaces_count = interfaces_testcases_objs.count()
        #
        # testcases_count = 0
        # for one_dict in interfaces_testcases_objs:
        #     testcases_count += one_dict['testcases']
        # # 计算配置数量
        # interfaces_configures_objs = Interfaces.objects.values('id').annotate(configures=Count('configures')).filter(
        #     project_id=project_id, is_delete=False)
        # configures_count = 0
        # for one_dict in interfaces_configures_objs:
        #     configures_count += one_dict['configures']
        # # 计算套件数量
        # testsuits_count = Testsuits.objects.filter(project_id=project_id, is_delete=False).count()
        #
        # # item['interfaces'] = interfaces_count
        # item['testsuits'] = testsuits_count
        # item['testcases'] = testcases_count
        # item['configures'] = configures_count
        datas_list.append(item)
    return datas_list

def get_testcases_by_interface_ids(ids_list):
    one_list = []
    for interface_id in ids_list:
        testcases_qs = Testcases.objects.values_list('id', flat=True).filter(interface_id=interface_id, is_delete=False)
        one_list.extend(list(testcases_qs))
    return one_list



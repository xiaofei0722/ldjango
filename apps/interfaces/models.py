from django.db import models

# Create your models here.
from projects.models import Projects
from utils.base_models import BaseModel


class Interfaces(BaseModel):
	"""
	创建Interfaces模型类
	一个项目有多个接口，一个接口往往属于一个项目，项目和接口关系：一对多
	需要在多的一侧，去创建外键
	"""
	id = models.AutoField('id主键', primary_key=True, help_text='id主键')
	name = models.CharField('接口名称', unique=True, max_length=200, help_text='接口名称')
	# 创建外键
	# on_delete 设置：当父表（项目表）中的数据删掉之后，从表该字段的处理方式
	# models.CASCADE 子表也会自动删除
	# models.SET_NULL 子表自动设置为Null
	# related_name 设置父表对子表引用名，如不指定，默认为子表模型类名小写_set(interfaces_set)
	project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE,
	                            related_name='interfaces', help_text='所属项目')
	tester = models.CharField(verbose_name='测试人员', max_length=50, help_text='测试人员')
	desc = models.CharField('简要描述', max_length=200, default='', blank=True,
	                        null=True, help_text='简要描述')

	class Meta:
		db_table = "tb_interfaces"
		verbose_name = "接口信息"
		verbose_name_plural = verbose_name


	def __str__(self):
		return self.name
from django.db import models

# Create your models here.
class Interface(models.Model):
    class Projects(models.Model):
        name = models.CharField(verbose_name='接口名称', max_length=200, unique=True, help_text='接口名称')
        tester = models.CharField(verbose_name='测试人员', max_length=50, help_text='测试人员')
        desc = models.TextField(verbose_name='简要描述', help_text='简要描述', blank=True, default='简要描述')
        project = models.ForeignKey('projects.Projects',on_delete=models.CASCADE,verbose_name='所属项目',help_text='所属项目')

        class Meta:
            db_table = 'tb_projects'

            verbose_name = '项目'
            verbose_name_plural = '项目'
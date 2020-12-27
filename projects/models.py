from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Projects(models.Model):
    name = models.CharField(max_length=200,verbose_name='项目名称',unique=True,help_text='')
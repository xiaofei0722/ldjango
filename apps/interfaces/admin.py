from django.contrib import admin
from interfaces.models import Interfaces
# Register your models here.

class InterfaceAdmin(admin.ModelAdmin):
    fields = ('name','tester','project')
    list_display = ['name',"tester"]


admin.site.register(Interfaces,InterfaceAdmin)
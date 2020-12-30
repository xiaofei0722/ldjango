from django.contrib import admin
from interfaces.models import Interface
# Register your models here.

class InterfaceAdmin(admin.ModelAdmin):
    fields = ('name','tester','project')
    list_display = ['name',"tester"]


admin.site.register(Interface,InterfaceAdmin)
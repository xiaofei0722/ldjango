from django.contrib import admin
from projects.models import Projects,Person
# Register your models here.

class PreojectsAdmin(admin.ModelAdmin):
    fields = ('name','leader','tester','programer','publish_app')

    list_display = ['id','name','leader','tester']

admin.site.register(Projects,PreojectsAdmin)
admin.site.register(Person)
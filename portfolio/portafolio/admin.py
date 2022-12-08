from django.contrib import admin
from .models import Project

# Register your models here.
#necesario para poder ver los campos ocultos 'created' y 'updated'
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)
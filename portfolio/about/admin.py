from django.contrib import admin
from .models import Course, Skill

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    

admin.site.register([Course, Skill], AboutAdmin)
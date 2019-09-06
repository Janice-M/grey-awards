from django.contrib import admin
from .models import Project, Tags
# Register your models here.

Class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal=('tags')
    
    
admin.site.register(Project,ProjectAdmin)
admin.site.register(Tags)
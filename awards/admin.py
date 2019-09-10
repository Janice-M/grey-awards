from django.contrib import admin
from .models import Project,Profile,Rating


    # filter_horizontal =('technologies','categories','colors')


# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Rating)

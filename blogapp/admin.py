from django.contrib import admin
from .models import profile
# Register your models here.
class profile_admin(admin.ModelAdmin):
    model=profile
    fields=['user','image','location','bio']
    list_display=['location',]
admin.site.register(profile,profile_admin)

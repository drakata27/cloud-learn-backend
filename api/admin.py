from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display=['username', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_editable=['verified']
    list_display=['user','full_name', 'verified']

# Register your models here.
admin.site.register(Section)
admin.site.register(Topic)
admin.site.register(Subtopic)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
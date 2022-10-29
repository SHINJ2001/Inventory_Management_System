from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser, UserModel)
admin.site.register(tools)
admin.site.register(parts)
admin.site.register(Operations)
admin.site.register(manufacturers)
admin.site.register(requirement)
admin.site.register(rejections)
admin.site.register(completed_processes)
admin.site.register(targets)
admin.site.register(Managers)
admin.site.register(Staff)
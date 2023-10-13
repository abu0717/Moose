from django.contrib import admin
from .models import UserModel, PostModel

# Register your models here.

# admin.site.register(UserModel)
admin.site.register(PostModel)


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", 'last_name']
    list_filter = ["first_name"]

from django.contrib import admin
from PaginationApp.models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    list_display=('user_name','user_designation','user_description')

admin.site.register(UserInfo,UserInfoAdmin)

# Register your models here.

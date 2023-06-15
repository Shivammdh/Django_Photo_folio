from django.contrib import admin
from news.models import MyNews

# Register your models here.
class MyNewsAdmin(admin.ModelAdmin):
    list_display=('news_title','news_description')

admin.site.register(MyNews,MyNewsAdmin)
from django.contrib import admin
from .models import Contact
from .models import Profession
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')

class ProfessionAdmin(admin.ModelAdmin):
    list_display=('desg','detail')


admin.site.register(Contact,ContactAdmin)
admin.site.register(Profession,ProfessionAdmin)


from django.contrib import admin

# Register your models here.
from web.models import Diary, Month

admin.site.register(Diary)
admin.site.register(Month)
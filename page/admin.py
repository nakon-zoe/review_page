from django.contrib import admin
from .models import Bakery_Info, Bakery_Location, Bakery_Review

# Register your models here.
admin.site.register(Bakery_Info)
admin.site.register(Bakery_Location)
admin.site.register(Bakery_Review)
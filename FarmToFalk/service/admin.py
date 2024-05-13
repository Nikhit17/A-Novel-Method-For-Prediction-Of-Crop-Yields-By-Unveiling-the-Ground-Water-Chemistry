from django.contrib import admin
from service.models import *



class Add_detailsadmin(admin.ModelAdmin):
    list_display = ('Crop','ph','N','P','K','Rainfall','Temeprature','Humidity')


admin.site.register(Add_details,Add_detailsadmin)
# Register your models here.

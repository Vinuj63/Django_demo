from django.contrib import admin

from myapp.models import GeeksModel, FormData

# Register your models here.

admin.site.register(GeeksModel)
class GeeksModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description',]
    

admin.site.register(FormData)

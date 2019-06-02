from django.contrib import admin
from .models import Contact
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class AdminContact(ImportExportModelAdmin):
    list_display=('id','name','email','phone','info','gender','image','date_added')
admin.site.register(Contact,AdminContact)

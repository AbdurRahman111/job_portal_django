from django.contrib import admin

# Register your models here.
from .models import User, Newsletter_Table
from import_export.admin import ImportExportModelAdmin


class Bran(ImportExportModelAdmin):
    pass


class show_Newsletter(admin.ModelAdmin):
    list_display = ['Email', 'Time']

admin.site.register(User)
admin.site.register(Newsletter_Table, show_Newsletter)
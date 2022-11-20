from django.contrib import admin
from .models import Jobs, Job_Apply
# Register your models here.

class show_jobs(admin.ModelAdmin):
    list_display = ['user', 'Job_title', 'Salary', 'vacancy', 'published_on', 'Date_Line']

class show_Job_Apply(admin.ModelAdmin):
    list_display = ['Job_Seeker', 'Job', 'Name', 'Email', 'Apply_Time']


admin.site.register(Jobs, show_jobs)
admin.site.register(Job_Apply, show_Job_Apply)
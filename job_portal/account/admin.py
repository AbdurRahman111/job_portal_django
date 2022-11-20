from django.contrib import admin
from .models import job_provider_profile, job_seeker_profile
# Register your models here.


admin.site.register(job_provider_profile)
admin.site.register(job_seeker_profile)
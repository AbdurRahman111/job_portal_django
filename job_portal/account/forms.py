from django.forms import ModelForm
from .models import job_provider_profile, job_seeker_profile


class form_job_provider_profile(ModelForm):
    class Meta:
        model = job_provider_profile
        fields = ['company_name', 'company_logo', 'company_website', 'company_email', 'About_company']


class form_job_seeker_profile(ModelForm):
    class Meta:
        model = job_seeker_profile
        fields = ['Your_image', 'designation', 'Location', 'Age', 'Skill', 'Qualification', 'Resume']



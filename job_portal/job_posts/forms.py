from django.forms import ModelForm
from .models import Jobs


class form_Jobs(ModelForm):
    class Meta:
        model = Jobs
        fields = ['Job_title', 'location', 'job_nature', 'Salary', 'vacancy', 'Description', 'Keywords','published_on', 'Date_Line']



from django.db import models
from main.models import User
# Create your models here.
from ckeditor.fields import RichTextField


class job_provider_profile(models.Model):
    class Meta:
        verbose_name_plural = 'Job Provider Profile'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_logo = models.FileField(upload_to='job_provider/company_logo/', null=True, blank=True)
    company_website = models.CharField(max_length=255, null=True, blank=True)
    company_email = models.CharField(max_length=255, null=True, blank=True)
    About_company = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class job_seeker_profile(models.Model):
    class Meta:
        verbose_name_plural = 'Job Seeker Profile'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Your_image = models.FileField(upload_to='job_seeker/image/', null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True, default="")
    Location = models.CharField(max_length=255, null=True, blank=True, default="")
    Age = models.CharField(max_length=255, null=True, blank=True)
    Skill = RichTextField(null=True, blank=True)
    Qualification = RichTextField(null=True, blank=True)
    Resume = models.FileField(upload_to='job_seeker/resume/', null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
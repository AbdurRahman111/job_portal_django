from django.db import models

# Create your models here.
from main.models import User
from account.models import job_provider_profile, job_seeker_profile
from ckeditor.fields import RichTextField
from datetime import datetime

class Jobs(models.Model):
    class Meta:
        verbose_name_plural = 'Jobs'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(job_provider_profile, on_delete=models.CASCADE)
    Job_title = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    nature = (
        ("Part Time", "Part Time"),
        ("Full Time", "Full Time"),
    )
    job_nature = models.CharField(max_length=20, choices=nature, default="Part Time")
    Salary = models.CharField(max_length=255, null=True, blank=True)
    vacancy = models.CharField(max_length=255, null=True, blank=True)
    Description = RichTextField(blank=True, null=True)
    Keywords = models.TextField(blank=True, null=True, default="")
    published_on = models.DateField(default=datetime.now(), blank=True)
    Date_Line = models.DateField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.Job_title + " " + str(self.published_on)

    def applies_quantity(self):
        return Job_Apply.objects.filter(Job=self).count()


class Job_Apply(models.Model):
    class Meta:
        verbose_name_plural = 'Job Apply'
    Job_Seeker = models.ForeignKey(job_seeker_profile, on_delete = models.CASCADE)
    Job = models.ForeignKey(Jobs, on_delete = models.CASCADE)
    Name = models.CharField(max_length=255, null=True, blank=True)
    Email = models.CharField(max_length=255, null=True, blank=True)
    Portfolio_website = models.CharField(max_length=255, null=True, blank=True)
    Attach_File = models.FileField(upload_to='Job_apply/File/', null=True, blank=True)
    Cover_Letter = models.TextField(null=True, blank=True)
    Apply_Time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.Job_Seeker.user.email


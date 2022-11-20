from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from ckeditor.fields import RichTextField

class User(AbstractUser):
    type = (
        ("", ""),
        ("Admin", "Admin"),
        ("Job Seeker", "Job Seeker"),
        ("Job Provider", "Job Provider"),
    )
    user_type = models.CharField(max_length=20, choices=type, default="")




class Newsletter_Table(models.Model):
    class Meta:
        verbose_name_plural = 'Newsletter Table'
    Email = models.CharField(max_length=255)
    Time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.Email
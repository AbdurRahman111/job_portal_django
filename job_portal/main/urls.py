from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('job_search', views.job_search, name="job_search"),
    path('about', views.about, name="about"),
    path('newsletter', views.newsletter, name="newsletter"),
]
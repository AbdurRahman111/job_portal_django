from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobs, name="jobs"),
    path('/post_a_job', views.post_a_job, name="post_a_job"),
    path('/my_post', views.my_post, name="my_post"),
    path('/job_post_details/<int:pk>', views.job_post_details, name="job_post_details"),
    path('/apply_Job', views.apply_Job, name="apply_Job"),
    path('/applicants/<int:pk>', views.applicants, name="applicants"),
    path('/applicant_details/<int:pk>', views.applicant_details, name="applicant_details"),
]
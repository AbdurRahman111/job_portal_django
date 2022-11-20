from django.urls import path
from . import views

urlpatterns = [
    path('', views.talent, name="talent"),
    path('/talent_details/<int:pk>', views.talent_details, name="talent_details"),
]
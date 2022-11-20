from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_account, name="my_account"),
    path('login_func', views.login_func, name="login_func"),
    path('func_logout', views.func_logout, name="func_logout"),
    path('/my_profile', views.my_profile, name="my_profile"),
    path('/edit_profile', views.edit_profile, name="edit_profile"),
]
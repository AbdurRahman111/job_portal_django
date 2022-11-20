from django.shortcuts import render, redirect
from main.models import User
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import form_job_provider_profile, form_job_seeker_profile
from .models import job_provider_profile, job_seeker_profile


def my_account(request):
    if request.method == 'POST':
        # check the post peramiters
        sign_email = request.POST.get('email_sign')
        sign_password = request.POST.get('pass_sign')
        confirm_sign_password = request.POST.get('re_pass_sign')
        sign_first_name = request.POST.get('first_name')
        sign_last_name = request.POST.get('last_name')
        user_type = request.POST.get('user_type')

        # chech the error inputs

        user_email_info = User.objects.filter(email=sign_email)

        erorr_message = ""

        if user_email_info:
            erorr_message = "Email Already Exist !"

        elif sign_password != confirm_sign_password:
            erorr_message = "Passwords are not match !"

        elif len(sign_password) < 7:
            erorr_message = "Passwords Must be Al least 7 Digits !"

        if not erorr_message:

            # create user
            myuser = User.objects.create_user(sign_email, sign_email, sign_password)
            myuser.first_name = sign_first_name
            myuser.last_name = sign_last_name
            myuser.user_type = user_type
            myuser.is_active = True
            myuser.save()

            login(request, myuser)

            if myuser.user_type == "Job Provider":
                empty_job_provider_profile = job_provider_profile(user=myuser)
                empty_job_provider_profile.save()
            else:
                empty_job_seeker_profile = job_seeker_profile(user=myuser)
                empty_job_seeker_profile.save()

            messages.success(request, 'Your Account Successfully Created !!! Now Please Complete your profile providing some information.')

            return redirect('edit_profile')

        else:
            value_dic = {'sign_email': sign_email, 'sign_first_name': sign_first_name,
                         'sign_last_name': sign_last_name, 'erorr_message': erorr_message}
            return render(request, 'my_account.html', value_dic)

    else:
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, "my_account.html")



def login_func(request):
    if request.method == 'POST':
        log_username = request.POST['log_email']
        log_password = request.POST['log_password']
        # this is for authenticate username and password for login
        user = authenticate(username=log_username, password=log_password)

        erorr_message_2 = ""

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            erorr_message_2 ="Invalid Credentials, Please Try Again !!"

            value_func2 = {'erorr_message_2':erorr_message_2, 'log_username':log_username}
            return render(request, 'my_account.html', value_func2)


def func_logout(request):
    # this is for logout from user id
    logout(request)
    return redirect('my_account')


def my_profile(request):
    if request.user.is_authenticated:
        if request.user.user_type == "Job Provider":
            usr = request.user
            gt_job_provider_profile = job_provider_profile.objects.get(user=usr)
            context = {'gt_job_provider_profile':gt_job_provider_profile}
            return render(request, 'my_profile.html', context)

        elif request.user.user_type == "Job Seeker":
            usr = request.user
            gt_job_seeker_profile = job_seeker_profile.objects.get(user=usr)
            context = {'gt_job_seeker_profile': gt_job_seeker_profile}
            return render(request, 'my_profile.html', context)

        else:
            return render(request, 'my_profile.html')
    else:
        return redirect('my_account')


def edit_profile(request):
    if request.user.is_authenticated:
        if request.user.user_type == "Job Provider":
            get_job_provider_profile = job_provider_profile.objects.get(user=request.user)

            if request.method == 'POST':
                form = form_job_provider_profile(request.POST, request.FILES, instance=get_job_provider_profile)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Successfully Profile Information Saved !!')
                    return redirect('my_profile')
                else:
                    messages.success(request, 'Fail to Save !!')
                    return redirect('my_profile')
            else:
                form = form_job_provider_profile(instance=get_job_provider_profile)
                context = {
                    'form': form,
                    'get_job_provider_profile':get_job_provider_profile,
                }
                return render(request, 'profile_edit.html', context)


        elif request.user.user_type == "Job Seeker":
            get_job_seeker_profile = job_seeker_profile.objects.get(user=request.user)

            if request.method == 'POST':
                form = form_job_seeker_profile(request.POST, request.FILES, instance=get_job_seeker_profile)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Successfully Profile Information Saved !!')
                    return redirect('my_profile')
                else:
                    messages.success(request, 'Fail to Save !!')
                    return redirect('my_profile')
            else:
                form = form_job_seeker_profile(instance=get_job_seeker_profile)
                context = {
                    'form': form,
                    'get_job_seeker_profile': get_job_seeker_profile,
                }
                return render(request, 'profile_edit.html', context)


        else:
            return render(request, 'my_profile.html')
    else:
        return redirect('my_account')
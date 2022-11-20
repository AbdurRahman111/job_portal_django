from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .forms import form_Jobs
from account.models import job_provider_profile, job_seeker_profile
from .models import Jobs, Job_Apply


def jobs(request):
    all_jobs = Jobs.objects.all()
    context={'all_jobs':all_jobs}
    return render(request, "job-list.html", context)

def post_a_job(request):
    if request.user.is_authenticated:
        if request.user.user_type == "Job Provider":
            get_usr_job_provider = job_provider_profile.objects.get(user=request.user)

            if request.method == 'POST':
                form = form_Jobs(request.POST)

                if form.is_valid():
                    var_frm = form.save(commit=False)
                    var_frm.user = request.user
                    var_frm.user_profile = get_usr_job_provider
                    var_frm.save()

                    messages.success(request, 'Successfully Added !!')
                    return redirect('post_a_job')
                else:
                    messages.success(request, 'Fail to Add !!')
                    return redirect('post_a_job')
            else:
                form = form_Jobs()
                context = {
                    'form': form,
                    'get_usr_job_provider':get_usr_job_provider,
                }

                return render(request, 'post_a_job.html', context)
        else:
            messages.error(request, "Your Account is Not Job Provider Account. You Can Sign Up a Job Provider Account then try for post a job!")
            return redirect('my_profile')
    else:
        messages.error(request, "To Post Jobs, You have to login as a Job Provider!")
        return redirect('my_account')

def my_post(request):
    if request.user.is_authenticated:
        filter_my_post = Jobs.objects.filter(user=request.user)
        context = {'filter_my_post':filter_my_post}
        return render(request, "my_post.html", context)
    else:
        return redirect('my_account')


def job_post_details(request, pk):
    if request.user.is_authenticated:
        get_post = Jobs.objects.get(id=pk)
        context = {'get_post':get_post}
        return render(request, "job-detail.html", context)
    else:
        return redirect('my_account')


def apply_Job(request):
    if request.user.is_authenticated:
        if request.user.user_type == "Job Seeker":
            applicant_name = request.POST.get('applicant_name')
            applicant_email = request.POST.get('applicant_email')
            applicant_protfolio_web = request.POST.get('applicant_protfolio_web')
            applicant_file = request.FILES.get('applicant_file')
            applicant_coverletter = request.POST.get('applicant_coverletter')
            post_id = request.POST.get('post_id')

            get_seeker = job_seeker_profile.objects.get(user=request.user)
            get_job = Jobs.objects.get(id=post_id)
            save_Job_Apply = Job_Apply(Job_Seeker=get_seeker, Job=get_job, Name=applicant_name, Email=applicant_email, Portfolio_website=applicant_protfolio_web, Attach_File=applicant_file, Cover_Letter=applicant_coverletter)
            save_Job_Apply.save()
            messages.success(request, "Your Application Has Been Submitted !!")
            return redirect('job_post_details', post_id)
        else:
            messages.error(request,
                           "Your Account is Not Job Seeker Account. You Can Sign Up a Job Seeker Account then try to apply for a job !!")
            return redirect('my_profile')
    else:
        return redirect('my_account')


def applicants(request, pk):
    get_job = Jobs.objects.get(id=pk)
    Job_Apply_filtr = Job_Apply.objects.filter(Job=get_job)
    context = {'get_job':get_job, 'Job_Apply_filtr':Job_Apply_filtr}
    return render(request, "applicants.html", context)


def applicant_details(request, pk):
    Job_Apply_get = Job_Apply.objects.get(id=pk)
    context = {'Job_Apply_get':Job_Apply_get}
    return render(request, "applicant_details.html", context)
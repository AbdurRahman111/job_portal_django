from django.shortcuts import render, redirect
from job_posts.models import Jobs
from .models import Newsletter_Table
from django.contrib import messages
# Create your views here.
from django.db.models import Q


def index(request):
    all_jobs = Jobs.objects.all()[:5]
    context = {'all_jobs': all_jobs}
    return render(request, "index.html", context)


def job_search(request):
    job_title = request.GET.get('job_title')
    Job_Nature = request.GET.get('Job_Nature')
    location = request.GET.get('location')

    print(job_title, Job_Nature, location)

    search_jobs = Jobs.objects.filter(Q(Job_title__icontains = job_title) |Q(Keywords__icontains = job_title) | Q(job_nature__icontains = Job_Nature) | Q(location__icontains = location))

    search_jobs2 = Jobs.objects.filter(Q(Job_title__icontains = job_title) |Q(Keywords__icontains = job_title))

    context = {'search_jobs2':search_jobs2}

    return render(request, "search_result.html", context)



def newsletter(request):
    newsletter_email = request.POST.get('newsletter_email')
    save_Newsletter_Table = Newsletter_Table(Email=newsletter_email)
    save_Newsletter_Table.save()
    messages.success(request, "Newsletter Submitted Successfully !!")
    return redirect('/')


def about(request):
    return render(request, "about.html")
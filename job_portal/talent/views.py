from django.shortcuts import render
from account.models import job_seeker_profile
# Create your views here.


def talent(request):
    all_talents = job_seeker_profile.objects.all()
    context = {'all_talents':all_talents}
    return render(request, 'talent.html', context)


def talent_details(request, pk):
    get_talents = job_seeker_profile.objects.get(id=pk)
    context = {'get_talents':get_talents}
    return render(request, 'talent_details.html', context)


from django.http import HttpResponse
from django.shortcuts import render

from .models import Geography, Relevance, Skills


def home(request):
    return render(request, 'main/home.html')


def info(request):
    infopage = Relevance.objects.all()[0]
    return render(
        request,
        'main/info.html',
        context={
            'infopage': infopage,
        }
    )


def geography(request):
    geographypage = Geography.objects.all()[0]
    return render(
        request,
        'main/geography.html',
        context={
            'geographypage': geographypage,
        }
    )


def skills(request):
    skillspage = Skills.objects.all()[0]
    return render(
        request,
        'main/skills.html',
        context={
            'skillspage': skillspage,
        }
    )


def statistics(request):
    return render(request, 'main/statistics.html')


def last_vacs(request):
    return render(request, 'main/last_vacs.html')

from django.http import HttpResponse
from django.shortcuts import render

from .models import Geography, Relevance, Skill
from .utils import get_vacancies


def home(request):
    return render(request, 'main/home.html')


def relevance(request):
    relevance = Relevance.objects.all()[0]
    context = {
        'relevance': relevance
    }
    return render(request, 'main/info.html', context)


def geography(request):
    geo = Geography.objects.all()[0]
    context = {
        'geo': geo,
    }
    return render(request, 'main/geography.html', context)


def skills(request):
    skills = Skill.objects.all()
    context = {
        'skills': skills,
    }
    return render(request, 'main/skills.html', context)


def statistics(request):
    skills = Skill.objects.all()
    geo = Geography.objects.all()[0]
    relevance = Relevance.objects.all()[0]
    context = {
        'skills': skills,
        'geo': geo,
        'relevance': relevance,
    }
    return render(request, 'main/statistics.html', context)


def last_vacs(request):
    context = {
        'vacancies': get_vacancies()
    }
    return render(request, 'main/last_vacs.html', context)

from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index),
    path('', views.home, name='home'),

    # new
    path('info', views.info, name='info'),
    path('geography', views.geography, name='geography'),
    path('vacancies', views.vacancies, name='vacancies'),
    path('skills', views.skills, name='skills'),
]

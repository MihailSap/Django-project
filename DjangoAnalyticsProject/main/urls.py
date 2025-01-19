from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('info', views.relevance, name='relevance'),
    path('geography', views.geography, name='geography'),
    path('skills', views.skills, name='skills'),
    path('statistics', views.statistics, name='statistics'),
    path('last_vacs', views.last_vacs, name='last_vacs')
]

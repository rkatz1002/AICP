from django.urls import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('seInscreva', views.seInscreva, name = 'seInscreva'),
    re_path('entrarMedico', views.entrarMedico, name = 'entrarMedicos'),
    re_path('base', views.base, name = 'base'),
]
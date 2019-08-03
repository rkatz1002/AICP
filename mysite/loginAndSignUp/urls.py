from django.urls import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('seInscreva', views.seInscreva, name = 'seInscreva'),
    re_path('entrar', views.entrar, name = 'entrar'),
    re_path('base', views.base, name = 'base'),
    # re_path('entrar', auth_views.LoginView.as_view(template_name='login.html'), name = 'entrar'),
]
from django.urls import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastrarMedicamento', views.cadastrarMedicamento, name = 'cadastrarMedicamento'),
    re_path('buscarMedicamento', views.buscarMedicamento, name="buscarMedicamento"),
    re_path('saidaPrescricao', views.saidaPrescricao, name="saidaPrescricao"),
    re_path('imprimirEtiqueta', views.imprimirEtiqueta, name="imprimirEtiqueta"),
    re_path('saidaFuncionario', views.saidaFuncionario, name="saidaFuncionario"),
]
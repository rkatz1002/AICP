from django.urls import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('medicosInicial', views.inicioMedico, name = 'cadastrarMedicamento'),
    path('encaminharParaInternacao', views.inicioMedico, name = 'encaminharParaInternacao'),
    path('editarProntuario', views.inicioMedico, name = 'editarProntuario'),
    path('Receitar', views.inicioMedico, name = 'Receitar'),
    path('fornecerAtestado', views.inicioMedico, name = 'fornecerAtestado'),
    path('consultarEvolucoes', views.inicioMedico, name = 'consultarEvolucoes')
]
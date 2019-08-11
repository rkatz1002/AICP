from django.urls import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastrarMedicamento', views.cadastrarMedicamento, name = 'cadastrarMedicamento'),
    re_path('buscarMedicamento', views.buscarMedicamento, name="buscarMedicamento"),
    re_path('darEntradaMedicamento', views.darEntradaMedicamento, name="darEntradaMedicamento"),
    re_path('inicioFarmacia', views.inicioFarmacia, name="inicioFarmacia"),
    re_path('inserirBrasindice', views.inserirBrasindice, name="inserirBrasindice"),
    re_path('retirarMedicamento', views.retirarMedicamento, name="retirarMedicamento"),
    re_path('retornarMedicamento', views.retornarMedicamento, name="retornarMedicamento"), 
    re_path('saidaPrescricao', views.saidaPrescricao, name="saidaPrescricao"),
<<<<<<< HEAD
    re_path('imprimirEtiqueta', views.imprimirEtiqueta, name="imprimirEtiqueta"),
    re_path('saidaFuncionario', views.saidaFuncionario, name="saidaFuncionario"),
    re_path('cadastrarAutorizacao', views.cadastrarAutorizacao, name="cadastrarAutorizacao"),
=======
    re_path('saidaPorDoacao', views.saidaPorDoacao, name="saidaPorDoacao"),
    re_path('saidaEmergenciaMaleta', views.saidaEmergenciaMaleta, name="saidaEmergenciaMaleta"),   
    re_path('saidaMedicamento', views.saidaMedicamento, name="saidaMedicamento"),
    re_path('saidaVencimento', views.saidaMedicamento, name="saidaVencimento"),
    re_path('saidaFrascos', views.saidaMedicamento, name="saidaFrascos"),  
    re_path('sucessoFarmacia', views.sucessoFarmacia, name="sucessoFarmacia"), 
>>>>>>> db2a6849aaf202ecff0b1b259d41fcda71461c89
]
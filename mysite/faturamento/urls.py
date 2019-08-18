from django.urls import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path('faturamentoAFechar', views.faturamentoAFechar, name="faturamentoAFechar"),
    re_path('faturamentoCadastrarConvenio', views.faturamentoCadastrarConvenio, name="faturamentoCadastrarConvenio"),
    re_path('faturamentoEditarDadosProprios', views.faturamentoEditarDadosProprios, name="faturamentoEditarDadosProprios"),
]



from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from farmacia.forms import *
from datetime import date
from django.http import HttpResponseRedirect

# Create your views here.
def faturamentoAFechar(request):
    return render(request, 'faturamento-a-fechar.html')
def faturamentoCadastrarConvenio(request):
    return render(request, 'faturamento-cadastrar-convenio.html')
def faturamentoEditarDadosProprios(request):
    return render(request, 'faturamento-editar-dados-proprios.html')
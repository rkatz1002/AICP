from django.shortcuts import render
from .models import *

# Create your views here.


def inicioMedico(request):
    return render(request, 'medicos/base-medicos.html')

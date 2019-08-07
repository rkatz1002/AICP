from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from farmacia.forms import *
from farmacia.models import Medicamento

# Create your views here.

def cadastrarMedicamento(request):

    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            Nome_Medicamento = form.cleaned_data.get('Nome_Medicamento')
            Laboratorio = form.cleaned_data.get('Nome')
            Nome_do_Sal = form.cleaned_data.get('Laboratorio')
            Descricao = form.cleaned_data.get('Descricao')
            Grupo = form.cleaned_data.get('Grupo')
            Quantidade = form.cleaned_data.get('Quantidade')
            Frasco = form.cleaned_data.get('Frasco')

            return render(request, 'cadastrar-medicamento.html', {'form': form})
    else:
        form = MedicamentoForm()
        
    return render(request, 'cadastrar-medicamento.html', {'form': form})

def buscarMedicamento(request): 

    form = BuscarMedicamentoForm(request.POST or None)
    medicamentos = None

    if request.method == 'POST':
        
        if form.is_valid():
            if form.cleaned_data.get('opcao_pesquisa') == 'Nome do Medicamento':
                medicamentos = Medicamento.objects.filter(
                    Nome_Medicamento = form.cleaned_data.get('entrada'),
                )
            if form.cleaned_data.get('opcao_pesquisa') == 'Nome do Sal':
                medicamentos = Medicamento.objects.filter(
                    Nome_do_sal = form.cleaned_data.get('entrada'),
                )
            else:
                _id = Medicamento.objects.raw('SELECT ID_Brasindice FROM Codigo_Brasindice WHERE TUSS = %s', [form.cleaned_data.get('entrada')] 
                )

                medicamentos = Medicamento.objects.filter(
                    ID_Brasindice = _id
                )


    return render(request, 'buscar-medicamento.html', {'form': form, 'medicamentos': medicamentos})

def saidaPrescricao(request):

    form = SaidaPrescricaoForm(request.POST or None)
    
    if request.method == 'POST':
        
        if form.is_valid():
            
            numero_etiqueta = form.cleaned_data.get('etiqueta_medicamento')
            
            prontuario = form.cleaned_data.get('prontuario')
            
            id_historico_prescricao = clAsS.objects.raw('SELECT ID_Historico_Prescricao FROM Historico_Prescricao WHERE ID_Paciente = %s',[prontuario])
            
            x = cLasS.objects.raw('SELECT Quantidade_por_dia, Periodo_fim, Periodo_inicio, Dosagem FROM Prescricao_Medicamento WHERE Periodo_fim => GETDATE() AND ID_Historico_Prescricao = %s',[id_Historico_Prescricao]) 

            while True:

                id_historico_prescricao = Historico_Prescricao.objects.raw('SELECT ID_Historico_Prescricao FROM Historico_Prescricao WHERE ID_Paciente = %s',[prontuario])
                
                y = Prescricao_Medicamento.objects.raw('SELECT Quantidade_por_dia, Periodo_fim, Periodo_inicio, Dosagem FROM Prescricao_Medicamento WHERE Periodo_fim => GETDATE() AND ID_Historico_Prescricao = %s',[id_Historico_Prescricao])

                if (y != None):
                    x.extend(y)

                else:
                    break


    return render(request, 'saida-prescricao.html')

def teste(request):

    return render(request,'mostrar-medicamento.html')
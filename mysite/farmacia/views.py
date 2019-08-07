from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from farmacia.forms import *
from farmacia.models import *
from datetime import date

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
                medicamentos = Medicamento_Cadastro.objects.filter(
                    Nome_Medicamento = form.cleaned_data.get('entrada'),
                )
            if form.cleaned_data.get('opcao_pesquisa') == 'Nome do Sal':
                medicamentos = Medicamento_Cadastro.objects.filter(
                    Nome_do_sal = form.cleaned_data.get('entrada'),
                )
            else:
                _id = Medicamento_Cadastro.objects.raw('SELECT ID_Brasindice FROM Codigo_Brasindice WHERE TUSS = %s', [form.cleaned_data.get('entrada')] 
                )

                medicamentos = Medicamento_Cadastro.objects.filter(
                    ID_Brasindice = _id
                )


    return render(request, 'buscar-medicamento.html', {'form': form, 'medicamentos': medicamentos})

def saidaPrescricao(request):

    form = SaidaPrescricaoForm(request.POST or None)
    
    prescricoes = None

    medicamentos = None

    prontuario = None

    conferencia_medicamento = None

    if request.method == 'POST':

        if form.is_valid():
            
            prontuario = form.cleaned_data.get('prontuario')

            ID_Medicamento = form.cleaned_data.get('id_medicamento')

            if (ID_Medicamento != None):
                
                conferencia_medicamento = Medicamento_Cadastro.objects.raw(''' SELECT Nome_Medicamento FROM Medicamento_Cadastro WHERE ID_Medicamento = %s''',[ID_Medicamento])
            
            id_historico_prescricao = Historico_Prescricao.objects.raw('''  SELECT * FROM Historico_Prescricao 
                                                                            WHERE ID_Paciente = %s''',[prontuario])
            
            x = Prescricao_Medicamento.objects.raw('''  SELECT Quantidade_por_dia, Periodo_fim, Periodo_inicio, Dosagem, ID_Medicamento_Cadastro 
                                                        FROM Prescricao_Medicamento 
                                                        WHERE Periodo_fim => GETDATE() 
                                                        AND ID_Historico_Prescricao = %s''',[id_Historico_Prescricao])

            prescricoes = [x]

            z = Medicamento_Cadastro.objecs.raw('''  SELECT Nome_Medicamento FROM Medicamento_Cadastro
                                                                WHERE ID_Medicamento_Cadastro = %s''',[x.ID_Medicamento_Cadastro])
            medicamentos = [z]

            while True:

                id_historico_prescricao = Historico_Prescricao.objects.raw('''  SELECT ID_Historico_Prescricao FROM Historico_Prescricao 
                                                                                WHERE ID_Paciente = %s''',[prontuario])
                
                y = Prescricao_Medicamento.objects.raw('''      SELECT Quantidade_por_dia, Periodo_fim, Periodo_inicio 
                                                                FROM Prescricao_Medicamento 
                                                                WHERE Periodo_fim => GETDATE() AND ID_Historico_Prescricao = %s''',[id_Historico_Prescricao.ID_Historico_Prescricao])

                prescricao = [y]

                medicamento = Medicamento_Cadastro.objecs.raw('''   SELECT Nome_Medicamento FROM Medicamento_Cadastro
                                                                    WHERE ID_Medicamento_Cadastro = %s''',[y.ID_Medicamento_Cadastro])
        
                if (prescricao != None):
                    prescricoes.extend(prescricao)
                    medicamentos.extend(medicamento)

                else:
                    break
                
            if (conferencia_medicamento != None) and (prontuario != None):

                return render(request, '', {'prontuario':prontuario, 'ID_Medicamento':ID_Medicamento}) 

    return render(request, 'saida-prescricao.html',{'prescricoes':prescricoes,'medicamentos':medicamentos,'prontuario':prontuario, })

def retirarMedicamento(request):

    form = retirarMedicamentoForm(request.POST or None)

<<<<<<< HEAD
    return render(request, 'saida-prescricao.html')

def teste(request):

    return render(request,'mostrar-medicamento.html')
=======
    lote = None

    medicamento_nao_autorizado = None

    etiqueta = None

    tipo_de_pagamento = None

    valor = None

    if request.method == 'POST':
        
        if form.is_valid():

            etiqueta = form.cleaned_data.get('etiqueta')

            tipo_de_pagamento = form.cleaned_data.get('tipo_de_pagamento')

            valor = form.cleaned_data.get('valor')

            pilula = Pilula.objects.raw(''' SELECT ID_Lote_Medicamento_Entrada
                                            FROM Pilula WHERE Etiqueta = %s''',[etiqueta])

            lote = Lote_Medicamento_Entrada.objects.raw(''' SELECT  Data_Validade, Quantidade, ID_Medicamento_Cadastro 
                                                            FROM Lote_Medicamento_Entrada WHERE ID_Lote_Medicamento_Entrada = %s''',[ID_Lote_Medicamento_Entrada])
            if (lote!=None):
                medicamento_nao_autorizado = Convenio_Medicamento.objects.raw('''   SELECT ID_Convenio_Medicamento 
                                                                                    FROM Convenio_Medicamento WHERE ID_Medicamento_Cadastro = %s''',[lote.ID_Medicamento_Cadastro])

            saida = Saida_Medicamento(
                Data_Saida = date.today(),
                Valor_Saida = valor,
                ID_Prescricao_Medicamento = ID_Prescricao_Medicamento,
            )
            
            saida.save()


    if (valor != None) and (etiqueta != None) and (tipo_de_pagamento != None) and (lote != None):
        return render(request, "success.html")

    else:
        if lote!=None:
            return render(request, 'retirar-medicamento.html',{
                'data_validade': lote.Data_Validade, 
                'medicamento_nao_autorizado': medicamento_nao_autorizado,
                })
        else:
            return render(request, 'retirar-medicamento.html',{
                'data_validade': None,
                'medicamento_nao_autorizado': medicamento_nao_autorizado,
                })

def teste(request):

    return render(request, 'dar-entrada-medicamento.html')
>>>>>>> 3653af6dbf86b5dfb037e4e9905db4bbcb2cf995

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

            entrada = form.cleaned_data.get('entrada')

            opcao_pesquisa = form.cleaned_data.get('opcao_pesquisa')

            if opcao_pesquisa == 'Nome do Medicamento':
                medicamentos = Medicamento_Cadastro.objects.filter(
                    Nome_Medicamento = entrada,
                )
            
            if opcao_pesquisa == 'Nome do Sal':
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
                
                conferencia_medicamento = Medicamento_Cadastro.objects.filter(ID_Medicamento = ID_Medicamento)

            historico_prescricoes = Historico_Prescricao.objects.filter(ID_Paciente = prontuario)

            tamanho_historico = len(historico_prescricoes)

            prescricoes = []

            if (tamanho_historico > 1):
            
                for i in range(0, tamanho_historico):

                    prescricoes = prescricoes.append(
                    Prescricao_Medicamento.objects.raw('''  SELECT Quantidade_por_dia, Periodo_fim, Periodo_inicio, Dosagem, ID_Medicamento_Cadastro 
                                                            FROM farmacia_Prescricao_Medicamento 
                                                            WHERE Periodo_fim => GETDATE() 
                                                            AND ID_Historico_Prescricao = %s''',[historico_prescricoes[i]])
                                                    )

                
            medicamentos = []

            tamanho_prescricoes = len(prescricoes)

            if (tamanho_prescricoes > 1):
            
                for i in range(0, tamanho_prescricoes):
                    
                    medicamentos.append(
                        Medicamento_Cadastro.filter(
                            ID_Medicamento_Cadastro = prescricoes[i].ID_Medicamento_Cadastro
                        )
                    )

                    return render(request, 'saida-prescricao.html',{'prescricoes':prescricoes,'medicamentos':medicamentos,'prontuario':prontuario, }) 

    return render(request, 'saida-prescricao.html',{'prescricoes':prescricoes,'medicamentos':medicamentos,'prontuario':prontuario, })

def retirarMedicamento(request):

    form = retirarMedicamentoForm(request.POST or None)

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

def saidaMedicamento(request):
    
    return render(request,'saida.html')

def darEntradaMedicamento(request):

    form = darEntradaMedicamentoForm(request.POST or None)

    remedio = None

    if request.method == 'POST':

        if form.is_valid():

            etiqueta = form.cleaned_data.get('etiqueta')

            remedio = Pilula.cadastro.objects.filter(
                etiqueta = etiqueta,
            )

            isFrasco = False

            if remedio == None:

                remedio = Frasco.objects.filter(
                    etiqueta = etiqueta
                )

                isFrasco = True

            setor = Setor.objects.get(Nome_Setor = "farmacia")
                
            remedio.objects.update(ID_Setor = setor.ID_Setor)

    return render(request, 'dar-entrada-medicamento.html')

def saidaPorDoacao(request):

    form = saidaPorDoacaoForm()

    faltou_dado = None

    data_validade = None

    if request.method == 'POST':

        if form.is_valid():

            etiqueta = form.cleanead_data.get('etiqueta')

            nome_recebedor_doacao = form.cleaned_data.get('nome_recebedor_doacao')

            CNPJ_CPF = form.cleaned_data.get('CNPJ_CPF')

            motivo = form.cleaned_data.get('motivo')

             

            if (CNPJ_CPF != None) and (etiqueta != None) and (nome_recebedor_doacao != None) and (motivo != None):
                
                remedio = None

                remedio = Pilula.objects.get(etiqueta = etiqueta)

                isFrasco = False

                if remedio == None:
                    
                    isFrasco = True

                    remedio = Frasco.objects.get(Etiqueta = etiqueta)

                if remedio != None:
                    faltou_dado = False
                    
                if faltou_dado == False:
                    
                    setor = Setor.objects.get(Nome_Setor = "doado")
                
                    remedio.objects.update(ID_Setor = setor.ID_Setor)


                    doacao = Doacao_Pilula(
                        Nome_Recebedor_Doacao = nome_recebedor_doacao,
                        Motivo = motivo,
                        CNPJ_CPF = CNPJ_CPF
                    )

                    doacao.save()

                    saida = Saida_Medicamento.objects.filter(ID_Saida_Medicamento = remedio.ID_Saida_Medicamento)

                    motivo_saida = Motivo_Saida_Pilula.objects.get(Nome_Motivo_Saida_Pilula = "doacao")
                    
                    saida.update(
                        ID_Doacao_Pilula = docao.ID_Doacao_Pilula,
                        ID_Motivo_Saida_Pilula = motivo_saida.ID_Motivo_Saida_Pilula
                    )

                    lote = Lote_Medicamento_Entrada.objects.filter(ID_Lote_Medicamento_Entrada = remedio.ID_Lote_Medicamento_Entrada)
                    
                    data_validade = lote.Data_Validade

                    return render(request, 'saida-medicamento.html')

    return render(request, 'saida-por-doacao.html',{'nao_faltou_dado':faltou_dado,'data_validade':data_validade})

def saidaEmergenciaMaleta(request):

    return render(request, 'saida-emergencia-maleta.html')

def inserirBrasindice(request):

    return render(request,'inserir-brasindice.html')

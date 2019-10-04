from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from farmacia.forms import *
from datetime import date
from django.http import HttpResponseRedirect

# Create your views here.

def cadastrarMedicamento(request):

    if request.method == 'POST':

        form = MedicamentoCadastroForm(request.POST)

        if form.is_valid():
           
            Nome_Medicamento = form.cleaned_data.get('nome_medicamento')
            Laboratorio = form.cleaned_data.get('laboratorio')
            id_nome_sal = form.cleaned_data.get('id_nome_sal')
            id_tipo_medicamento = form.cleaned_data.get('id_tipo_medicamento')
            id_codigo_brasindice = form.cleaned_data.get('id_codigo_brasindice')
            id_grupo_farmacologico = form.cleaned_data.get('id_grupo_farmacologico')
            Descricao = form.cleaned_data.get('descricao')
            Grupo = form.cleaned_data.get('grupo')
            quantidade_de_gotas = form.cleaned_data.get('quantidade_de_gotas')

            x = MedicamentoCadastro.objects.latest('id_medicamento_cadastro')
            
            medicamento = MedicamentoCadastro(
                id_medicamento_cadastro = x.id_medicamento_cadastro + 1,
                nome_medicamento = Nome_Medicamento,
                laboratorio = Laboratorio,
                grupo = Grupo,
                descricao = Descricao,
                quantidade_gotas = quantidade_de_gotas,
                id_nome_sal = id_nome_sal,
                id_tipo_medicamento = id_tipo_medicamento,
                id_codigo_brasindice = id_codigo_brasindice,
                id_grupo_farmacologico = id_grupo_farmacologico
            )

            medicamento.save()

            return HttpResponseRedirect('/sucessoFarmacia')
        
    else:
        form = MedicamentoCadastroForm()

    return render(request, 'farmacia/cadastrar-medicamento.html', {'form': form})

def buscarMedicamento(request): 

    form = BuscarMedicamentoForm(request.POST or None)
    medicamentos = None
    
    medicamento_nao_existe = False
    
    nao_ha_lote = False    
    
    lotes = []

    pilulas = []

    setores = []

    if request.method == 'POST':
        
        if form.is_valid():

            entrada = form.cleaned_data.get('entrada')

            opcao_pesquisa = form.cleaned_data.get('Nome do Medicamento')
            
            if opcao_pesquisa == 'nome_do_medicamento':
                
                medicamentos = MedicamentoCadastro.objects.filter(
                    nome_medicamento = entrada,
                )
            
            if opcao_pesquisa == 'Código TUSS':
                
                sal = NomeSal.objects.filter(
                    descricao_sal = entrada,
                )

                medicamentos = MedicamentoCadastro.objects.filter(
                    id_nome_sal = sal.id_nome_sal,
                )
            
            else:
                
                brasindice = CodigoBrasindice.objects.filter(
                    tuss = entrada,
                )
                
                if brasindice.exists():
                    medicamentos = MedicamentoCadastro.objects.filter(
                        id_codigo_brasindice = brasindice[0].id_codigo_brasindice,
                    )
                
                else:
                    medicamento_nao_existe = True

            if medicamento_nao_existe == False:
                lotes = LoteMedicamentoEntrada.objects.filter(
                    id_medicamento_cadastro = medicamentos[0].id_medicamento_cadastro
                )

            for lote in lotes:
                
                pilula = Pilula.objects.filter(
                    id_lote_medicamento_entrada = lote.id_lote_medicamento_entrada
                )

                pilulas.append(pilula)
            
            if (medicamento_nao_existe == False):
                if pilula.exists():
                
                    for pilula in pilulas:
                        
                        identificacao_setor = pilula.id_setor

                        setor = Setor.objects.get(
                            pk = identificacao_setor,
                        )

                        setores.append(setor)

            if medicamentos == []:
                medicamento_nao_existe = True
            
            if ((lotes == []) and (medicamentos != [])):
                nao_ha_lote = True

    return render(request, 'farmacia/buscar-medicamento.html', {
        'form': form, 
        'medicamentos': medicamentos,
        'pilulas': pilulas,
        'setores': setores,
        'lotes': lotes,
        'medicamento_nao_existe': medicamento_nao_existe,
        'nao_ha_lote': nao_ha_lote,
    })

def saidaPrescricao(request):

    form = SaidaPrescricaoForm(request.POST or None)
    
    prescricoes = []

    medicamentos = []

    prontuario = None

    pessoa_nao_existe = None

    if request.method == 'POST':

        if form.is_valid():
            
            prontuario = form.cleaned_data.get('prontuario')

            pessoa_nao_existe = Paciente.objects.filter(id_paciente = prontuario)

            if pessoa_nao_existe == None:
                
                pessoa_nao_existe=True
            
            else:
                pessoa_nao_existe = False

            historico_prescricoes = []

            if pessoa_nao_existe == False:
                historico_prescricoes = HistoricoPrescricao.objects.filter(id_paciente = prontuario)

            tamanho_historico = len(historico_prescricoes)

            prescricoes = []

            if (tamanho_historico > 1):
            
                for i in range(0, tamanho_historico):

                    prescricoes.append(
                    PrescricaoMedicamento.objects.raw('''  SELECT * 
                                                            FROM farmacia_Prescricao_Medicamento 
                                                            WHERE Periodo_fim => GETDATE() 
                                                            AND ID_Historico_Prescricao = %s''',[historico_prescricoes[i].id_historico_prescricao])
                                                    )

                
            medicamentos = []

            tamanho_prescricoes = len(prescricoes)

            if (tamanho_prescricoes > 1):
            
                for i in range(0, tamanho_prescricoes):
                    
                    medicamentos.append(
                        MedicamentoCadastro.filter(
                            id_medicamento_cadastro = prescricoes[i].id_medicamento_cadastro
                        )
                    )

                    return render(request, 'farmacia/retirar-medicamento.html',{'prescricoes':prescricoes,'medicamentos':medicamentos,'pessoa_nao_existe':pessoa_nao_existe, }) 

    return render(request, 'farmacia/saida-prescricao.html',{'medicamentos':medicamentos,'pessoa_nao_existe':pessoa_nao_existe, })

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

            pilula = Pilula.objects.raw(''' SELECT *
                                            FROM Pilula WHERE Etiqueta = %s''',[etiqueta])

            lote = LoteMedicamentoEntrada.objects.raw(''' SELECT  Data_Validade, Quantidade, ID_Medicamento_Cadastro 
                                                            FROM Lote_Medicamento_Entrada WHERE ID_Lote_Medicamento_Entrada = %s''',[pilula[0].id_lote_medicamento_entrada])
            if (lote!=None):
                medicamento_nao_autorizado = ConvenioMedicamento.objects.raw('''   SELECT *
                                                                                    FROM Convenio_Medicamento WHERE ID_Medicamento_Cadastro = %s''',[lote.id_medicamento_cadastro])

            saida = SaidaMedicamento(
                data_saida = date.today(),
                valor_Saida = valor,
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
            return render(request, 'farmacia/retirar-medicamento.html',{
                'data_validade': None,
                'medicamento_nao_autorizado': medicamento_nao_autorizado,
                })


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

    return render(request, 'farmacia/dar-entrada-medicamento.html')

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

                    return render(request, 'farmacia/saida-medicamento.html')

    return render(request, 'farmacia/saida-por-doacao.html',{'nao_faltou_dado':faltou_dado,'data_validade':data_validade})

def saidaEmergenciaMaleta(request):
    return render(request, 'farmacia/saida-emergencia-maleta.html')

def inserirBrasindice(request):
    return render(request,'farmacia/inserir-brasindice.html')

def inicioFarmacia(request):
    return render(request, 'farmacia/inicio-farmacia.html')

def saidaMedicamento(request):
    return render(request,'farmacia/saida-medicamento.html')

def retornarMedicamento(request):
    return render(request, 'farmacia/retornar-medicamento.html')

def sucessoFarmacia(request):
    return render(request, 'farmacia/success.html')
def saidaFrascos(request):
    pass
def saidaVencimento(request):
    pass
def saidaFuncionario(request):
    pass
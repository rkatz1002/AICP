from django import forms
from loginAndSignUp.models import *


class MedicamentoCadastroForm(forms.Form):

    sais = NomeSal.objects.filter(pk=2)
    tipos_medicamentos = TipoMedicamento.objects.filter(pk=1)
    codigos_brasindice = CodigoBrasindice.objects.filter(pk=1)
    grupos_farmacologicos = GrupoFarmacologico.objects.filter(pk=1)

    nome_medicamento = forms.CharField(max_length=50)
    laboratorio = forms.CharField(max_length=50)
    grupo = forms.CharField(max_length=50)
    descricao = forms.CharField(max_length=50)
    quantidade_de_gotas = forms.IntegerField(required=False)
    id_nome_sal = forms.ModelChoiceField(
        queryset=sais,
        empty_label= "(Escolha um Sal)",
    )
    id_tipo_medicamento = forms.ModelChoiceField(
        queryset=tipos_medicamentos,
        empty_label= "(Escolha um tipo de medicamento)",
    )
    id_codigo_brasindice = forms.ModelChoiceField(
        queryset=codigos_brasindice,
        empty_label= "(Escolha um código brasíndice)",
    )
    id_grupo_farmacologico = forms.ModelChoiceField(
        queryset=grupos_farmacologicos,
        empty_label= "(Escolha um grupo farmacológico)",
    )
        

class BuscarMedicamentoForm(forms.Form):

    RADIO_BUTTON_CHOICES = [
        ('Nome do Sal','Nome do Sal'),
        ('Nome do Medicamento','Nome do Medicamento'),        
        ('Código TUSS','Código TUSS'),
    ]

    opcao_pesquisa = forms.ChoiceField(widget=forms.RadioSelect,choices=RADIO_BUTTON_CHOICES)

    entrada = forms.CharField(max_length = 100)


class SaidaPrescricaoForm(forms.Form):

    prontuario = forms.IntegerField()


class retirarMedicamentoForm(forms.Form):

    RADIO_BUTTON_CHOICES = [
        ('Brasindice_PMF','Brasindice_PMF'),
        ('Brasindice_PF','Brasindice_PF'),
        ('Simpro','Simpro'),
    ]

    opcao_preco = forms.ChoiceField(widget=forms.RadioSelect, choices=RADIO_BUTTON_CHOICES)

    valor = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    etiqueta = forms.IntegerField()
from django import forms
from farmacia.models import *


class MedicamentoForm(forms.Form):

    class Meta:
        model = Medicamento_Cadastro
        fields = '__all__'
        

class BuscarMedicamentoForm(forms.Form):

    RADIO_BUTTON_CHOICES = [
        ('Nome do Sal','Nome do Sal'),
        ('Nome do Medicamento','Nome do Medicamento'),        
        ('Código TUSS','Código TUSS'),
    ]

    opcao_pesquisa = forms.ChoiceField(widget=forms.RadioSelect,choices=RADIO_BUTTON_CHOICES)

    entrada = models.CharField(max_length = 100)


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
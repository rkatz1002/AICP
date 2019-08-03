from django import forms
from farmacia.models import *


class MedicamentoForm(forms.Form):

    class Meta:
        model = Medicamento
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

    etiqueta_medicamento = forms.IntegerField()
    prontuario = forms.IntegerField()
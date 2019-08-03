from django.db import models

# Create your models here.

class Codigo_Brasindice(models.Model):

    ID_Brasindice = models.IntegerField(primary_key=True)
    
    Brasindice_PMF = models.DecimalField(
        decimal_places=2,
        max_digits = 18
    )
    
    Brasindice_PF =models.DecimalField(
        decimal_places=2,
        max_digits = 18
    )
    
    Simpro = models.DecimalField(
        decimal_places=2,
        max_digits = 18
    )

    TUSS = models.CharField(max_length=50)
    
    TISS = models.CharField(max_length=50)


class Grupo_Farmacologico(models.Model):

    ID_Grupo_Farmacologico = models.IntegerField(primary_key=True)    

    Nome_Grupo_Farmacologico = models.CharField(max_length = 50)

class Tipo(models.Model):

    ID_Tipo = models.IntegerField(primary_key=True)

    Nome_Tipo = models.CharField(max_length=50)

class Convenio(models.Model):
    
    ID_Convenio = models.IntegerField(primary_key=True)

class Medicamento(models.Model):

    ID_Medicamento_Cadastro = models.IntegerField(primary_key=True)

    ID_Convenio_Medicamento = models.ForeignKey(
        to = Convenio, 
        on_delete = models.CASCADE
    )

    ID_Tipo = models.ForeignKey(
        to = Tipo,
        on_delete = models.CASCADE
    )

    ID_Grupo_Farmacologico = models.ForeignKey(
        to = Grupo_Farmacologico,  
        on_delete = models.CASCADE
    )

    ID_Brasindice = models.ForeignKey(
        to= Codigo_Brasindice,
        on_delete = models.CASCADE,
    )

    Nome_Medicamento = models.CharField(max_length = 50)
    
    Laboratorio = models.CharField(max_length = 50)
    
    Nome_do_Sal = models.CharField(max_length = 50)
    
    Descricao = models.CharField(max_length = 50)
    
    Grupo = models.CharField(max_length = 50)
    
    Quantidade = models.IntegerField()
    
    # Frasco = models.Bit1BooleanField()

    def __str__(self):
        return self.ID_Medicamento_Cadastro

class Historico_Prescricao(models.Model):

    ID_Historico_Prescricao = models.IntegerField(primary_key=True)
    
    FILESTREAM_Prescricao = models.CharField(max_length = 100)
    
    Data_Historico_Prescricao = models.DateField()
    
    # ID_Paciente = models.ForeignKey(
    #     to = Paciente, 
    #     on_delete = models.CASCADE
    # )
    
    # ID_Medico = models.ForeignKey(
    #     to = Medico, 
    #     on_delete = models.CASCADE
    # )
    
    def __str__(self):
        return self.ID_Historico_Prescricao

class Prescricao_Medicamento(models.Model):

    ID_Prescricao_Medicamento = models.IntegerField(primary_key=True)
    
    Quantidade_por_dia = models.IntegerField()
    
    Periodo_inicio = models.DateField()
    
    Periodo_fim = models.DateField()
    
    ID_Medicamento_Cadastro = models.ForeignKey(
        to = Medicamento, 
        on_delete = models.CASCADE
    )
    
    ID_Historico_Prescricao = models.ForeignKey(
        to = Historico_Prescricao, 
        on_delete = models.CASCADE
    )
    
    Dosagem = models.IntegerField()

    def __str__(self):
        return self.ID_Prescricao_Medicamento
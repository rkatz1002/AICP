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

class Medicamento_Cadastro(models.Model):

    ID_Medicamento_Cadastro = models.IntegerField(primary_key=True)

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

    def __str__(self):
        return self.ID_Medicamento_Cadastro

class Convenio_Medicamento(models.Model):
    
    ID_Convenio_Medicamento = models.IntegerField(primary_key=True)
    ID_Medicamento_Cadastro = models.ForeignKey(
        to=Medicamento_Cadastro,
        on_delete=models.CASCADE,
    )

class Historico_Prescricao(models.Model):

    ID_Historico_Prescricao = models.IntegerField(primary_key=True)
    
    FILESTREAM_Prescricao = models.CharField(max_length = 100)
    
    Data_Historico_Prescricao = models.DateField()
    
    def __str__(self):
        return self.ID_Historico_Prescricao

class Prescricao_Medicamento(models.Model):

    ID_Prescricao_Medicamento = models.IntegerField(primary_key=True)
    
    Quantidade_por_dia = models.IntegerField()
    
    Periodo_inicio = models.DateField()
    
    Periodo_fim = models.DateField()
    
    ID_Medicamento_Cadastro = models.ForeignKey(
        to = Medicamento_Cadastro, 
        on_delete = models.CASCADE
    )
    
    ID_Historico_Prescricao = models.ForeignKey(
        to = Historico_Prescricao, 
        on_delete = models.CASCADE
    )
    
    Dosagem = models.IntegerField()

    def __str__(self):
        return self.ID_Prescricao_Medicamento

class Lote_Medicamento_Entrada(models.Model):

    ID_Lote_Medicamento_Entrada = models.IntegerField(primary_key=True)
    
    Lote = models.IntegerField()

    Data_Entrada = models.DateField()

    Data_Validade = models.DateField()

    ID_Medicamento_Cadastro = models.ForeignKey(
        to=Medicamento_Cadastro,
        on_delete=models.CASCADE
    )

    Quantidade = models.IntegerField()


class Setor(models.Model):

    ID_Setor = models.IntegerField(primary_key=True)

    Nome_Setor = models.CharField(max_length=50)

    Descricao =models.CharField(max_length=120)

class Saida_Medicamento(models.Model):

    ID_Saida_Medicamento = models.IntegerField(primary_key=True)
    
    Data_Saida = models.DateTimeField()

    Valor_Saida = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    Quantidade_de_Gotas = models.IntegerField()
    
    ID_Prescricao_Medicamento =models.ForeignKey(
        to = Prescricao_Medicamento,
        on_delete = models.CASCADE,
    )

class Pilula(models.Model):

    ID_Pilula = models.IntegerField(primary_key=True)
    
    Valor_Saida = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    
    Quantidade_Gotas = models.IntegerField()
    
    Etiqueta = models.IntegerField()

    ID_Lote_Medicamento_Entrada = models.ForeignKey(
        to=Lote_Medicamento_Entrada,
        on_delete=models.CASCADE
    )

    ID_Setor = models.ForeignKey(
        to=Setor,
        on_delete=models.CASCADE
    )

    ID_Saida_Medicamento = models.ForeignKey(
        to=Saida_Medicamento,
        on_delete=models.CASCADE
    )

class Frasco(models.Model):

    ID_Frasco =  models.IntegerField(primary_key=True)

    Quantidade_Gotas_Saiu = models.IntegerField()

    ID_Lote_Medicamento_Entrada = models.ForeignKey(
        to=Lote_Medicamento_Entrada,
        on_delete=models.CASCADE,
    )

    ID_Setor = models.ForeignKey(
        to=Setor,
        on_delete=models.CASCADE,
    )

    ID_Saida_Medicamento = models.ForeignKey(
        to=Saida_Medicamento,
        on_delete=models.CASCADE,
    )

# class Medicamento_Estoque(models.Model):

#     Quantidade_Total = 

#     Quantidade_Farmacia = 

#     ID_Medicamento_Cadastro = 

# class Controle(models.Model):

#     ID_Controle = 
#     ID_Prescricao_Medicamento =
#     Previsao_Estoque =
#     Status_Prescricao =
#     Cobertura_Convenio =

# class Pag_Particular_Med(models.Model):

#     ID_Pag_Particular_Med =
#     Data_Previsao_Pag = 
#     Data_Pag = 
#     Valor_Particular = 
#     ID_Prescricao_Medicamento =

# class Pag_Convenio_Medicamento(models.Model):

#     ID_Pag_Convenio_Medicamento = 
#     Quantidade = 

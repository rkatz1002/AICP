from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

# class UserAdmin(models.Model):

#     id = models.IntegerField(primary_key=True)
#     login = models.CharField(max_length=200)   
#     senha1 = models.CharField(max_length=200)
#     senha2 = models.CharField(max_length=200)

#     class Meta:
#         db_table = "User"   
    
#     def authenticate(self, request, username=None, password=None):
#         pass

class Pessoa(AbstractUser):
    
    ESTADO_CIVIL_CHOICES = [
        ('Solteiro','Solteiro'),
        ('Casado','Casado'),        
        ('Divorciado','Divorciado'),
        ('Viúvo','Viúvo'),
        ('Separado','Separado'),
    ]

    GRAU_DE_INSTRUCAO_CHOICES = [

        ('Analfabeto','Analfabeto'),
        ('Ensino_Fundamental_Incompleto','Ensino_Fundamental_Incompleto'),
        ('Ensino_Fundamental_Completo','Ensino_Fundamental_Completo'),
        ('Ensino_Médio_Incompleto','Ensino_Médio_Incompleto'),
        ('Ensino_Médio_Completo','Ensino_Médio_Completo'),
        ('Superior_Completo','Superior_Completo'),
        ('Pós-Graduação','Pós-Graduação'),
        ('Mestrado','Mestrado'),
        ('Doutorado','Doutorado'),
        ('Pós-Doutorado','Pós-Doutorado'),
    ]

    cpf = models.CharField(max_length=20, primary_key=True)
    Nome = models.CharField(max_length=200)
    Falecido = models.BooleanField(default=False)
    Data_Nascimento = models.DateField()
    Telefone_Residencial = models.CharField(max_length=20)
    Telefone_Celular = models.CharField(max_length=20)
    rg = models.CharField(max_length=20)
    rg_orgao_expeditor = models.CharField(max_length=50)
    rg_uf = models.CharField(max_length=2)
    rg_data_emissao = models.DateField()
    Naturalidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    Profissao = models.CharField(max_length=50)
    Conjugue = models.CharField(max_length=50)
    Endereco_Rua = models.CharField(max_length=100)
    Endereco_Complemento = models.IntegerField()
    Endereco_CEP = models.IntegerField()
    Endereco_Estado = models.CharField(max_length=100)
    Endereco_Cidade = models.CharField(max_length=100)
    Endereco_Bairro = models.CharField(max_length=100)
    Estado_Civil = models.CharField(max_length=30, choices=ESTADO_CIVIL_CHOICES)
    Grau_de_Instrucao = models.CharField(max_length=50, choices=GRAU_DE_INSTRUCAO_CHOICES)
    Email = models.CharField(max_length=200)


    def __str__(self):
        return self.Nome
    
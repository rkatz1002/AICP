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

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdicionalNoturno(models.Model):
    id_adicional_noturno = models.IntegerField(db_column='ID_Adicional_Noturno', primary_key=True)  # Field name made lowercase.
    id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='ID_Funcionario')  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Adicional_Noturno'


class ArquivoMedicoResponsavel(models.Model):
    id_arquivo_medico_responsavel = models.IntegerField(db_column='ID_Arquivo_Medico_Responsavel', primary_key=True)  # Field name made lowercase.
    filestream_arquivo_medico_responsavel = models.CharField(db_column='FILESTREAM_Arquivo_Medico_Responsavel', max_length=200)  # Field name made lowercase.
    data = models.DateField(db_column='Data')  # Field name made lowercase.
    id_atendimento_historico_medico_responsavel = models.ForeignKey('HistoricoMedicoResponsavel', models.DO_NOTHING, db_column='ID_Atendimento_Historico_Medico_Responsavel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Arquivo_Medico_Responsavel'


class AtendimentoMedicoPlantao(models.Model):
    id_atendimento_medico_plantao = models.IntegerField(db_column='ID_Atendimento_Medico_Plantao', primary_key=True)  # Field name made lowercase.
    data_atendimento = models.DateField(db_column='Data_Atendimento')  # Field name made lowercase.
    filestream_atendimento_medico_plantao = models.CharField(db_column='FILESTREAM_Atendimento_Medico_Plantao', max_length=200)  # Field name made lowercase.
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='ID_Paciente')  # Field name made lowercase.
    id_medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='ID_Medico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Atendimento_Medico_Plantao'


class Banco(models.Model):
    id_banco = models.CharField(db_column='ID_Banco', primary_key=True, max_length=50)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50)  # Field name made lowercase.
    dinheiro_dentro = models.DecimalField(db_column='Dinheiro_dentro', max_digits=8, decimal_places=2)  # Field name made lowercase.
    dinheiro_dentro_real = models.DecimalField(db_column='Dinheiro_dentro_Real', max_digits=8, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Banco'


class Cid(models.Model):
    id_cid = models.IntegerField(db_column='ID_CID', primary_key=True)  # Field name made lowercase.
    nome_cid = models.CharField(db_column='Nome_CID', max_length=50)  # Field name made lowercase.
    numero_cadastrado = models.CharField(db_column='Numero_Cadastrado', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CID'


class Cipa(models.Model):
    id_cipa = models.IntegerField(db_column='ID_CIPA', primary_key=True)  # Field name made lowercase.
    id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='ID_Funcionario')  # Field name made lowercase.
    cargo_cipa = models.CharField(db_column='Cargo_CIPA', max_length=50)  # Field name made lowercase.
    data_inicio = models.DateField(db_column='Data_Inicio')  # Field name made lowercase.
    data_fim = models.DateField(db_column='Data_Fim')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CIPA'


class CadastroAcidenteTrabalho(models.Model):
    id_cadastro_acidente_trabalho = models.IntegerField(db_column='ID_Cadastro_Acidente_Trabalho', primary_key=True)  # Field name made lowercase.
    motivo_acidente = models.CharField(db_column='Motivo_Acidente', max_length=120)  # Field name made lowercase.
    data_acidente = models.DateField(db_column='Data_Acidente')  # Field name made lowercase.
    data_abertura = models.DateField(db_column='Data_Abertura')  # Field name made lowercase.
    numero_cat = models.CharField(db_column='Numero_CAT', max_length=50)  # Field name made lowercase.
    id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='ID_Funcionario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cadastro_Acidente_Trabalho'


class CadastroHd(models.Model):
    id_cadastro_hd = models.IntegerField(db_column='ID_Cadastro_HD', primary_key=True)  # Field name made lowercase.
    data_inicio = models.DateField(db_column='Data_Inicio')  # Field name made lowercase.
    data_fim = models.DateField(db_column='Data_Fim')  # Field name made lowercase.
    senha_provisoria = models.CharField(db_column='Senha_Provisoria', max_length=100)  # Field name made lowercase.
    data_validade_senha = models.DateField(db_column='Data_Validade_Senha')  # Field name made lowercase.
    id_leito = models.ForeignKey('Leito', models.DO_NOTHING, db_column='ID_Leito')  # Field name made lowercase.
    id_cid = models.ForeignKey(Cid, models.DO_NOTHING, db_column='ID_CID')  # Field name made lowercase.
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='ID_Paciente')  # Field name made lowercase.
    id_medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='ID_Medico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cadastro_HD'


class CadastroInternacao(models.Model):
    id_cadastro_internacao = models.IntegerField(db_column='ID_Cadastro_Internacao', primary_key=True)  # Field name made lowercase.
    data_inicio = models.DateField(db_column='Data_Inicio')  # Field name made lowercase.
    data_fim = models.DateField(db_column='Data_Fim', blank=True, null=True)  # Field name made lowercase.
    valor_caucao = models.DecimalField(db_column='Valor_Caucao', max_digits=8, decimal_places=2)  # Field name made lowercase.
    recomendacao_medica = models.IntegerField(db_column='Recomendacao_Medica')  # Field name made lowercase.
    filestream_documento_recomendacao_medica = models.CharField(db_column='FILESTREAM_Documento_Recomendacao_Medica', max_length=200)  # Field name made lowercase.
    involuntaria = models.IntegerField(db_column='Involuntaria')  # Field name made lowercase.
    dependente_quimico = models.IntegerField(db_column='Dependente_Quimico')  # Field name made lowercase.
    filestream_documento_ordem_judicial = models.CharField(db_column='FILESTREAM_Documento_Ordem_Judicial', max_length=200, blank=True, null=True)  # Field name made lowercase.
    data_aviso_ordem_judicial = models.DateTimeField(db_column='Data_Aviso_Ordem_Judicial', blank=True, null=True)  # Field name made lowercase.
    ordem_judicial = models.IntegerField(db_column='Ordem_Judicial', blank=True, null=True)  # Field name made lowercase.
    filestream_documento_termo_ciencia = models.CharField(db_column='FILESTREAM_Documento_Termo_Ciencia', max_length=200, blank=True, null=True)  # Field name made lowercase.
    filestream_documento_familia_de_acordo = models.CharField(db_column='FILESTREAM_Documento_Familia_de_Acordo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    senha_provisoria = models.CharField(db_column='Senha_Provisoria', max_length=50)  # Field name made lowercase.
    data_validade_senha = models.CharField(db_column='Data_Validade_Senha', max_length=50)  # Field name made lowercase.
    motivo_alta = models.CharField(db_column='Motivo_Alta', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='ID_Paciente')  # Field name made lowercase.
    id_leito = models.ForeignKey('Leito', models.DO_NOTHING, db_column='ID_Leito')  # Field name made lowercase.
    id_cid = models.ForeignKey(Cid, models.DO_NOTHING, db_column='ID_CID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cadastro_Internacao'


class CadastroProduto(models.Model):
    id_cadastro_produto = models.IntegerField(db_column='ID_Cadastro_Produto', primary_key=True)  # Field name made lowercase.
    nome_produto = models.CharField(db_column='Nome_Produto', max_length=50)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100)  # Field name made lowercase.
    quantidade_minima = models.IntegerField(db_column='Quantidade_Minima')  # Field name made lowercase.
    id_fornecedor = models.ForeignKey('Fornecedor', models.DO_NOTHING, db_column='ID_Fornecedor')  # Field name made lowercase.
    id_categoria_produto = models.ForeignKey('CategoriaProduto', models.DO_NOTHING, db_column='ID_Categoria_Produto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cadastro_Produto'


class CargoFuncionario(models.Model):
    id_cargo_funcionario = models.IntegerField(db_column='ID_Cargo_Funcionario', primary_key=True)  # Field name made lowercase.
    nome_cargo = models.CharField(db_column='Nome_Cargo', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cargo_Funcionario'


class CategoriaProduto(models.Model):
    id_categoria_produto = models.IntegerField(db_column='ID_Categoria_Produto', primary_key=True)  # Field name made lowercase.
    nome_categoria_produto = models.CharField(db_column='Nome_Categoria_Produto', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categoria_Produto'


class Certificado(models.Model):
    id_certificado = models.IntegerField(db_column='ID_Certificado', primary_key=True)  # Field name made lowercase.
    registro_certificado = models.CharField(db_column='Registro_Certificado', max_length=30)  # Field name made lowercase.
    vencimento_certificado = models.DateField(db_column='Vencimento_Certificado')  # Field name made lowercase.
    verificado = models.IntegerField(db_column='Verificado')  # Field name made lowercase.
    protocolo_cnes = models.CharField(db_column='Protocolo_CNES', max_length=50)  # Field name made lowercase.
    id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='ID_Funcionario', blank=True, null=True)  # Field name made lowercase.
    id_conselho_classe = models.ForeignKey('ConselhoClasse', models.DO_NOTHING, db_column='ID_Conselho_Classe')  # Field name made lowercase.
    id_medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='ID_Medico', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Certificado'


class CodigoBrasindice(models.Model):
    id_codigo_brasindice = models.IntegerField(db_column='ID_Codigo_Brasindice', primary_key=True)  # Field name made lowercase.
    brasindice_pmf = models.DecimalField(db_column='Brasindice_PMF', max_digits=8, decimal_places=2)  # Field name made lowercase.
    brasindice_pf = models.DecimalField(db_column='Brasindice_PF', max_digits=8, decimal_places=2)  # Field name made lowercase.
    simpro = models.DecimalField(db_column='Simpro', max_digits=8, decimal_places=2)  # Field name made lowercase.
    tuss = models.CharField(db_column='TUSS', max_length=50)  # Field name made lowercase.
    tiss = models.CharField(db_column='TISS', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Codigo_brasindice'


class ConselhoClasse(models.Model):
    id_conselho_classe = models.IntegerField(db_column='ID_Conselho_Classe', primary_key=True)  # Field name made lowercase.
    tipo_conselho_classe = models.CharField(db_column='Tipo_Conselho_Classe', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Conselho_Classe'


class Consulta(models.Model):
    id_consulta = models.IntegerField(db_column='ID_Consulta', primary_key=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data')  # Field name made lowercase.
    confirmado = models.IntegerField(db_column='Confirmado')  # Field name made lowercase.
    consultado = models.IntegerField(db_column='Consultado')  # Field name made lowercase.
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='ID_Paciente')  # Field name made lowercase.
    id_medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='ID_Medico')  # Field name made lowercase.
    id_tipo_cobranca = models.ForeignKey('TipoCobranca', models.DO_NOTHING, db_column='ID_Tipo_Cobranca')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Consulta'


class ConsultaConvenio(models.Model):
    id_consulta_convenio = models.IntegerField(db_column='ID_Consulta_Convenio', primary_key=True)  # Field name made lowercase.
    valor_consulta = models.DecimalField(db_column='Valor_Consulta', max_digits=8, decimal_places=2)  # Field name made lowercase.
    id_contrato_convenio = models.ForeignKey('ContratoConvenio', models.DO_NOTHING, db_column='ID_Contrato_Convenio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Consulta_Convenio'


class ContratoConvenio(models.Model):
    id_contrato_convenio = models.IntegerField(db_column='ID_Contrato_Convenio', primary_key=True)  # Field name made lowercase.
    id_convenio = models.ForeignKey('Convenio', models.DO_NOTHING, db_column='ID_Convenio')  # Field name made lowercase.
    filestream_contrato_convenio = models.CharField(db_column='FILESTREAM_Contrato_Convenio', max_length=200)  # Field name made lowercase.
    tipo_contrato = models.CharField(db_column='Tipo_Contrato', max_length=50)  # Field name made lowercase.
    data_inicio = models.DateField(db_column='Data_Inicio')  # Field name made lowercase.
    data_fim = models.DateField(db_column='Data_Fim')  # Field name made lowercase.
    valor_mensal = models.DecimalField(db_column='Valor_Mensal', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contrato_Convenio'


class Controle(models.Model):
    id_controle = models.IntegerField(db_column='ID_Controle', primary_key=True)  # Field name made lowercase.
    id_prescricao_medicamento = models.ForeignKey('PrescricaoMedicamento', models.DO_NOTHING, db_column='ID_Prescricao_Medicamento')  # Field name made lowercase.
    previsao_estoque = models.IntegerField(db_column='Previsao_Estoque')  # Field name made lowercase.
    status_prescricao = models.CharField(db_column='Status_Prescricao', max_length=50)  # Field name made lowercase.
    cobertura_convenio = models.CharField(db_column='Cobertura_Convenio', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Controle'


class Convenio(models.Model):
    id_convenio = models.IntegerField(db_column='ID_Convenio', primary_key=True)  # Field name made lowercase.
    nome_convenio = models.CharField(db_column='Nome_Convenio', max_length=50)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Convenio'


class ConvenioMedicamento(models.Model):
    id_convenio_medicamento = models.IntegerField(db_column='ID_Convenio_medicamento', primary_key=True)  # Field name made lowercase.
    id_medicamento_cadastro = models.ForeignKey('MedicamentoCadastro', models.DO_NOTHING, db_column='ID_Medicamento_Cadastro')  # Field name made lowercase.
    id_convenio = models.ForeignKey(Convenio, models.DO_NOTHING, db_column='ID_Convenio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Convenio_Medicamento'


class DadosHospital(models.Model):
    id_cnpj = models.CharField(db_column='ID_CNPJ', primary_key=True, max_length=50)  # Field name made lowercase.
    end_rua = models.CharField(db_column='End_Rua', max_length=100)  # Field name made lowercase.
    end_numero = models.IntegerField(db_column='End_Numero')  # Field name made lowercase.
    end_cep = models.CharField(db_column='End_CEP', max_length=10)  # Field name made lowercase.
    end_complemento = models.CharField(db_column='End_Complemento', max_length=100)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=50)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dados_Hospital'


class DescontosGratificacoes(models.Model):
    id_descontos_gratificacoes = models.IntegerField(db_column='ID_Descontos_Gratificacoes', primary_key=True)  # Field name made lowercase.
    mes = models.IntegerField(db_column='Mes')  # Field name made lowercase.
    gratificacao = models.IntegerField(db_column='Gratificacao')  # Field name made lowercase.
    valor = models.DecimalField(db_column='Valor', max_digits=8, decimal_places=2)  # Field name made lowercase.
    id_tipo_desc_grat = models.ForeignKey('TipoDescontoGratificacao', models.DO_NOTHING, db_column='ID_Tipo_Desc_Grat')  # Field name made lowercase.
    id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='ID_Funcionario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Descontos_Gratificacoes'


class DiariasConvenio(models.Model):
    id_diarias_convenio = models.IntegerField(db_column='ID_Diarias_Convenio', primary_key=True)  # Field name made lowercase.
    valor_diarias_convenio = models.DecimalField(db_column='Valor_Diarias_Convenio', max_digits=8, decimal_places=2)  # Field name made lowercase.
    id_contrato_convenio = models.ForeignKey(ContratoConvenio, models.DO_NOTHING, db_column='ID_Contrato_Convenio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Diarias_Convenio'


class DispMedConsulta(models.Model):
    id_disp_med_consulta = models.IntegerField(db_column='ID_Disp_Med_Consulta', primary_key=True)  # Field name made lowercase.
    data_disp_med_consulta = models.DateField(db_column='Data_Disp_Med_Consulta')  # Field name made lowercase.
    periodo_consulta = models.CharField(db_column='Periodo_Consulta', max_length=50)  # Field name made lowercase.
    sala_consulta = models.IntegerField(db_column='Sala_Consulta')  # Field name made lowercase.
    id_medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='ID_Medico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disp_Med_Consulta'


class DisponibilidadeHorarioMultidisciplinar(models.Model):
    id_horario = models.IntegerField(db_column='ID_Horario', primary_key=True)  # Field name made lowercase.
    horario_inicio = models.DateTimeField(db_column='Horario_Inicio')  # Field name made lowercase.
    horario_fim = models.DateTimeField(db_column='Horario_Fim')  # Field name made lowercase.
    id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='ID_Funcionario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disponibilidade_Horario_Multidisciplinar'


class DoacaoPilula(models.Model):
    id_doacao_pilula = models.IntegerField(db_column='ID_Doacao_Pilula', primary_key=True)  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=300)  # Field name made lowercase.
    nome_recebedor_doacao = models.CharField(db_column='Nome_Recebedor_Doacao', max_length=300)  # Field name made lowercase.
    cnpj_cpf = models.CharField(db_column='CNPJ_CPF', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Doacao_Pilula'


class Emprestimo(models.Model):
    id_emprestimo = models.IntegerField(db_column='ID_Emprestimo', primary_key=True)  # Field name made lowercase.
    id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='ID_Funcionario')  # Field name made lowercase.
    valor_total_emprestimo = models.DecimalField(db_column='Valor_Total_Emprestimo', max_digits=8, decimal_places=2)  # Field name made lowercase.
    valor_pago = models.DecimalField(db_column='Valor_Pago', max_digits=8, decimal_places=2)  # Field name made lowercase.
    qtd_prestacoes = models.IntegerField(db_column='Qtd_Prestacoes')  # Field name made lowercase.
    data_inicio = models.DateField(db_column='Data_inicio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Emprestimo'


class EnfermagemPlantao(models.Model):
    id_atendimento_enfermagem_plantao = models.IntegerField(db_column='ID_Atendimento_Enfermagem_Plantao', primary_key=True)  # Field name made lowercase.
    data_atendimento = models.DateField(db_column='Data_Atendimento')  # Field name made lowercase.
    filestream_enfermagem_plantao = models.CharField(db_column='FILESTREAM_Enfermagem_Plantao', max_length=200)  # Field name made lowercase.
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='ID_Paciente')  # Field name made lowercase.
    id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='ID_Funcionario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Enfermagem_Plantao'


class EscalaMedicoPlantao(models.Model):
    id_escala_medico_plantao = models.IntegerField(db_column='ID_Escala_Medico_Plantao', primary_key=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data')  # Field name made lowercase.
    periodo = models.CharField(db_column='Periodo', max_length=50)  # Field name made lowercase.
    id_medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='ID_Medico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Escala_Medico_Plantao'


class Especialidade(models.Model):
    id_especialidade = models.IntegerField(db_column='ID_Especialidade', primary_key=True)  # Field name made lowercase.
    nome_especialidade = models.CharField(db_column='Nome_Especialidade', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Especialidade'


class EstadoCivil(models.Model):
    id_estado_civil = models.IntegerField(db_column='ID_Estado_Civil', primary_key=True)  # Field name made lowercase.
    estado_civil = models.CharField(db_column='Estado_Civil', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Estado_Civil'


class Estoque(models.Model):
    id_estoque = models.IntegerField(db_column='ID_Estoque', primary_key=True)  # Field name made lowercase.
    id_produto = models.IntegerField(db_column='ID_Produto')  # Field name made lowercase.
    lote = models.CharField(db_column='Lote', max_length=50)  # Field name made lowercase.
    valor = models.CharField(db_column='Valor', max_length=50)  # Field name made lowercase.
    data_entrada = models.DateField(db_column='Data_Entrada')  # Field name made lowercase.
    data_saida = models.DateField(db_column='Data_Saida', blank=True, null=True)  # Field name made lowercase.
    id_nota_fiscal = models.ForeignKey('NotaFiscal', models.DO_NOTHING, db_column='ID_Nota_Fiscal')  # Field name made lowercase.
    id_pedido_compra = models.ForeignKey('PedidoCompra', models.DO_NOTHING, db_column='ID_Pedido_Compra')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Estoque'


class Ferias(models.Model):
    id_ferias = models.IntegerField(db_column='ID_Ferias', primary_key=True)  # Field name made lowercase.
    data_inicio = models.DateField(db_column='Data_Inicio')  # Field name made lowercase.
    data_fim = models.DateField(db_column='Data_Fim')  # Field name made lowercase.
    periodo_aquisitivo = models.CharField(db_column='Periodo_Aquisitivo', max_length=50)  # Field name made lowercase.
    gozado = models.IntegerField(db_column='Gozado')  # Field name made lowercase.
    valor_ferias = models.DecimalField(db_column='Valor_Ferias', max_digits=8, decimal_places=2)  # Field name made lowercase.
    id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='ID_Funcionario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ferias'


class Fornecedor(models.Model):
    id_fornecedor = models.IntegerField(db_column='ID_Fornecedor', primary_key=True)  # Field name made lowercase.
    nome_fornecedor = models.CharField(db_column='Nome_Fornecedor', max_length=50)  # Field name made lowercase.
    end_rua = models.CharField(db_column='End_Rua', max_length=50)  # Field name made lowercase.
    end_num = models.IntegerField(db_column='End_Num')  # Field name made lowercase.
    end_cep = models.CharField(db_column='End_CEP', max_length=50)  # Field name made lowercase.
    end_complemento = models.CharField(db_column='End_Complemento', max_length=50)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=50)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=50)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fornecedor'


class Frasco(models.Model):
    id_frasco = models.IntegerField(db_column='ID_Frasco', primary_key=True)  # Field name made lowercase.
    quantidade_gotas_saida = models.IntegerField(db_column='Quantidade_Gotas_Saida')  # Field name made lowercase.
    id_lote_medicamento_entrada = models.ForeignKey('LoteMedicamentoEntrada', models.DO_NOTHING, db_column='ID_Lote_Medicamento_Entrada')  # Field name made lowercase.
    id_setor = models.ForeignKey('Setor', models.DO_NOTHING, db_column='ID_Setor')  # Field name made lowercase.
    id_saida_medicamento = models.ForeignKey('SaidaMedicamento', models.DO_NOTHING, db_column='ID_Saida_Medicamento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Frasco'


class Funcionario(models.Model):
    id_funcionario = models.IntegerField(db_column='ID_Funcionario', primary_key=True)  # Field name made lowercase.
    data_admissao = models.DateField(db_column='Data_Admissao')  # Field name made lowercase.
    id_situacao = models.ForeignKey('Situacao', models.DO_NOTHING, db_column='ID_Situacao')  # Field name made lowercase.
    conta_cef = models.CharField(db_column='Conta_CEF', max_length=50)  # Field name made lowercase.
    carga_horaria_tipo = models.CharField(db_column='Carga_Horaria_Tipo', max_length=50)  # Field name made lowercase.
    carga_horaria_intervalo = models.TimeField(db_column='Carga_Horaria_Intervalo')  # Field name made lowercase.
    pis = models.IntegerField(db_column='PIS')  # Field name made lowercase.
    ctps_numero = models.BigIntegerField(db_column='CTPS_Numero')  # Field name made lowercase.
    ctps_serie = models.BigIntegerField(db_column='CTPS_Serie')  # Field name made lowercase.
    id_sindicato = models.ForeignKey('Sindicato', models.DO_NOTHING, db_column='ID_Sindicato')  # Field name made lowercase.
    id_cargo_funcionario = models.ForeignKey(CargoFuncionario, models.DO_NOTHING, db_column='ID_Cargo_Funcionario')  # Field name made lowercase.
    id_pcd = models.ForeignKey('PessoaComDeficiencia', models.DO_NOTHING, db_column='ID_PCD', blank=True, null=True)  # Field name made lowercase.
    possui_epi = models.IntegerField(db_column='Possui_EPI')  # Field name made lowercase.
    vacina_hepatite = models.DateField(db_column='Vacina_Hepatite', blank=True, null=True)  # Field name made lowercase.
    vacina_triplice_viral = models.DateField(db_column='Vacina_Triplice_Viral', blank=True, null=True)  # Field name made lowercase.
    vacina_duplo_adulto = models.DateField(db_column='Vacina_Duplo_Adulto', blank=True, null=True)  # Field name made lowercase.
    valor_max_emprestimo = models.IntegerField(db_column='Valor_Max_Emprestimo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Funcionario'


class Glosa(models.Model):
    id_glosa = models.IntegerField(db_column='ID_Glosa', primary_key=True)  # Field name made lowercase.
    valor_glosado = models.DecimalField(db_column='Valor_Glosado', max_digits=8, decimal_places=2)  # Field name made lowercase.
    filestream_justificativa_convenio = models.CharField(db_column='FILESTREAM_Justificativa_Conv�nio', max_length=200)  # Field name made lowercase.
    filestream_justificativa_aicp = models.CharField(db_column='FILESTREAM_Justificativa_AICP', max_length=200, blank=True, null=True)  # Field name made lowercase.
    justificativa_glosa_aceita = models.IntegerField(db_column='Justificativa_Glosa_Aceita', blank=True, null=True)  # Field name made lowercase.
    data_prazo_resposta = models.DateField(db_column='Data_Prazo_Resposta')  # Field name made lowercase.
    glosa_definitiva = models.IntegerField(db_column='Glosa_Definitiva', blank=True, null=True)  # Field name made lowercase.
    id_pag_convenio_medicamento = models.ForeignKey('PagConvenioMedicamento', models.DO_NOTHING, db_column='ID_Pag_Convenio_Medicamento', blank=True, null=True)  # Field name made lowercase.
    id_pag_convenio_dieta = models.ForeignKey('PagConvenioDieta', models.DO_NOTHING, db_column='ID_Pag_Convenio_Dieta', blank=True, null=True)  # Field name made lowercase.
    id_pag_convenio_hd = models.ForeignKey('PagConvenioHd', models.DO_NOTHING, db_column='ID_Pag_Convenio_HD', blank=True, null=True)  # Field name made lowercase.
    id_pag_convenio_internacao = models.ForeignKey('PagConvenioInternacao', models.DO_NOTHING, db_column='ID_Pag_Convenio_Internacao', blank=True, null=True)  # Field name made lowercase.
    id_pag_convenio_consulta = models.ForeignKey('PagConvenioConsulta', models.DO_NOTHING, db_column='ID_Pag_Convenio_Consulta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Glosa'


class GrauInstrucao(models.Model):
    id_grau_instrucao = models.IntegerField(db_column='ID_Grau_Instrucao', primary_key=True)  # Field name made lowercase.
    nome_grau_instrucao = models.CharField(db_column='Nome_Grau_Instrucao', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Grau_Instrucao'


class GrupoFarmacologico(models.Model):
    id_grupo_farmacologico = models.IntegerField(db_column='ID_Grupo_Farmacologico', primary_key=True)  # Field name made lowercase.
    nome_grupo_farmacologico = models.CharField(db_column='Nome_Grupo_Farmacologico', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Grupo_Farmacologico'


class HistoricoAtestado(models.Model):
    id_atestado = models.IntegerField(db_column='ID_Atestado', primary_key=True)  # Field name made lowercase.
    filestream_atestado = models.CharField(db_column='FILESTREAM_Atestado', max_length=200)  # Field name made lowercase.
    data_atestado = models.DateField(db_column='Data_Atestado')  # Field name made lowercase.
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='ID_Paciente')  # Field name made lowercase.
    id_medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='ID_Medico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Historico_Atestado'


class HistoricoDieta(models.Model):
    id_dieta = models.IntegerField(db_column='ID_Dieta', primary_key=True)  # Field name made lowercase.
    data_dieta = models.DateField(db_column='Data_Dieta')  # Field name made lowercase.
    filestream_dieta = models.CharField(db_column='FILESTREAM_Dieta', max_length=200)  # Field name made lowercase.
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='ID_Paciente')  # Field name made lowercase.
    id_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='ID_Funcionario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Historico_Dieta'


class HistoricoExame(models.Model):
    id_historico_exame = models.IntegerField(db_column='ID_Historico_Exame', primary_key=True)  # Field name made lowercase.
    data_exame = models.DateField(db_column='Data_Exame')  # Field name made lowercase.
    filestream_historico_exame = models.CharField(db_column='FILESTREAM_Historico_Exame', max_length=200)  # Field name made lowercase.
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='ID_Paciente')  # Field name made lowercase.
    id_medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='ID_Medico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Historico_Exame'


class HistoricoMedicoResponsavel(models.Model):
    id_atendimento_historico_medico_responsavel = models.IntegerField(db_column='ID_Atendimento_Historico_Medico_Responsavel', primary_key=True)  # Field name made lowercase.
    data_inicio = models.DateField(db_column='Data_Inicio')  # Field name made lowercase.
    data_fim = models.DateField(db_column='Data_Fim', blank=True, null=True)  # Field name made lowercase.
    id_cadastro_internacao = models.ForeignKey(CadastroInternacao, models.DO_NOTHING, db_column='ID_Cadastro_Internacao')  # Field name made lowercase.
    id_medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='ID_Medico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Historico_Medico_Responsavel'


class HistoricoPrescricao(models.Model):
    id_historico_prescricao = models.IntegerField(db_column='ID_Historico_Prescricao', primary_key=True)  # Field name made lowercase.
    filestream_prescricao = models.CharField(db_column='FILESTREAM_Prescricao', max_length=200)  # Field name made lowercase.
    data_historico_prescricao = models.DateField(db_column='Data_Historico_Prescricao')  # Field name made lowercase.
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='ID_Paciente')  # Field name made lowercase.
    id_medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='ID_Medico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Historico_Prescricao'


class HoraExtra(models.Model):
    id_hora_extra = models.IntegerField(db_column='ID_Hora_Extra', primary_key=True)  # Field name made lowercase.
    mes_hora_extra = models.CharField(db_column='Mes_Hora_Extra', max_length=2)  # Field name made lowercase.
    ano_hora_extra = models.CharField(db_column='Ano_Hora_Extra', max_length=4)  # Field name made lowercase.
    quantidade_hora_extra = models.IntegerField(db_column='Quantidade_Hora_Extra')  # Field name made lowercase.
    justificativa = models.CharField(db_column='Justificativa', max_length=50)  # Field name made lowercase.
    id_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='ID_Funcionario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hora_Extra'


class ItensNotaFiscal(models.Model):
    id_itens_nota_fiscal = models.IntegerField(db_column='ID_Itens_Nota_Fiscal', primary_key=True)  # Field name made lowercase.
    id_nota_fiscal = models.ForeignKey('NotaFiscal', models.DO_NOTHING, db_column='ID_Nota_Fiscal')  # Field name made lowercase.
    id_pag_convenio_medicamento = models.ForeignKey('PagConvenioMedicamento', models.DO_NOTHING, db_column='ID_Pag_Convenio_Medicamento', blank=True, null=True)  # Field name made lowercase.
    id_pag_convenio_dieta = models.ForeignKey('PagConvenioDieta', models.DO_NOTHING, db_column='ID_Pag_Convenio_Dieta', blank=True, null=True)  # Field name made lowercase.
    id_pag_convenio_hd = models.ForeignKey('PagConvenioHd', models.DO_NOTHING, db_column='ID_Pag_Convenio_HD', blank=True, null=True)  # Field name made lowercase.
    id_pag_convenio_internacao = models.ForeignKey('PagConvenioInternacao', models.DO_NOTHING, db_column='ID_Pag_Convenio_Internacao', blank=True, null=True)  # Field name made lowercase.
    id_pag_convenio_consulta = models.ForeignKey('PagConvenioConsulta', models.DO_NOTHING, db_column='ID_Pag_Convenio_Consulta', blank=True, null=True)  # Field name made lowercase.
    id_pag_particular_consulta = models.ForeignKey('PagParticularConsulta', models.DO_NOTHING, db_column='ID_Pag_Particular_Consulta', blank=True, null=True)  # Field name made lowercase.
    id_pag_particular_internacao = models.ForeignKey('PagParticularInternacao', models.DO_NOTHING, db_column='ID_Pag_Particular_Internacao', blank=True, null=True)  # Field name made lowercase.
    id_pag_particular_med = models.ForeignKey('PagParticularMed', models.DO_NOTHING, db_column='ID_Pag_Particular_Med', blank=True, null=True)  # Field name made lowercase.
    id_pag_particular_dieta = models.ForeignKey('PagParticularDieta', models.DO_NOTHING, db_column='ID_Pag_Particular_Dieta', blank=True, null=True)  # Field name made lowercase.
    id_pag_particular_hd = models.ForeignKey('PagParticularHd', models.DO_NOTHING, db_column='ID_Pag_Particular_HD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Itens_Nota_Fiscal'


class Leito(models.Model):
    id_leito = models.IntegerField(db_column='ID_Leito', primary_key=True)  # Field name made lowercase.
    num_leito = models.IntegerField(db_column='Num_leito')  # Field name made lowercase.
    id_setor = models.ForeignKey('Setor', models.DO_NOTHING, db_column='ID_Setor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Leito'


class LoteMedicamentoEntrada(models.Model):
    id_lote_medicamento_entrada = models.IntegerField(db_column='ID_Lote_Medicamento_Entrada', primary_key=True)  # Field name made lowercase.
    lote = models.IntegerField(db_column='Lote')  # Field name made lowercase.
    data_entrada = models.DateField(db_column='Data_Entrada')  # Field name made lowercase.
    data_validade = models.DateField(db_column='Data_Validade')  # Field name made lowercase.
    data_fabricacao = models.DateField(db_column='Data_Fabricacao')  # Field name made lowercase.
    valor_compra_medicamento = models.DecimalField(db_column='Valor_Compra_Medicamento', max_digits=8, decimal_places=2)  # Field name made lowercase.
    id_medicamento_cadastro = models.ForeignKey('MedicamentoCadastro', models.DO_NOTHING, db_column='ID_Medicamento_Cadastro')  # Field name made lowercase.
    id_nota_fiscal = models.ForeignKey('NotaFiscal', models.DO_NOTHING, db_column='ID_Nota_Fiscal')  # Field name made lowercase.
    id_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='ID_Funcionario')  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lote_Medicamento_Entrada'


class LotePagamento(models.Model):
    id_lote_pagamento = models.IntegerField(db_column='ID_Lote_Pagamento', primary_key=True)  # Field name made lowercase.
    id_convenio = models.ForeignKey(Convenio, models.DO_NOTHING, db_column='ID_Convenio')  # Field name made lowercase.
    id_nota_fiscal = models.ForeignKey('NotaFiscal', models.DO_NOTHING, db_column='ID_Nota_Fiscal')  # Field name made lowercase.
    lote_convenio = models.CharField(db_column='Lote_Convenio', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lote_Pagamento'


class MedicamentoCadastro(models.Model):
    id_medicamento_cadastro = models.IntegerField(db_column='ID_Medicamento_Cadastro', primary_key=True)  # Field name made lowercase.
    nome_medicamento = models.CharField(db_column='Nome_Medicamento', max_length=50)  # Field name made lowercase.
    laboratorio = models.CharField(db_column='Laboratorio', max_length=50)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=50)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=50)  # Field name made lowercase.
    quantidade_gotas = models.IntegerField(db_column='Quantidade_Gotas', blank=True, null=True)  # Field name made lowercase.
    id_nome_sal = models.ForeignKey('NomeSal', models.DO_NOTHING, db_column='ID_Nome_SAL')  # Field name made lowercase.
    id_tipo_medicamento = models.ForeignKey('TipoMedicamento', models.DO_NOTHING, db_column='ID_Tipo_Medicamento')  # Field name made lowercase.
    id_codigo_brasindice = models.ForeignKey(CodigoBrasindice, models.DO_NOTHING, db_column='ID_Codigo_Brasindice')  # Field name made lowercase.
    id_grupo_farmacologico = models.ForeignKey(GrupoFarmacologico, models.DO_NOTHING, db_column='ID_Grupo_Farmacologico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Medicamento_Cadastro'


class MedicamentoEstoque(models.Model):
    id_medicamento_estoque = models.IntegerField(db_column='ID_Medicamento_Estoque', primary_key=True)  # Field name made lowercase.
    quantidade_total = models.IntegerField(db_column='Quantidade_Total')  # Field name made lowercase.
    quantidade_farmacia = models.IntegerField(db_column='Quantidade_Farmacia')  # Field name made lowercase.
    id_medicamento_cadastro = models.ForeignKey(MedicamentoCadastro, models.DO_NOTHING, db_column='ID_Medicamento_Cadastro')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Medicamento_Estoque'


class MedicamentoFamilia(models.Model):
    id_medicamento_familia = models.IntegerField(db_column='ID_Medicamento_Familia', primary_key=True)  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade')  # Field name made lowercase.
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='ID_Paciente')  # Field name made lowercase.
    id_medicamento_cadastro = models.ForeignKey(MedicamentoCadastro, models.DO_NOTHING, db_column='ID_Medicamento_Cadastro')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Medicamento_Familia'


class Medico(models.Model):
    id_medico = models.IntegerField(db_column='ID_Medico', primary_key=True)  # Field name made lowercase
    crm = models.CharField(db_column='CRM', max_length=50)  # Field name made lowercase.
    id_especialidade = models.ForeignKey(Especialidade, models.DO_NOTHING, db_column='ID_Especialidade')  # Field name made lowercase.
    senha = models.CharField(db_column='senha', max_length=100)
    class Meta:
        managed = False
        db_table = 'Medico'


class MedicoConvenio(models.Model):
    id_medico_convenio = models.IntegerField(db_column='ID_Medico_Convenio', primary_key=True)  # Field name made lowercase.
    id_medico = models.ForeignKey(Medico, models.DO_NOTHING, db_column='ID_Medico')  # Field name made lowercase.
    id_convenio = models.ForeignKey(Convenio, models.DO_NOTHING, db_column='ID_Convenio')  # Field name made lowercase.
    valor_consulta_especial = models.DecimalField(db_column='Valor_Consulta_Especial', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Medico_Convenio'


class MedidaCorretiva(models.Model):
    id_medida_corretiva = models.IntegerField(db_column='ID_Medida_Corretiva', primary_key=True)  # Field name made lowercase.
    fato_observado = models.CharField(db_column='Fato_Observado', max_length=200)  # Field name made lowercase.
    data_medida_corretiva = models.DateField(db_column='Data_Medida_Corretiva')  # Field name made lowercase.
    id_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='ID_Funcionario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Medida_Corretiva'


class MotivoSaidaPilula(models.Model):
    id_motivo_saida_pilula = models.IntegerField(db_column='ID_Motivo_Saida_Pilula', primary_key=True)  # Field name made lowercase.
    nome_motivo_saida_pilula = models.CharField(db_column='Nome_Motivo_Saida_Pilula', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Motivo_Saida_Pilula'


class NomeSal(models.Model):
    id_nome_sal = models.IntegerField(db_column='ID_Nome_SAL', primary_key=True)  # Field name made lowercase.
    descricao_sal = models.CharField(db_column='Descricao_SAL', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nome_SAL'

class NotaFiscal(models.Model):
    id_nota_fiscal = models.CharField(db_column='ID_Nota_Fiscal', primary_key=True, max_length=50)  # Field name made lowercase.
    mes_competencia = models.CharField(db_column='Mes_Competencia', max_length=2)  # Field name made lowercase.
    ano_competencia = models.CharField(db_column='Ano_Competencia', max_length=4)  # Field name made lowercase.
    id_banco = models.ForeignKey(Banco, models.DO_NOTHING, db_column='ID_Banco')  # Field name made lowercase.
    razao_social = models.CharField(db_column='Razao_Social', max_length=50)  # Field name made lowercase.
    data_expedicao = models.DateField(db_column='Data_Expedicao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nota_Fiscal'


class Paciente(models.Model):
    id_paciente = models.IntegerField(db_column='ID_Paciente', primary_key=True)  # Field name made lowercase.
    n_carteira = models.CharField(db_column='N_Carteira', max_length=50)  # Field name made lowercase.
    validade_carteira = models.DateField(db_column='Validade_Carteira')  # Field name made lowercase.
    restricao_internacao = models.IntegerField(db_column='Restricao_Internacao')  # Field name made lowercase.
    motivo_restricao = models.CharField(db_column='Motivo_Restricao', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nome_pai = models.CharField(db_column='Nome_Pai', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nome_mae = models.CharField(db_column='Nome_Mae', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_convenio = models.ForeignKey(Convenio, models.DO_NOTHING, db_column='ID_Convenio', blank=True, null=True)  # Field name made lowercase.
    procedencia = models.CharField(db_column='Procedencia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    medicamento_familiar = models.IntegerField(db_column='Medicamento_Familiar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Paciente'


class PagConvenioConsulta(models.Model):
    id_pag_convenio_consulta = models.IntegerField(db_column='ID_Pag_Convenio_Consulta', primary_key=True)  # Field name made lowercase.
    data_fim_resposta = models.DateField(db_column='Data_Fim_Resposta', blank=True, null=True)  # Field name made lowercase.
    data_fim_pedido = models.DateField(db_column='Data_Fim_Pedido', blank=True, null=True)  # Field name made lowercase.
    data_pedido_autorizacao = models.DateField(db_column='Data_Pedido_Autorizacao', blank=True, null=True)  # Field name made lowercase.
    data_resposta = models.DateField(db_column='Data_Resposta', blank=True, null=True)  # Field name made lowercase.
    data_estimativa_resposta = models.DateField(db_column='Data_Estimativa_Resposta', blank=True, null=True)  # Field name made lowercase.
    id_tipo_status_autorizacao = models.ForeignKey('TipoStatusAutorizacao', models.DO_NOTHING, db_column='ID_Tipo_Status_Autorizacao')  # Field name made lowercase.
    id_tipo_autorizacao = models.ForeignKey('TipoAutorizacao', models.DO_NOTHING, db_column='ID_Tipo_Autorizacao')  # Field name made lowercase.
    data_previsao_pag = models.DateField(db_column='Data_Previsao_Pag', blank=True, null=True)  # Field name made lowercase.
    data_pag = models.DateField(db_column='Data_Pag', blank=True, null=True)  # Field name made lowercase.
    valor_convenio = models.DecimalField(db_column='Valor_Convenio', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    id_consulta = models.ForeignKey(Consulta, models.DO_NOTHING, db_column='ID_Consulta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pag_Convenio_Consulta'


class PagConvenioDieta(models.Model):
    id_pag_convenio_dieta = models.IntegerField(db_column='ID_Pag_Convenio_Dieta', primary_key=True)  # Field name made lowercase.
    data_fim_resposta = models.DateField(db_column='Data_Fim_Resposta', blank=True, null=True)  # Field name made lowercase.
    data_fim_pedido = models.DateField(db_column='Data_Fim_Pedido', blank=True, null=True)  # Field name made lowercase.
    id_dieta = models.ForeignKey(HistoricoDieta, models.DO_NOTHING, db_column='ID_Dieta')  # Field name made lowercase.
    data_pedido_autorizacao = models.DateField(db_column='Data_Pedido_Autorizacao', blank=True, null=True)  # Field name made lowercase.
    data_resposta = models.DateField(db_column='Data_Resposta', blank=True, null=True)  # Field name made lowercase.
    data_estimativa_resposta = models.DateField(db_column='Data_Estimativa_Resposta', blank=True, null=True)  # Field name made lowercase.
    id_tipo_status_autorizacao = models.ForeignKey('TipoStatusAutorizacao', models.DO_NOTHING, db_column='ID_Tipo_Status_Autorizacao')  # Field name made lowercase.
    id_tipo_autorizacao = models.ForeignKey('TipoAutorizacao', models.DO_NOTHING, db_column='ID_Tipo_Autorizacao')  # Field name made lowercase.
    data_previsao_pag = models.DateField(db_column='Data_Previsao_Pag', blank=True, null=True)  # Field name made lowercase.
    date_pag = models.DateField(db_column='Date_Pag', blank=True, null=True)  # Field name made lowercase.
    valor_convenio = models.DecimalField(db_column='Valor_Convenio', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pag_Convenio_Dieta'


class PagConvenioHd(models.Model):
    id_pag_convenio_hd = models.IntegerField(db_column='ID_Pag_Convenio_HD', primary_key=True)  # Field name made lowercase.
    qtd_dias_pedidos = models.IntegerField(db_column='Qtd_Dias_Pedidos')  # Field name made lowercase.
    data_fim_resposta = models.DateField(db_column='Data_Fim_Resposta', blank=True, null=True)  # Field name made lowercase.
    data_fim_pedido = models.DateField(db_column='Data_Fim_Pedido', blank=True, null=True)  # Field name made lowercase.
    data_pedido_autorizacao = models.DateField(db_column='Data_Pedido_Autorizacao', blank=True, null=True)  # Field name made lowercase.
    data_resposta = models.DateField(db_column='Data_Resposta', blank=True, null=True)  # Field name made lowercase.
    data_estimativa_resposta = models.DateField(db_column='Data_Estimativa_Resposta', blank=True, null=True)  # Field name made lowercase.
    id_cadastro_hd = models.ForeignKey(CadastroHd, models.DO_NOTHING, db_column='ID_Cadastro_HD')  # Field name made lowercase.
    id_tipo_status_autorizacao = models.ForeignKey('TipoStatusAutorizacao', models.DO_NOTHING, db_column='ID_Tipo_Status_Autorizacao')  # Field name made lowercase.
    id_tipo_autorizacao = models.ForeignKey('TipoAutorizacao', models.DO_NOTHING, db_column='ID_Tipo_Autorizacao')  # Field name made lowercase.
    qtd_dias_autorizados = models.IntegerField(db_column='Qtd_Dias_Autorizados', blank=True, null=True)  # Field name made lowercase.
    data_previsao_pag = models.DateField(db_column='Data_Previsao_Pag', blank=True, null=True)  # Field name made lowercase.
    data_pag = models.DateField(db_column='Data_Pag', blank=True, null=True)  # Field name made lowercase.
    valor_convenio = models.DecimalField(db_column='Valor_Convenio', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pag_Convenio_HD'


class PagConvenioInternacao(models.Model):
    id_pag_convenio_internacao = models.IntegerField(db_column='ID_Pag_Convenio_Internacao', primary_key=True)  # Field name made lowercase.
    data_inicio_periodo = models.DateField(db_column='Data_Inicio_Periodo', blank=True, null=True)  # Field name made lowercase.
    data_final_periodo = models.DateField(db_column='Data_Final_Periodo', blank=True, null=True)  # Field name made lowercase.
    data_final_pedido = models.DateField(db_column='Data_Final_Pedido', blank=True, null=True)  # Field name made lowercase.
    data_pedido_autorizacao = models.DateField(db_column='Data_Pedido_Autorizacao', blank=True, null=True)  # Field name made lowercase.
    data_resposta = models.DateField(db_column='Data_Resposta', blank=True, null=True)  # Field name made lowercase.
    data_estimativa_resposta = models.DateField(db_column='Data_Estimativa_Resposta', blank=True, null=True)  # Field name made lowercase.
    id_cadastro_internacao = models.ForeignKey(CadastroInternacao, models.DO_NOTHING, db_column='ID_Cadastro_Internacao')  # Field name made lowercase.
    id_tipo_status_autorizacao = models.ForeignKey('TipoStatusAutorizacao', models.DO_NOTHING, db_column='ID_Tipo_Status_Autorizacao')  # Field name made lowercase.
    id_tipo_autorizacao = models.ForeignKey('TipoAutorizacao', models.DO_NOTHING, db_column='ID_Tipo_Autorizacao')  # Field name made lowercase.
    data_previsao_pag = models.DateField(db_column='Data_Previsao_Pag', blank=True, null=True)  # Field name made lowercase.
    data_pag = models.DateField(db_column='Data_Pag', blank=True, null=True)  # Field name made lowercase.
    valor_convenio = models.DecimalField(db_column='Valor_Convenio', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pag_Convenio_Internacao'


class PagConvenioMedicamento(models.Model):
    id_pag_convenio_medicamento = models.IntegerField(db_column='ID_Pag_Convenio_Medicamento', primary_key=True)  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade')  # Field name made lowercase.
    id_prescricao_medicamento = models.ForeignKey('PrescricaoMedicamento', models.DO_NOTHING, db_column='ID_Prescricao_Medicamento')  # Field name made lowercase.
    data_pedido_autorizacao = models.DateField(db_column='Data_Pedido_Autorizacao', blank=True, null=True)  # Field name made lowercase.
    data_resposta = models.DateField(db_column='Data_Resposta', blank=True, null=True)  # Field name made lowercase.
    data_estimativa_resposta = models.DateField(db_column='Data_Estimativa_Resposta', blank=True, null=True)  # Field name made lowercase.
    id_tipo_status_autorizacao = models.ForeignKey('TipoStatusAutorizacao', models.DO_NOTHING, db_column='ID_Tipo_Status_Autorizacao')  # Field name made lowercase.
    id_tipo_autorizacao = models.ForeignKey('TipoAutorizacao', models.DO_NOTHING, db_column='ID_Tipo_Autorizacao')  # Field name made lowercase.
    data_previsao_pag = models.DateField(db_column='Data_Previsao_Pag', blank=True, null=True)  # Field name made lowercase.
    data_pag = models.DateField(db_column='Data_Pag', blank=True, null=True)  # Field name made lowercase.
    valor_convenio = models.DecimalField(db_column='Valor_Convenio', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pag_Convenio_Medicamento'


class PagParticularConsulta(models.Model):
    id_pag_particular_consulta = models.IntegerField(db_column='ID_Pag_Particular_Consulta', primary_key=True)  # Field name made lowercase.
    data_previsao_pag_consulta = models.DateField(db_column='Data_Previsao_Pag_Consulta', blank=True, null=True)  # Field name made lowercase.
    data_pag_consulta = models.DateField(db_column='Data_Pag_Consulta', blank=True, null=True)  # Field name made lowercase.
    valor_particular_consulta = models.DecimalField(db_column='Valor_Particular_Consulta', max_digits=8, decimal_places=2)  # Field name made lowercase.
    id_consulta = models.ForeignKey(Consulta, models.DO_NOTHING, db_column='ID_Consulta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pag_Particular_Consulta'


class PagParticularDieta(models.Model):
    id_pag_particular_dieta = models.IntegerField(db_column='ID_Pag_Particular_Dieta', primary_key=True)  # Field name made lowercase.
    data_previsao_pag_dieta = models.DateField(db_column='Data_Previsao_Pag_Dieta', blank=True, null=True)  # Field name made lowercase.
    data_pag_particular_dieta = models.DateField(db_column='Data_Pag_Particular_Dieta', blank=True, null=True)  # Field name made lowercase.
    valor_pag_particular_dieta = models.DecimalField(db_column='Valor_Pag_Particular_Dieta', max_digits=8, decimal_places=2)  # Field name made lowercase.
    id_dieta = models.ForeignKey(HistoricoDieta, models.DO_NOTHING, db_column='ID_Dieta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pag_Particular_Dieta'


class PagParticularHd(models.Model):
    id_pag_particular_hd = models.IntegerField(db_column='ID_Pag_Particular_HD', primary_key=True)  # Field name made lowercase.
    data_previsao_pag_hd = models.DateField(db_column='Data_Previsao_Pag_HD', blank=True, null=True)  # Field name made lowercase.
    data_pag_hd = models.DateField(db_column='Data_Pag_HD', blank=True, null=True)  # Field name made lowercase.
    valor_particular_hd = models.DecimalField(db_column='Valor_Particular_HD', max_digits=8, decimal_places=2)  # Field name made lowercase.
    id_cadastro_hd = models.ForeignKey(CadastroHd, models.DO_NOTHING, db_column='ID_Cadastro_HD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pag_Particular_HD'


class PagParticularInternacao(models.Model):
    id_pag_particular_internacao = models.IntegerField(db_column='ID_Pag_Particular_Internacao', primary_key=True)  # Field name made lowercase.
    data_previsao = models.DateField(db_column='Data_Previsao', blank=True, null=True)  # Field name made lowercase.
    data_pag = models.DateField(db_column='Data_Pag', blank=True, null=True)  # Field name made lowercase.
    valor_particular = models.DecimalField(db_column='Valor_Particular', max_digits=8, decimal_places=2)  # Field name made lowercase.
    id_cadastro_internacao = models.ForeignKey(CadastroInternacao, models.DO_NOTHING, db_column='ID_Cadastro_Internacao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pag_Particular_Internacao'


class PagParticularMed(models.Model):
    id_pag_particular_med = models.IntegerField(db_column='ID_Pag_Particular_Med', primary_key=True)  # Field name made lowercase.
    data_previsao_pag = models.DateField(db_column='Data_Previsao_Pag', blank=True, null=True)  # Field name made lowercase.
    data_pag = models.DateField(db_column='Data_Pag', blank=True, null=True)  # Field name made lowercase.
    valor_particular = models.DecimalField(db_column='Valor_Particular', max_digits=8, decimal_places=2)  # Field name made lowercase.
    id_prescricao_medicamento = models.ForeignKey('PrescricaoMedicamento', models.DO_NOTHING, db_column='ID_Prescricao_Medicamento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pag_Particular_Med'


class PedidoCompra(models.Model):
    id_pedido_compra = models.IntegerField(db_column='ID_Pedido_Compra', primary_key=True)  # Field name made lowercase.
    id_cadastro_produto = models.ForeignKey(CadastroProduto, models.DO_NOTHING, db_column='ID_Cadastro_Produto')  # Field name made lowercase.
    autorizado = models.IntegerField(db_column='Autorizado')  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=50)  # Field name made lowercase.
    numero_pedido = models.IntegerField(db_column='Numero_Pedido')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pedido_Compra'


class Pessoa(models.Model):
    id_cpf = models.CharField(db_column='ID_CPF', primary_key=True, max_length=20)  # Field name made lowercase.
    nome_pessoa = models.CharField(db_column='Nome_Pessoa', max_length=200)  # Field name made lowercase.
    sexo_masculino = models.IntegerField(db_column='Sexo_Masculino')  # Field name made lowercase.
    falecido = models.IntegerField(db_column='Falecido')  # Field name made lowercase.
    data_nascimento = models.DateField(db_column='Data_Nascimento', blank=True, null=True)  # Field name made lowercase.
    telefone_residencial = models.CharField(db_column='Telefone_Residencial', max_length=20, blank=True, null=True)  # Field name made lowercase.
    telefone_celular = models.CharField(db_column='Telefone_Celular', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rg = models.CharField(db_column='RG', max_length=20)  # Field name made lowercase.
    rg_orgao_expeditor = models.CharField(db_column='RG_Orgao_Expeditor', max_length=50)  # Field name made lowercase.
    rg_uf = models.CharField(db_column='RG_UF', max_length=2)  # Field name made lowercase.
    rg_data_emissao = models.DateField(db_column='RG_Data_Emissao')  # Field name made lowercase.
    naturalidade = models.CharField(db_column='Naturalidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nacionalidade = models.CharField(db_column='Nacionalidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    profissao = models.CharField(db_column='Profissao', max_length=50)  # Field name made lowercase.
    foto = models.CharField(db_column='Foto', max_length=200)  # Field name made lowercase.
    conjuge = models.CharField(db_column='Conjuge', max_length=200)  # Field name made lowercase.
    endereco_rua = models.CharField(db_column='Endereco_Rua', max_length=100)  # Field name made lowercase.
    endereco_complemento = models.IntegerField(db_column='Endereco_Complemento')  # Field name made lowercase.
    endereco_cep = models.CharField(db_column='Endereco_CEP', max_length=50)  # Field name made lowercase.
    endereco_estado = models.CharField(db_column='Endereco_Estado', max_length=100)  # Field name made lowercase.
    endereco_cidade = models.CharField(db_column='Endereco_Cidade', max_length=100)  # Field name made lowercase.
    endereco_bairro = models.CharField(db_column='Endereco_Bairro', max_length=100)  # Field name made lowercase.
    id_estado_civil = models.ForeignKey(EstadoCivil, models.DO_NOTHING, db_column='ID_Estado_Civil')  # Field name made lowercase.
    id_grau_instrucao = models.ForeignKey(GrauInstrucao, models.DO_NOTHING, db_column='ID_Grau_Instrucao')  # Field name made lowercase.
    id_paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='ID_Paciente', blank=True, null=True)  # Field name made lowercase.
    id_medico = models.ForeignKey(Medico, models.DO_NOTHING, db_column='ID_Medico', blank=True, null=True)  # Field name made lowercase.
    id_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='ID_Funcionario', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'Pessoa'


class PessoaComDeficiencia(models.Model):
    id_pcd = models.IntegerField(db_column='ID_PCD', primary_key=True)  # Field name made lowercase.
    tipo_deficiencia = models.CharField(db_column='Tipo_Deficiencia', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pessoa_Com_Deficiencia'


class Pilula(models.Model):
    id_pilula = models.IntegerField(db_column='ID_Pilula', primary_key=True)  # Field name made lowercase.
    etiqueta = models.IntegerField(db_column='Etiqueta')  # Field name made lowercase.
    id_lote_medicamento_entrada = models.ForeignKey(LoteMedicamentoEntrada, models.DO_NOTHING, db_column='ID_Lote_Medicamento_Entrada')  # Field name made lowercase.
    id_setor = models.ForeignKey('Setor', models.DO_NOTHING, db_column='ID_Setor')  # Field name made lowercase.
    id_saida_medicamento = models.ForeignKey('SaidaMedicamento', models.DO_NOTHING, db_column='ID_Saida_Medicamento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pilula'


class PrescricaoMedicamento(models.Model):
    id_prescricao_medicamento = models.IntegerField(db_column='ID_Prescricao_Medicamento', primary_key=True)  # Field name made lowercase.
    quantidade_por_dia = models.IntegerField(db_column='Quantidade_por_dia')  # Field name made lowercase.
    periodo_inicio = models.DateTimeField(db_column='Periodo_inicio')  # Field name made lowercase.
    periodo_fim = models.DateTimeField(db_column='Periodo_fim')  # Field name made lowercase.
    id_medicamento_cadastro = models.ForeignKey(MedicamentoCadastro, models.DO_NOTHING, db_column='ID_Medicamento_Cadastro')  # Field name made lowercase.
    id_historico_prescricao = models.ForeignKey(HistoricoPrescricao, models.DO_NOTHING, db_column='ID_Historico_Prescricao')  # Field name made lowercase.
    dosagem = models.IntegerField(db_column='Dosagem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Prescricao_Medicamento'


class PresencaHd(models.Model):
    id_presenca_hd = models.IntegerField(db_column='ID_Presenca_HD', primary_key=True)  # Field name made lowercase.
    data_presenca_hd = models.DateField(db_column='Data_Presenca_HD')  # Field name made lowercase.
    id_cadastro_hd = models.ForeignKey(CadastroHd, models.DO_NOTHING, db_column='ID_Cadastro_HD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Presenca_HD'


class PresencaTreinamento(models.Model):
    id_presenca_treinamento = models.IntegerField(db_column='ID_Presenca_Treinamento', primary_key=True)  # Field name made lowercase.
    atraso = models.IntegerField(db_column='Atraso')  # Field name made lowercase.
    id_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='ID_Funcionario')  # Field name made lowercase.
    id_treinamento = models.ForeignKey('Treinamento', models.DO_NOTHING, db_column='ID_Treinamento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Presenca_Treinamento'


class PrestacaoPagaEmprestimo(models.Model):
    id_prestacao_paga_emprestimo = models.IntegerField(db_column='ID_Prestacao_Paga_Emprestimo', primary_key=True)  # Field name made lowercase.
    id_emprestimo = models.ForeignKey(Emprestimo, models.DO_NOTHING, db_column='ID_Emprestimo')  # Field name made lowercase.
    valor_pago_prestacao = models.DecimalField(db_column='Valor_Pago_Prestacao', max_digits=8, decimal_places=2)  # Field name made lowercase.
    data_pagamento_prestacao = models.DateField(db_column='Data_Pagamento_Prestacao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Prestacao_Paga_Emprestimo'


class Recibo(models.Model):
    id_recibo = models.CharField(db_column='ID_Recibo', primary_key=True, max_length=50)  # Field name made lowercase.
    valor = models.DecimalField(db_column='Valor', max_digits=8, decimal_places=2)  # Field name made lowercase.
    cheque = models.IntegerField(db_column='Cheque', blank=True, null=True)  # Field name made lowercase.
    destinario = models.CharField(db_column='Destinario', max_length=50)  # Field name made lowercase.
    produto = models.CharField(db_column='Produto', max_length=50, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data')  # Field name made lowercase.
    nome_nota = models.CharField(db_column='Nome_Nota', max_length=50)  # Field name made lowercase.
    id_nota_fiscal = models.ForeignKey(NotaFiscal, models.DO_NOTHING, db_column='ID_Nota_Fiscal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recibo'


class RegistroLigacaoPaciente(models.Model):
    id_registro_ligacao_paciente = models.IntegerField(db_column='ID_Registro_Ligacao_Paciente', primary_key=True)  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=120)  # Field name made lowercase.
    id_paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='ID_Paciente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Registro_Ligacao_Paciente'


class ResponsavelHistorico(models.Model):
    id_reponsabilidade = models.IntegerField(db_column='ID_Reponsabilidade', primary_key=True)  # Field name made lowercase.
    data_inicio = models.DateField(db_column='Data_Inicio')  # Field name made lowercase.
    data_fim = models.DateField(db_column='Data_Fim')  # Field name made lowercase.
    id_paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='ID_Paciente')  # Field name made lowercase.
    id_cpf = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='ID_CPF')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Responsavel_Historico'


class RoupaPaciente(models.Model):
    id_roupa_paciente = models.IntegerField(db_column='ID_Roupa_Paciente', primary_key=True)  # Field name made lowercase.
    descricao_roupa = models.CharField(db_column='Descricao_Roupa', max_length=200)  # Field name made lowercase.
    quantidade_roupa = models.IntegerField(db_column='Quantidade_Roupa')  # Field name made lowercase.
    roupa_devolvida = models.IntegerField(db_column='Roupa_Devolvida')  # Field name made lowercase.
    roupa_lavanderia = models.IntegerField(db_column='Roupa_Lavanderia')  # Field name made lowercase.
    id_paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='ID_Paciente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Roupa_Paciente'


class SaidaMedicamento(models.Model):
    id_saida_medicamento = models.IntegerField(db_column='ID_Saida_Medicamento', primary_key=True)  # Field name made lowercase.
    data_saida = models.DateTimeField(db_column='Data_Saida')  # Field name made lowercase.
    valor_saida = models.DecimalField(db_column='Valor_Saida', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    quantidade_de_gotas = models.IntegerField(db_column='Quantidade_de_Gotas', blank=True, null=True)  # Field name made lowercase.
    id_motivo_saida_pilula = models.ForeignKey(MotivoSaidaPilula, models.DO_NOTHING, db_column='ID_Motivo_Saida_Pilula')  # Field name made lowercase.
    id_prescricao_medicamento = models.ForeignKey(PrescricaoMedicamento, models.DO_NOTHING, db_column='ID_Prescricao_Medicamento', blank=True, null=True)  # Field name made lowercase.
    id_doacao_pilula = models.ForeignKey(DoacaoPilula, models.DO_NOTHING, db_column='ID_Doacao_Pilula', blank=True, null=True)  # Field name made lowercase.
    id_descontos_gratificacoes = models.ForeignKey(DescontosGratificacoes, models.DO_NOTHING, db_column='ID_Descontos_Gratificacoes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Saida_Medicamento'


class Salario(models.Model):
    id_salario = models.IntegerField(db_column='ID_Salario', primary_key=True)  # Field name made lowercase.
    valor_salario = models.DecimalField(db_column='Valor_Salario', max_digits=8, decimal_places=2)  # Field name made lowercase.
    mes_inicio_vigencia_reajuste = models.CharField(db_column='Mes_Inicio_Vigencia_Reajuste', max_length=2)  # Field name made lowercase.
    ano_inicio_vigencia_reajuste = models.CharField(db_column='Ano_Inicio_Vigencia_Reajuste', max_length=4)  # Field name made lowercase.
    data_reajuste = models.DateField(db_column='Data_Reajuste')  # Field name made lowercase.
    porcentagem_reajuste = models.FloatField(db_column='Porcentagem_Reajuste')  # Field name made lowercase.
    id_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='ID_Funcionario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Salario'


class Setor(models.Model):
    id_setor = models.IntegerField(db_column='ID_Setor', primary_key=True)  # Field name made lowercase.
    nome_setor = models.CharField(db_column='Nome_Setor', max_length=50)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Setor'


class Sindicato(models.Model):
    id_sindicato = models.IntegerField(db_column='ID_Sindicato', primary_key=True)  # Field name made lowercase.
    nome_sindicato = models.CharField(db_column='Nome_Sindicato', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sindicato'


class Situacao(models.Model):
    id_situacao = models.IntegerField(db_column='ID_Situacao', primary_key=True)  # Field name made lowercase.
    tipo_situacao = models.CharField(db_column='Tipo_Situacao', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Situacao'


class TecnicoPlantao(models.Model):
    id_atendimento_plantao_tecnico = models.IntegerField(db_column='ID_Atendimento_Plantao_Tecnico', primary_key=True)  # Field name made lowercase.
    data_atendimento = models.DateField(db_column='Data_Atendimento')  # Field name made lowercase.
    filestream_tecnico_plantao = models.CharField(db_column='FILESTREAM_Tecnico_Plantao', max_length=200)  # Field name made lowercase.
    id_paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='ID_Paciente')  # Field name made lowercase.
    id_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='ID_Funcionario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tecnico_Plantao'


class TipoAutorizacao(models.Model):
    id_tipo_autorizacao = models.IntegerField(db_column='ID_Tipo_Autorizacao', primary_key=True)  # Field name made lowercase.
    nome_autorizacao = models.CharField(db_column='Nome_Autorizacao', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_Autorizacao'


class TipoCobranca(models.Model):
    id_tipo_cobranca = models.IntegerField(db_column='ID_Tipo_Cobranca', primary_key=True)  # Field name made lowercase.
    nome_tipo_cobranca = models.CharField(db_column='Nome_Tipo_Cobranca', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_Cobranca'


class TipoDescontoGratificacao(models.Model):
    id_tipo_desc_grat = models.IntegerField(db_column='ID_Tipo_Desc_Grat', primary_key=True)  # Field name made lowercase.
    nome_desconto_gratificacao = models.CharField(db_column='Nome_Desconto_Gratificacao', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_Desconto_Gratificacao'


class TipoMedicamento(models.Model):
    id_tipo_medicamento = models.IntegerField(db_column='ID_Tipo_Medicamento', primary_key=True)  # Field name made lowercase.
    nome_tipo = models.CharField(db_column='Nome_tipo', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_Medicamento'


class TipoStatusAutorizacao(models.Model):
    id_tipo_status_autorizacao = models.IntegerField(db_column='ID_Tipo_Status_Autorizacao', primary_key=True)  # Field name made lowercase.
    nome_tipo_status_autorizacao = models.CharField(db_column='Nome_Tipo_Status_Autorizacao', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_Status_Autorizacao'


class Treinamento(models.Model):
    id_treinamento = models.IntegerField(db_column='ID_Treinamento', primary_key=True)  # Field name made lowercase.
    nome_treinamento = models.CharField(db_column='Nome_Treinamento', max_length=50)  # Field name made lowercase.
    assunto_treinamento = models.CharField(db_column='Assunto_Treinamento', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Treinamento'


class TxtBrasindice(models.Model):
    id_txt_brasindice = models.IntegerField(db_column='ID_Txt_Brasindice', primary_key=True)  # Field name made lowercase.
    filestream_brasindice = models.CharField(db_column='FILESTREAM_Brasindice', max_length=200)  # Field name made lowercase.
    data_inserida_brasindice = models.DateField(db_column='Data_Inserida_Brasindice')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Txt_Brasindice'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)

from django import forms
from loginAndSignUp.models import *
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# # from loginAndSignUp.models import UserAdmin
# from loginAndSignUp.models import Pessoa

# # class SignUpForm(forms.ModelForm):
    
# #     class Meta:
# #         model = UserAdmin
# #         fields = ['id','login', 'senha1', 'senha2']

# class PessoaForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = Pessoa
#         exclude = (
#                 'email',
#                 'user_permissions',
#                 'groups',
#                 'first_name', 
#                 'last_name', 
#                 'is_staff', 
#                 'is_active',
#                 'is_superuser',
#                 'last_login',
#                 'date_joined'
#                 )

# class PessoaChangeForm(UserChangeForm):

#     class Meta(UserChangeForm):
#         model = Pessoa
#         exclude = (
#                 'email',
#                 'user_permissions',
#                 'groups',
#                 'first_name', 
#                 'last_name', 
#                 'is_staff', 
#                 'is_active',
#                 'is_superuser',
#                 'last_login',
#                 'date_joined'
#                 )


# # class CustomUserCreationForm(UserCreationForm):

# #     class Meta(UserCreationForm):
# #         model = CustomUser
# #         fields = ('username', 'email')

# # class CustomUserChangeForm(UserChangeForm):

# #     class Meta(UserChangeForm):
# #         model = CustomUser
# #         fields = ('username''

# class PessoaForm(forms.Form):

#     SEXO_CHOICES = [
#         (1,"M"),
#         (0,"F")
#     ]

#     STATUS_VIDA = [
#         (1,"Vivo"),
#         (0,"Morto")
#     ]

#     ESTADOS_CHOICES = [
#         ("AC","Acre"),
#         ("AL","Alagoas"),
#         ("AP","Amapá"),
#         ("AM","Amazonas"),
#         ("BA","Bahia"),
#         ("CE","Ceará"),
#         ("DF","Distrito Federal"),
#         ("ES","Espírito Santo"),
#         ("GO","Goiás"),
#         ("MA","Maranhão"),
#         ("MT","Mato Grosso"),
#         ("MS","Mato Grosso do Sul"),
#         ("MG","Minas Gerais"),
#         ("PA","Pará"),
#         ("PB","Paraíba"),
#         ("PR","Paraná"),
#         ("PE","Pernambuco"),
#         ("PI","Piauí"),
#         ("RJ","Rio de Janeiro"),
#         ("RN","Rio Grande do Norte"),
#         ("RS","Rio Grande do Sul"),
#         ("RO","Rondônia"),
#         ("RR","Roraima"),
#         ("SC","Santa Catarina"),
#         ("SP","São Paulo"),
#         ("SE","Sergipe"),
#         ("TO","Tocantins"),
#     ]

#     PAISES_CHOICES = [
#         ("Afeganistão","Afeganistão"),
#         ("África do Sul","África do Sul"),
#         ("Akrotiri","Akrotiri"),
#         ("Albânia","Albânia"),
#         ("Alemanha","Alemanha"),
#         ("Andorra","Andorra"),
#         ("Angola","Angola"),
#         ("Anguila","Anguila"),
#         ("Antárctida","Antárctida"),
#         ("Antígua e Barbuda","Antígua e Barbuda"),
#         ("Arábia Saudita","Arábia Saudita"),
#         ("Arctic Ocean","Arctic Ocean"),
#         ("Argélia","Argélia"),
#         ("Argentina","Argentina"),
#         ("Arménia","Arménia"),
#         ("Aruba","Aruba"),
#         ("Ashmore and Cartier Islands","Ashmore and Cartier Islands"),
#         ("Atlantic Ocean","Atlantic Ocean"),
#         ("Austrália","Austrália"),
#         ("Áustria","Áustria"),
#         ("Azerbaijão","Azerbaijão"),
#         ("Baamas","Baamas"),
#         ("Bangladeche","Bangladeche"),
#         ("Barbados","Barbados"),
#         ("Barém","Barém"),
#         ("Bélgica","Bélgica"),
#         ("Belize","Belize"),
#         ("Benim","Benim"),
#         ("Bermudas","Bermudas"),
#         ("Bielorrússia","Bielorrússia"),
#         ("Birmânia","Birmânia"),
#         ("Bolívia","Bolívia"),
#         ("Bósnia e Herzegovina","Bósnia e Herzegovina"),
#         ("Botsuana","Botsuana"),
#         ("Brasil","Brasil"),
#         ("Brunei","Brunei"),
#         ("Bulgária","Bulgária"),
#         ("Burquina Faso","Burquina Faso"),
#         ("Burúndi","Burúndi"),
#         ("Butão","Butão"),
#         ("Cabo Verde","Cabo Verde"),
#         ("Camarões","Camarões"),
#         ("Camboja","Camboja"),
#         ("Canadá","Canadá"),
#         ("Catar","Catar"),
#         ("Cazaquistão","Cazaquistão"),
#         ("Chade","Chade"),
#         ("Chile","Chile"),
#         ("China","China"),
#         ("Chipre","Chipre"),
#         ("Clipperton","Clipperton"),
#         ("Colômbia","Colômbia"),
#         ("Comores","Comores"),
#         ("Congo-Brazzaville","Congo-Brazzaville"),
#         ("Congo-Kinshasa","Congo-Kinshasa"),
#         ("Coral Sea Islands","Coral Sea Islands"),
#         ("Coreia do Norte","Coreia do Norte"),
#         ("Coreia do Sul","Coreia do Sul"),
#         ("Costa do Marfim","Costa do Marfim"),
#         ("Costa Rica","Costa Rica"),
#         ("Croácia","Croácia"),
#         ("Cuba","Cuba"),
#         ("Curacao","Curacao"),
#         ("Dhekelia","Dhekelia"),
#         ("Dinamarca","Dinamarca"),
#         ("Egipto","Egipto"),
#         ("Emiratos Árabes Unidos","Emiratos Árabes Unidos"),
#         ("Equador","Equador"),
#         ("Eritreia","Eritreia"),
#         ("Eslováquia","Eslováquia"),
#         ("Eslovénia","Eslovénia"),
#         ("Espanha","Espanha"),
#         ("Estados Unidos","Estados Unidos"),
#         ("Etiópia","Etiópia"),
#         ("Faroé","Faroé"),
#         ("Fiji","Fiji"),
#         ("Filipinas","Filipinas"),
#         ("Finlândia","Finlândia"),
#         ("França","França"),
#         ("Gabão","Gabão"),
#         ("Gâmbia","Gâmbia"),
#         ("Gana","Gana"),
#         ("Gaza Strip","Gaza Strip"),
#         ("Geórgia","Geórgia"),
#         ("Geórgia do Sul","Geórgia do Sul"),
#         ("Gibraltar","Gibraltar"),
#         ("Granada","Granada"),
#         ("Grécia","Grécia"),
#         ("Gronelândia","Gronelândia"),
#         ("Guame","Guame"),
#         ("Guatemala","Guatemala"),
#         ("Guernsey","Guernsey"),        
#         ("Guiana","Guiana"),        
#         ("Guiné","Guiné"),        
#         ("Guiné Equatorial","Guiné Equatorial"),        
#         ("Guiné-Bissau","Guiné-Bissau"),        
#         ("Haiti","Haiti"),
#         ("Honduras","Honduras"),
#         ("Hong Kong","Hong Kong"),
#         ("Hungria","Hungria"),
#         ("Iémen","Iémen"),
#         ("Ilha Bouvet","Ilha Bouvet"),
#         ("Ilha do Natal","Ilha do Natal"),
#         ("Ilha Norfolk","Ilha Norfolk"),
#         ("Ilhas Caimão","Ilhas Caimão"),
#         ("Ilhas Cook","Ilhas Cook"),
#         ("Ilhas dos Cocos","Ilhas dos Cocos"),
#         ("Ilhas Falkland","Ilhas Falkland"),
#         ("Ilhas Heard e McDonald","Ilhas Heard e McDonald"),
#         ("Ilhas Marshall","Ilhas Marshall"),
#         ("Ilhas Salomão","Ilhas Salomão"),
#         ("Ilhas Turcas e Caicos","Ilhas Turcas e Caicos"),
#         ("Ilhas Virgens Americanas","Ilhas Virgens Americanas"),
#         ("Ilhas Virgens Britânicas","Ilhas Virgens Britânicas"),
#         ("Índia","Índia"),
#         ("Indian Ocean","Indian Ocean"),
#         ("Indonésia","Indonésia"),
#         ("Irão","Irão"),
#         ("Iraque","Iraque"),
#         ("Irlanda","Irlanda"),
#         ("Islândia","Islândia"),
#         ("Itália","Itália"),
#         ("Jamaica","Jamaica"),
#         ("Jan Mayen","Jan Mayen"),
#         ("Jibuti","Jibuti"),
#         ("Jordânia","Jordânia"),
#         ("Kosovo","Kosovo"),
#         ("Kuwait","Kuwait"),
#         ("Laos","Laos"),
#         ("Lesoto","Lesoto"),
#         ("Letónia","Letónia"),
#         ("Líbano","Líbano"),
#         ("Libéria","Libéria"),
#         ("Líbia","Líbia"),
#         ("Listenstaine","Listenstaine"),
#         ("Lituânia","Lituânia"),
#         ("Luxemburgo","Luxemburgo"),
#         ("Macau","Macau"),
#         ("Macedónia","Macedónia"),
#         ("Madagáscar","Madagáscar"),
#         ("Malásia","Malásia"),
#         ("Malávi","Malávi"),
#         ("Maldivas","Maldivas"),
#         ("Mali","Mali"),
#         ("Malta","Malta"),
#         ("Marrocos","Marrocos"),
#         ("Maurícia","Maurícia"),
#         ("México","México"),
#         ("Moçambique","Moçambique"),
#         ("Moldávia","Moldávia"),
#         ("Mónaco","Mónaco"),
#         ("Montenegro","Montenegro"),
#         ("Namíbia","Namíbia"),
#         ("Nepal","Nepal"),
#         ("Nicarágua","Nicarágua"),
#         ("Nigéria","Nigéria"),
#         ("Noruega","Noruega"),
#         ("Nova Zelândia","Nova Zelândia"),
#         ("Países Baixos","Países Baixos"),
#         ("Panamá","Panamá"),
#         ("Papua-Nova Guiné","Papua-Nova Guiné"),
#         ("Paquistão","Paquistão"),
#         ("Paraguai","Paraguai"),
#         ("Peru","Peru"),
#         ("Polónia","Polónia"),
#         ("Porto Rico","Porto Rico"),
#         ("Portugal","Portugal"),
#         ("Quénia","Quénia"),
#         ("Quirguizistão","Quirguizistão"),
#         ("Reino Unido","Reino Unido"),
#         ("República Checa","República Checa"),
#         ("República Dominicana","República Dominicana"),
#         ("Roménia","Roménia"),
#         ("Rússia","Rússia"),
#         ("Serra Leoa","Serra Leoa"),
#         ("Sérvia","Sérvia"),
#         ("Sérvia","Sérvia"),
#         ("Singapura","Singapura"),
#         ("Sudão","Sudão"),
#         ("Suécia","Suécia"),
#         ("Suíça","Suíça"),
#         ("Suriname","Suriname"),
#         ("Tailândia","Tailândia"),
#         ("Taiwan","Taiwan"),
#         ("Tunísia","Tunísia"),
#         ("Uruguai","Uruguai"),
#         ("Ucrânia","Ucrânia"),
#         ("Outro","Outro")
#     ]
    
#     cpf = forms.CharField(max_length=20,label="CPF")

#     nome_pessoa = forms.CharField(max_length=200,label="nome")

#     sexo_masculino = forms.ChoiceField(choices=SEXO_CHOICES,label="Sexo")

#     falecido = forms.ChoiceField(choices=STATUS_VIDA,label="Óbito",help_text="Essa pessoa está viva?")

#     data_nascimento = forms.DateField(label="Data de Nascimento")

#     telefone_residencial = forms.CharField(max_length=20,label="telefone residencial")

#     telefone_celular = forms.CharField(max_length=20,label="telefone celular")

#     email = forms.CharField(max_length=100, label="email")

#     rg = forms.CharField(max_length=20, label="RG")

#     rg_orgao_expeditor = forms.CharField(max_length=50, label="Órgão expeditor")

#     rg_uf = forms.ChoiceField(
#         choices=ESTADOS_CHOICES,
#         label="UF"
#     )

#     rg_data_emissao = forms.DateField(label="Data emissão")

#     naturalidade = forms.ChoiceField(choices=PAISES_CHOICES,label="Naturalidade")

#     profissao = forms.CharField(max_length=50,label="Profissão")

#     conjugue = forms.CharField(max_length=200,label="Cônjugue")

#     endereco_rua = forms.CharField(max_length=100,label="Rua")

#     endereco_complemento = forms.IntegerField(label="Complemento")

#     endereco_cep = forms.CharField(max_length=50,label="CEP")

#     endereco_estado = forms.ChoiceField(choices = ESTADOS_CHOICES,label="Estado")

#     endereco_cidade = forms.CharField(max_length=100,label="Cidade")

#     endereco_bairro = forms.CharField(max_length=100,label="Bairro")

#     estado_civil = forms.ModelChoiceField(
#         queryset = EstadoCivil.objects.all(),
#         empty_label= None,
#         label="Estado Civil"
#     )

#     grau_instrucao = forms.ModelChoiceField(
#         queryset = GrauInstrucao.objects.all(),
#         empty_label= None,
#         label="Grau de Instrução"
#     )

#     medico = forms.BooleanField(required=False,label="É médico?")



class MedicoLoginForm(forms.Form):

    senha = forms.CharField(max_length=100)

    crm = forms.CharField(max_length=200)
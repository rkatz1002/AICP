from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from loginAndSignUp.forms import PessoaForm

def seInscreva(request):

    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            cpf = form.cleaned_data.get('cpf')
            Nome = form.cleaned_data.get('Nome')
            Falecido = form.cleaned_data.get('Falecido')
            Data_Nascimento = form.cleaned_data.get('Data_Nascimento')
            Telefone_Residencial = form.cleaned_data.get('Telefone_Residencial')
            Telefone_Celular = form.cleaned_data.get('Telefone_Celular')
            rg = form.cleaned_data.get('rg')
            rg_orgao_expeditor = form.cleaned_data.get('rg_orgao_expeditor')
            rg_uf = form.cleaned_data.get('rg_uf')
            rg_data_emissao = form.cleaned_data.get('rg_data_emissao')
            Naturalidade = form.cleaned_data.get('Naturalidade')
            uf = form.cleaned_data.get('uf')
            Profissao = form.cleaned_data.get('Profissao')
            Conjugue = form.cleaned_data.get('Conjugue')
            Endereco_Rua = form.cleaned_data.get('Endereco_Rua')
            Endereco_Complemento = form.cleaned_data.get('Endereco_Complemento')
            Endereco_CEP = form.cleaned_data.get('Endereco_CEP')
            Endereco_Estado = form.cleaned_data.get('Endereco_Estado')
            Endereco_Cidade = form.cleaned_data.get('Endereco_Cidade')
            Endereco_Bairro = form.cleaned_data.get('Endereco_Bairro')
            Estado_Civil = form.cleaned_data.get('Estado_Civil')
            Grau_de_Instrucao = form.cleaned_data.get('Endereco_Rua')
            Endereco_Rua = form.cleaned_data.get('Grau_de_Instrucao')

            return render(request, 'sign-up.html', {'form': form})
    else:
        form = PessoaForm()
        
    return render(request, 'sign-up.html', {'form': form})

def entrar(request):

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password','')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)        
            return render(request, 'home.html', {'user':user})
        else:
            return render(request, 'base.html')

    return render(request, 'login.html')

def base(request):

    return render(request, 'base.html')

def imprimirEtiqueta(request):
    return render(request, 'imprimir-etiqueta.html')

def saidaFuncionario(request):
    return render(request, 'saida-funcionario.html')

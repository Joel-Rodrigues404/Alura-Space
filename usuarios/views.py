""" Views referentes as funcionalidades do aplicativo usuarios """

""" IMPORTAÇOES DE MODULOS QUE FORAM USADOS """
from usuarios.forms import LoguinForms, CadastroForms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth

# Create your views here.

def login(request):
    """ View pra fazer o login do user """

    form = LoguinForms() #Cria o Form vazio
    if request.method == 'POST': #Se tiver algum input
        form = LoguinForms(request.POST)#Preenche o form com as informaçoes passadas
        if form.is_valid():
            #Pega os dados nesseçarios para Autenticar um user
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha
            )
            if usuario is not None:
                auth.login(request, usuario)#Faz login
                messages.success(request, f'{nome} Logado com Sucesso!')
                return redirect('galeria:index')
            else:
                #Se o Usuario for Null
                messages.error(request, 'Erro ao Efetuar Login!')
                return redirect('usuarios:login')
            
    return render(request, 'usuarios/login.html', {'form':form})

def cadastro(request):
    """ View para criar um novo usuario """

    form = CadastroForms()#Cria form vazio
    if request.method == 'POST':#Se for enviado algum dado
        form = CadastroForms(request.POST)#Preenche o form com as informaçoes passadas
        if form.is_valid():
            #Valida se nome_cadastro ou email ja existem no banco de dados
            if User.objects.filter(username=form['nome_cadastro'].value()).exists() or User.objects.filter(email=form['email'].value()).exists():
                #Se for True volta para fazer cadastro de novo
                messages.error(request, 'Usuario ou Email ja Cadastrados!')
                return redirect('usuarios:cadastro')
            #Coleta os dados nessaçarios para Criar um usuario
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_2'].value()
            #Cria o user com os dados
            usuario = User.objects.create_user(
                username = nome,
                email = email,
                password = senha,
            )
            #Salva user no banco de dados
            usuario.save()
            messages.success(request, 'Cadastro efetuado com Sucesso!')
            return redirect('usuarios:login')

    return render(request, 'usuarios/cadastro.html', {"form":form})

def logout(request):
    """ View para deslogar o user """
    
    auth.logout(request)#desloga o user
    messages.success(request, 'Logout efetuado com Sucesso!')
    return redirect('usuarios:login')

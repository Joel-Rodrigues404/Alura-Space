""" Views referentes as funcionalidades do aplicativo galeria """

""" IMPORTAÇOES DE MODULOS QUE FORAM USADOS """
from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia
from django.contrib import messages

def index(request):
    """ Tela inicial Mostra todas as fotografias publicadas por orden de envio"""
    #Se o user não estiver logado ele e enviado para a pagina de logar
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario Não logado')
        return redirect('usuarios:login')
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)#Pega todas as fotos publicadas e em ordem de envio
    return render(request, 'galeria/index.html', {"cards":fotografias})

def imagem(request, foto_id):
    """ Tela que mostra uma imagem especificada pela foto_id """
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografia":fotografia})

def buscar(request):
    """ tela que busca uma fot especifica pelo nome """
    #Se o user não estiver logado ele e enviado para a pagina de logar
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario Não logado')
        return redirect('usuarios:login')
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']#referencia ao name="buscar" no html
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)#nome__icontains IMPORTANTE
    return render(request, 'galeria/buscar.html', {'cards':fotografias})

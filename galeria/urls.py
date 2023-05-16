""" Urls do aplicativo blogs """

""" IMPORTAÇOES DE MODULOS QUE FORAM USADOS """
from django.urls import path
from galeria.views import index, imagem, buscar

app_name = 'galeria'
urlpatterns = [
    #Pagina Inicial
    path('', index, name='index'),
    #Pagina para mostrar uma foto sendo passada o parametro id
    path('imagem/<int:foto_id>/', imagem, name='imagem'),
    #Pagina de buscar
    path('buscar/', buscar, name='buscar')
]

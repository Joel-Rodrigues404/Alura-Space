""" IMPORTAÇOES DE MODULOS QUE FORAM USADOS """

from django.urls import path
from usuarios.views import login, cadastro, logout

app_name = 'usuarios'
urlpatterns = [
    #Pagina de login
    path('login/', login, name='login'),
    #Pagina de cadastro
    path('cadastro/', cadastro, name='cadastro'),
    #Logout
    path('logout/', logout, name='logout')
]

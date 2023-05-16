""" Configurações do site para admins """

""" IMPORTAÇOES DE MODULOS QUE FORAM USADOS """
from django.contrib import admin
from galeria.models import Fotografia
# Register your models here.

class ListandoFotografias(admin.ModelAdmin):
    """ Class para visualização da pagina de admin de Fotografia """
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria","usuario",)
    list_editable = ("publicada",)
    list_per_page = 10
    
#Onde são registrados os models para apareçerem no site para admins
admin.site.register(Fotografia, ListandoFotografias)

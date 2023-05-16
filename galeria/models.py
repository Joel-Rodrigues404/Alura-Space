""" Models referentes ao Aplicativo galeria """

""" IMPORTAÇOES DE MODULOS QUE FORAM USADOS """
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Fotografia(models.Model):
    """ Model Referente a todas as fotografias """
    #Choices para a escolha com opcoes
    OPCOES_CATEGORIA = [
        ("NEBULOSA","nebulosa"),
        ("ESTRELA","estrela"),
        ("GALAXIA","galaxia"),
        ("PLANETA","planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)#null = vazia, Blank = string vazia
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')#recebe OPCOES_CATEGORIA para definir as opcoes
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)#Define a organização do diretorio de fotos como fotos/2023/05/16/arq.jpg
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)#Define com o horario atual
    #Relacionamento de chave estrangeira com o modelo USER que foi importado a cima que ja vem por padrão no django
    usuario = models.ForeignKey(
        to=User,#Define Model
        on_delete=models.SET_NULL,#Se o user passa a não existir o Campo usuario se tornara NUll
        null=True,
        blank=False,
        related_name='user',
    )
    
    """ Passa a nomear a instancia no plural quando se tem mais de uma fotografia ficando fotografias """
    class Meta:
        verbose_name_plural = 'Fotografias'

    def __str__(self) -> str:
        return self.nome

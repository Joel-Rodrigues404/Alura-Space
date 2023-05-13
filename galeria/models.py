from django.db import models
from datetime import datetime
# Create your models here.

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA","nebulosa"),
        ("ESTRELA","estrela"),
        ("GALAXIA","galaxia"),
        ("PLANETA","planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)#null = vazia, Blank = string vazia
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self) -> str:
        return self.nome
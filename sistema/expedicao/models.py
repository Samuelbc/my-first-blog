from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Expedicao(models.Model):
    data = models.DateField('data published')
    primeiro_tempo = models.IntegerField(default=0)
    segundo_tempo = models.IntegerField(default=0)
    terceiro_tempo = models.IntegerField(default=0)
    quarto_tempo = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    dia = models.CharField(max_length=20, null=True)
    mes = models.CharField(max_length=20, null=True)
    ano = models.CharField(max_length=20, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

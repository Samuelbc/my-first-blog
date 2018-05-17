from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Anuncio(models.Model):
    produto = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    reposicao = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

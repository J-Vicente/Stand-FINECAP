from django.db import models

# Create your models here.

class Reserva(models.Model):
    cnpj = models.CharField(max_length=14)
    nome_empresa = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100)
    quitado = models.BooleanField()

class Stand(models.Model):
    localizacao = models.CharField(max_length=100)
    valor = models.FloatField()

    
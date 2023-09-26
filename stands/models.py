from django.db import models

# Create your models here.

class Stand(models.Model):
    localizacao = models.CharField(max_length=100)
    valor = models.FloatField()

    def __str__(self):
        return self.localizacao


class Reserva(models.Model):
    cnpj = models.CharField(max_length=14)
    nome_empresa = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100)
    quitado = models.BooleanField()
    stand = models.OneToOneField(Stand,on_delete=models.CASCADE, null=True)
    data = models.DateField(auto_now_add=True)

    

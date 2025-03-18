from django.db import models

# Create your models here.
class Jogador(models.Model):
    nome=models.CharField(max_length=50)
    salario_inicial = models.FloatField()

    def __str__(self):
        return self.nome

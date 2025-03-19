from django.db import models

# Create your models here.
class Jogador(models.Model):
    nome=models.CharField(max_length=50)
    salario_inicial = models.FloatField()
    CPF = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Time(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class MeuTime(models.Model):
    players = models.ManyToManyField(Jogador)
    def __str__(self):
        return[jogador_atual.nome for jogador_atual in self.players.all()].__str__()

class Jogo(models.Model):
    data = models.DateTimeField()
    timeA = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="timeA")
    timeA_gols = models.IntegerField(default=0)
    timeB = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="timeB")
    timeB_gols  = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.timeA}x{self.timeB}'
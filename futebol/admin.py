from django.contrib import admin
from .models import Jogador, Time, MeuTime, Jogo

# Register your models here.
class JogadorAdmin(admin.ModelAdmin): #classe administrdora
    list_display = ('nome','salario_inicial','CPF',)
    search_fields = ('nome',)
    list_per_page = int = 2
    model = Jogador #modelo de referencia

class JogoAdmin (admin.ModelAdmin):
    list_display= ('timeA', 'timeA_gols', 'timeB_gols','timeB')
    model = Jogo

admin.site.register(Jogador, JogadorAdmin)
admin.site.register(Time)
admin.site.register(MeuTime)
admin.site.register(Jogo, JogoAdmin)
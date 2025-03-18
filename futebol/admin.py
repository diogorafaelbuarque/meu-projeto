from django.contrib import admin
from .models import Jogador

# Register your models here.
class JogadorAdmin(admin.ModelAdmin): #classe administrdora
    list_display = ('nome','salario_inicial')
    search_fields = ('nome',)
    list_per_page = int = 2
    model = Jogador #modelo de referencia

admin.site.register(Jogador, JogadorAdmin)

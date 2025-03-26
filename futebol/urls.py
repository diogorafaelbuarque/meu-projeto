from django.urls import path
from .views import listar_jogadores, adicionar_jogador, editar_jogador, excluir_jogador

urlpatterns = [ 
    path('', listar_jogadores, name='listar_jogadores'),
    path('novo/', adicionar_jogador, name='adicionar_jogador'),
    path('editar/<int:pk>/', editar_jogador, name='editar_jogador'),
    path('excluir/<int:pk>/', excluir_jogador, name= 'excluir_jogador')
]
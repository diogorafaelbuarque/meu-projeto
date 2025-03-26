from django.shortcuts import render, redirect, get_object_or_404
from .models import Jogador
from .forms import JogadorForm

def listar_jogadores(request):
    jogadores = Jogador.objects.all()
    return render(request, 'jogadores/listar.html',{'jogadores': jogadores})

def adicionar_jogador(request):
    if request.method == 'POST':
        form = JogadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_jogadores')
        else:
            form = JogadorForm()
            return render (request, 'jogadores/form.html', {'form': form, 'titulo': 'Adicionar Jogador'})
        
def editar_jogador(request,pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    if request.method == 'POST':
        form = JogadorForm(request.POST, instance=jogador)
        if form.is_valid():
            form.save()
            return redirect('listar_jogadores')
        else:
            form = JogadorForm(instance=jogador)
            return render (request, 'jogadores/form.html', {'form': form, 'titulo' : 'Editar Jogador'})
        
def excluir_jogador(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    if request.method == 'POST':
        jogador.delete()
        return redirect ('listar_jogadores')
    return render (request, 'jogadores/confirmar_exclusao.html', {'jogador': jogador})

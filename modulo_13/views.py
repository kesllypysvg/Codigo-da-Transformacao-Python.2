# produtos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

def listar_produtos(request):
    produtos = Produto.objects.all()
    contexto = {'produtos': produtos}
    return render(request, 'produtos/lista_produtos.html', contexto)

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        
        Produto.objects.create(
            nome=nome,
            descricao=descricao,
            preco=preco,
            quantidade=quantidade
        )
        return redirect('listar_produtos')
        
    return render(request, 'produtos/form_produto.html')

def atualizar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        produto.quantidade = request.POST.get('quantidade')
        produto.save()
        return redirect('listar_produtos')
        
    contexto = {'produto': produto}
    return render(request, 'produtos/form_produto.html', contexto)
    
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')
        
    contexto = {'produto': produto}
    return render(request, 'produtos/confirmar_exclusao.html', contexto)
    # produtos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('atualizar/<int:pk>/', views.atualizar_produto, name='atualizar_produto'),
    path('excluir/<int:pk>/', views.excluir_produto, name='excluir_produto'),
]
# meuprojeto/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produtos.urls')), # Adicione esta linha
]

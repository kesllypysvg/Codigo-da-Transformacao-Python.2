# produtos/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Produto

# Testes para o seu modelo Produto
class ProdutoModelTest(TestCase):
    def test_criacao_produto(self):
        """Testa se um produto é criado corretamente."""
        produto = Produto.objects.create(
            nome='Teclado Gamer',
            descricao='Teclado mecânico RGB',
            preco=250.00,
            quantidade=10
        )
        self.assertEqual(produto.nome, 'Teclado Gamer')
        self.assertEqual(produto.quantidade, 10)
    
    def test_representacao_str(self):
        """Testa a representação em string do objeto."""
        produto = Produto.objects.create(nome='Mouse')
        self.assertEqual(str(produto), 'Mouse')


# Testes para suas views (rotas)
class ProdutoViewTest(TestCase):
    def test_view_lista_produtos(self):
        """Testa se a página de listagem de produtos carrega corretamente."""
        response = self.client.get(reverse('listar_produtos'))
        self.assertEqual(response.status_code, 200) # Verifica se a página retornou status 200 OK
        self.assertContains(response, '<h1>Lista de Produtos</h1>') # Verifica se o HTML contém o título
        

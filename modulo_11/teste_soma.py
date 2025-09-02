import unittest

# --- 1. A FUNÇÃO A SER TESTADA ---
def soma(a, b):
    """Função que retorna a soma de dois números."""
    return a + b

# --- 2. A CLASSE DE TESTE ---
# A classe de teste deve herdar de unittest.TestCase
class TestSoma(unittest.TestCase):
    
    # 3. O MÉTODO DE TESTE
    # O nome do método deve começar com 'test_'
    def test_soma_numeros_inteiros(self):
        """Testa a soma de números inteiros."""
        # Define os valores de entrada e o resultado esperado
        resultado_esperado = 5
        
        # Chama a função e armazena o resultado
        resultado_real = soma(2, 3)
        
        # Usa o método de asserção para verificar se os resultados são iguais
        self.assertEqual(resultado_real, resultado_esperado)

    def test_soma_numeros_flutuantes(self):
        """Testa a soma de números flutuantes (decimais)."""
        resultado_esperado = 5.5
        resultado_real = soma(2.5, 3.0)
        self.assertEqual(resultado_real, resultado_esperado)

    def test_soma_com_negativos(self):
        """Testa a soma de números negativos."""
        resultado_esperado = -5
        resultado_real = soma(-2, -3)
        self.assertEqual(resultado_real, resultado_esperado)

# --- 4. EXECUTAR OS TESTES ---
# Este bloco de código é padrão e executa todos os testes da classe
if __name__ == '__main__':
    unittest.main()

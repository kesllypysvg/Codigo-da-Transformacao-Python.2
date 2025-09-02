import unittest

# --- 1. A CLASSE A SER TESTADA ---
class Calculadora:
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida!")
        return a / b

# --- 2. A CLASSE DE TESTE ---
class TestCalculadora(unittest.TestCase):
    
    # Este método é executado ANTES de cada teste.
    def setUp(self):
        # Cria uma nova instância da Calculadora para cada teste
        self.calculadora = Calculadora()
        print("Preparando para o teste...")
        
    # Este método é executado DEPOIS de cada teste.
    def tearDown(self):
        # Limpeza (opcional neste caso, mas útil para fechar conexões, etc.)
        print("Finalizando o teste.")

    # 3. MÉTODOS DE TESTE
    def test_somar_inteiros(self):
        # Testa a soma de números inteiros
        self.assertEqual(self.calculadora.somar(5, 3), 8)
        self.assertEqual(self.calculadora.somar(-1, 1), 0)

    def test_somar_flutuantes(self):
        # Testa a soma de números flutuantes (decimais)
        self.assertAlmostEqual(self.calculadora.somar(2.5, 3.5), 6.0)

    def test_dividir_inteiros(self):
        # Testa uma divisão válida
        self.assertEqual(self.calculadora.dividir(10, 2), 5)
        
    def test_dividir_flutuantes(self):
        # Testa uma divisão com resultado decimal
        self.assertAlmostEqual(self.calculadora.dividir(10, 4), 2.5)

    def test_divisao_por_zero(self):
        # Testa se a exceção correta é levantada
        with self.assertRaises(ValueError):
            self.calculadora.dividir(10, 0)
            
# --- 4. EXECUTAR OS TESTES ---
if __name__ == '__main__':
    unittest.main()

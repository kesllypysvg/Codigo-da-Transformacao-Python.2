import unittest

# A CLASSE CALCULADORA COM VALIDAÇÃO
class Calculadora:
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        # Validação: se o divisor for zero, lança uma exceção
        if b == 0:
            raise ValueError("Divisão por zero não é permitida!")
        # Outra validação: se os tipos não forem números, lança uma exceção
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("As entradas devem ser números!")
        return a / b

# A CLASSE DE TESTE
class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()
    
    # Teste para verificar se a exceção é lançada corretamente
    def test_divisao_por_zero(self):
        """Verifica se a exceção ValueError é levantada para divisão por zero."""
        # Usa 'with self.assertRaises' para esperar uma exceção
        with self.assertRaises(ValueError):
            self.calculadora.dividir(10, 0)

    def test_entradas_nao_numericas(self):
        """Verifica se a exceção TypeError é levantada para entradas inválidas."""
        with self.assertRaises(TypeError):
            self.calculadora.dividir("dez", 2)
            
# --- EXECUTAR OS TESTES ---
if __name__ == '__main__':
    unittest.main()

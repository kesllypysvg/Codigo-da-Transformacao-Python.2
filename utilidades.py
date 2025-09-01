# Arquivo: utilidades.py

def soma(a, b):
    """Calcula a soma de dois números."""
    return a + b

def subtracao(a, b):
    """Calcula a subtração de dois números."""
    return a - b

def potencia(base, expoente):
    """Calcula a potência de um número."""
    return base ** expoente

# Esta parte do código não será executada quando o módulo for importado,
# mas serve para testar as funções diretamente se o arquivo for rodado sozinho.
if __name__ == "__main__":
    print("Testando o módulo utilidades.py...")
    print(f"Soma de 5 e 3: {soma(5, 3)}")
    print(f"Subtração de 10 e 4: {subtracao(10, 4)}")
    print(f"Potência de 2 elevado a 5: {potencia(2, 5)}")

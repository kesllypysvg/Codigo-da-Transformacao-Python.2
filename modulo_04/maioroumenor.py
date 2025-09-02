def maior_menor(lista_de_numeros):
    """
    Encontra e retorna o maior e o menor número em uma lista.

    Args:
        lista_de_numeros (list): Uma lista de números inteiros ou flutuantes.

    Returns:
        tuple: Uma tupla contendo o maior e o menor número (maior, menor).
    """
    if not lista_de_numeros:
        return (None, None)  # Retorna None para listas vazias

    maior_valor = max(lista_de_numeros)
    menor_valor = min(lista_de_numeros)

    return (maior_valor, menor_valor)

# --- Exemplos de uso da função ---

# Exemplo 1: Lista de números inteiros
numeros1 = [10, 5, 25, 1, 9, 30]
maior, menor = maior_menor(numeros1)
print(f"Lista: {numeros1}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")

print("-" * 20)

# Exemplo 2: Lista com números flutuantes
numeros2 = [3.14, 1.618, 2.71, 0.577]
maior, menor = maior_menor(numeros2)
print(f"Lista: {numeros2}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")

print("-" * 20)

# Exemplo 3: Lista vazia
numeros3 = []
maior, menor = maior_menor(numeros3)
print(f"Lista: {numeros3}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")

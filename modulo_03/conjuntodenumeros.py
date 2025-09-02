# Conjunto de números a ser analisado
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Listas para armazenar os números pares e ímpares
numeros_pares = []
numeros_impares = []

# Loop para percorrer cada número na lista
for numero in numeros:
    # Use o operador de módulo (%) para verificar se o número é par
    # Um número é par se o resto da divisão por 2 for 0
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

# Exiba os resultados
print("--- Números Pares ---")
print(numeros_pares)

print("\n--- Números Ímpares ---")
print(numeros_impares)

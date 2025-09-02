def calcular_media(notas):
    """
    Calcula a média de um aluno e determina se ele foi aprovado ou reprovado.

    Args:
        notas (list): Uma lista de notas do aluno.

    Returns:
        float: A média calculada.
    """
    if not notas:
        return 0.0  # Retorna 0 se a lista de notas estiver vazia para evitar erro de divisão.

    # Calcula a soma das notas
    soma_das_notas = sum(notas)
    
    # Calcula a média dividindo a soma pelo número de notas
    media = soma_das_notas / len(notas)
    
    print(f"A média do aluno é: {media:.2f}")

    # Verifica se o aluno foi aprovado (média >= 7) ou reprovado
    if media >= 7.0:
        print("Status: Aprovado!")
    else:
        print("Status: Reprovado.")
        
    return media

# --- Exemplos de uso da função ---

# Exemplo 1: Aluno aprovado
print("--- Aluno 1 ---")
notas_aluno1 = [8.5, 7.0, 9.5]
calcular_media(notas_aluno1)

# Exemplo 2: Aluno reprovado
print("\n--- Aluno 2 ---")
notas_aluno2 = [6.0, 5.5, 7.0]
calcular_media(notas_aluno2)

# Exemplo 3: Notas em float (números com casas decimais)
print("\n--- Aluno 3 ---")
notas_aluno3 = [4.5, 7.8, 6.2, 8.0]
calcular_media(notas_aluno3)

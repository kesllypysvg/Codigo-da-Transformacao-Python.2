aluno = {
    "nome": "João Silva",
    "idade": 16,
    "notas": {
        "matematica": 9.5,
        "historia": 8.0,
        "ciencias": 7.5
    },
    "curso": "Ensino Médio"
}

# Exiba os dados do aluno
print("--- Dados do Aluno ---")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Curso: {aluno['curso']}")

# Exiba as notas do aluno (acessando o dicionário aninhado)
print("\n--- Notas ---")
for disciplina, nota in aluno['notas'].items():
    print(f"- {disciplina.capitalize()}: {nota}")

# Calcule e exiba a média das notas
soma_notas = sum(aluno['notas'].values())
quantidade_notas = len(aluno['notas'])
media = soma_notas / quantidade_notas

print(f"\nMédia Geral: {media:.2f}")

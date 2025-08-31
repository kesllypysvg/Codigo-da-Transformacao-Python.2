idade = int(input("Digite a sua idade: "))

# Estrutura condicional para classificar a idade
if idade < 0:
    print("Idade inválida. A idade não pode ser um número negativo.")
elif idade <= 12:
    print("Você é uma Criança.")
elif idade <= 17:
    print("Você é um Adolescente.")
elif idade <= 59:
    print("Você é um Adulto.")
else:
    print("Você é um Idoso.")

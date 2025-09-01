python
CopyEdit
a = 10
b = 3
print(a+b)
print(a//b)
print(a-b)

# Definindo algumas variáveis para usar nas expressões
a = 10
b = 5
c = 2

# 1. Expressão de adição
resultado_soma = a + b
print(f"O resultado de {a} + {b} é: {resultado_soma}")

# 2. Expressão de subtração
resultado_subtracao = a - b
print(f"O resultado de {a} - {b} é: {resultado_subtracao}")

# 3. Expressão de multiplicação
resultado_multiplicacao = a * c
print(f"O resultado de {a} * {c} é: {resultado_multiplicacao}")

# 4. Expressão de divisão
resultado_divisao = a / c
print(f"O resultado de {a} / {c} é: {resultado_divisao}")

# 5. Expressão com ordem de precedência (multiplicação primeiro)
resultado_complexo = a + b * c
print(f"O resultado de {a} + {b} * {c} é: {resultado_complexo}")

# 6. Expressão com parênteses (para mudar a ordem)
resultado_parenteses = (a + b) * c
print(f"O resultado de ({a} + {b}) * {c} é: {resultado_parenteses}")

# 7. Operador de módulo (resto da divisão)
resultado_modulo = a % 3
print(f"O resto da divisão de {a} por 3 é: {resultado_modulo}")

# 8. Operador de exponenciação (potência)
resultado_potencia = b ** c
print(f"O resultado de {b} elevado a {c} é: {resultado_potencia}")
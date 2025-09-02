# Arquivo: programa_principal.py

# Importa o módulo utilidades que acabamos de criar
import utilidades

# --- Utilizando as funções do módulo ---

# Chamando a função soma() do módulo utilidades
resultado_soma = utilidades.soma(15, 7)
print(f"A soma de 15 e 7 é: {resultado_soma}")

# Chamando a função subtracao()
resultado_subtracao = utilidades.subtracao(50, 25)
print(f"A subtração de 50 e 25 é: {resultado_subtracao}")

# Chamando a função potencia()
base = 3
expoente = 4
resultado_potencia = utilidades.potencia(base, expoente)
print(f"O resultado de {base} elevado a {expoente} é: {resultado_potencia}")

# Você também pode importar funções específicas para usar diretamente
from utilidades import soma

print(f"Usando 'soma' diretamente: 20 + 10 = {soma(20, 10)}")

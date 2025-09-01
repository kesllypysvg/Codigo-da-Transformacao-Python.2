import random
import math

def jogar_adivinhacao():
    """
    Cria um jogo de adivinhação onde o jogador tenta acertar
    um número gerado aleatoriamente entre 1 e 100.
    """
    # Gera um número inteiro aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    # A variável `math.inf` é um valor infinito.
    # Usado aqui para mostrar que não há limite de tentativas.
    # Não é estritamente necessário para a lógica do jogo,
    # mas mostra o uso da biblioteca `math`.
    limite_tentativas = math.inf
    
    print("--- Bem-vindo ao Jogo de Adivinhação! ---")
    print("Estou pensando em um número entre 1 e 100.")
    print("Tente adivinhar qual é!")
    
    while True:
        try:
            chute = int(input("Digite o seu palpite: "))
            tentativas += 1
            
            if chute < 1 or chute > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue

            if chute < numero_secreto:
                print("O número secreto é maior. Tente novamente!")
            elif chute > numero_secreto:
                print("O número secreto é menor. Tente novamente!")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
                break
                
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Inicia o jogo
if __name__ == "__main__":
    jogar_adivinhacao()

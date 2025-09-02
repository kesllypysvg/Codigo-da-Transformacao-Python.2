import csv
import os

NOME_ARQUIVO = "notas_alunos.csv"
CABECALHO = ["Nome do Aluno", "Disciplina", "Nota"]

def adicionar_nota(nome, disciplina, nota):
    """Adiciona uma nova linha com os dados da nota ao arquivo CSV."""
    # O modo 'a' (append) permite adicionar linhas sem apagar as existentes
    with open(NOME_ARQUIVO, 'a', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)

        # Se o arquivo estiver vazio, escreve o cabeçalho primeiro
        if os.stat(NOME_ARQUIVO).st_size == 0:
            escritor.writerow(CABECALHO)
        
        escritor.writerow([nome, disciplina, nota])
        print(f"Nota de '{nome}' em '{disciplina}' salva com sucesso.")

def exibir_notas():
    """Lê o arquivo CSV e exibe o conteúdo de forma organizada."""
    print("\n--- Notas dos Alunos ---")
    try:
        with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            
            # Pula a linha do cabeçalho
            proxima_linha = next(leitor)
            print(f"{' | '.join(proxima_linha)}")
            print("-" * 30)

            for linha in leitor:
                print(f"{' | '.join(linha)}")

    except FileNotFoundError:
        print(f"O arquivo '{NOME_ARQUIVO}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

# --- Demonstração do uso das funções ---

# 1. Adicionando algumas notas
adicionar_nota("Ana Paula", "Matemática", 8.5)
adicionar_nota("Carlos Mello", "História", 7.0)
adicionar_nota("Ana Paula", "Geografia", 9.0)
adicionar_nota("Carlos Mello", "Matemática", 6.5)

# 2. Exibindo as notas salvas
exibir_notas()

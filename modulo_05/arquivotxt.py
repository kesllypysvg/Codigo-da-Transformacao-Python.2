# Nome do arquivo que será criado
nome_do_arquivo = "dados_do_usuario.txt"

# --- Parte 1: Escrever informações no arquivo ---
try:
    # O modo 'w' (write) abre o arquivo para escrita.
    # Se o arquivo já existir, ele será sobrescrito.
    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
        # Escreve as linhas de texto no arquivo
        arquivo.write("Nome: Maria Silva\n")
        arquivo.write("Idade: 30\n")
        arquivo.write("Cidade: Rio de Janeiro\n")
        print(f"Dados gravados com sucesso no arquivo '{nome_do_arquivo}'.")

except IOError as e:
    print(f"Erro ao escrever no arquivo: {e}")

# --- Parte 2: Ler informações do arquivo ---
print("\n--- Conteúdo do Arquivo ---")
try:
    # O modo 'r' (read) abre o arquivo para leitura
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
        # Lê e imprime cada linha do arquivo
        for linha in arquivo:
            print(linha.strip())  # O .strip() remove espaços e quebras de linha extras

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_do_arquivo}' não foi encontrado.")
except IOError as e:
    print(f"Erro ao ler o arquivo: {e}")

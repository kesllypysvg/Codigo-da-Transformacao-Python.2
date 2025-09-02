import json

# Nome do arquivo JSON
nome_do_arquivo = "clientes.json"

# --- Parte 1: Salvar o dicionário em um arquivo JSON ---

# Dicionário de clientes
clientes = {
    "cliente_01": {
        "nome": "João da Silva",
        "email": "joao@email.com",
        "telefone": "11987654321"
    },
    "cliente_02": {
        "nome": "Maria de Souza",
        "email": "maria@email.com",
        "telefone": "21998765432"
    },
    "cliente_03": {
        "nome": "Pedro Santos",
        "email": "pedro@email.com",
        "telefone": "31976543210"
    }
}

try:
    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo_json:
        # json.dump() converte o dicionário para JSON e salva no arquivo
        json.dump(clientes, arquivo_json, indent=4, ensure_ascii=False)
        print(f"Dados dos clientes salvos com sucesso em '{nome_do_arquivo}'.")

except IOError as e:
    print(f"Erro ao salvar o arquivo: {e}")

# --- Parte 2: Carregar os dados de volta para um dicionário ---

print("\n--- Conteúdo do Arquivo JSON ---")

try:
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo_json:
        # json.load() lê o arquivo JSON e o converte de volta para um dicionário
        dados_carregados = json.load(arquivo_json)
        
        # Exibe os dados carregados
        for id_cliente, info in dados_carregados.items():
            print(f"ID: {id_cliente}")
            print(f"  Nome: {info['nome']}")
            print(f"  Email: {info['email']}")
            print(f"  Telefone: {info['telefone']}")
            print("-" * 20)

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_do_arquivo}' não foi encontrado.")
except json.JSONDecodeError:
    print(f"Erro: O arquivo '{nome_do_arquivo}' não está em um formato JSON válido.")
except IOError as e:
    print(f"Erro ao ler o arquivo: {e}")

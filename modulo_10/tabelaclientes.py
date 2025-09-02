import psycopg2

def criar_tabela_clientes(conn_params):
    """
    Conecta ao PostgreSQL e cria a tabela 'clientes' de forma simplificada.
    """
    try:
        # Usa 'with' para gerenciar a conexão e o cursor automaticamente
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cursor:
                # Comando SQL para criar a tabela
                create_table_command = """
                CREATE TABLE IF NOT EXISTS clientes (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL UNIQUE
                );
                """
                
                # Executa o comando e confirma a operação
                cursor.execute(create_table_command)
                conn.commit()
                print("Tabela 'clientes' criada com sucesso!")

    except psycopg2.Error as error:
        # Captura e exibe qualquer erro do psycopg2
        print(f"❌ Erro ao conectar ou criar a tabela: {error}")

# --- Substitua com suas credenciais de acesso ---
conn_params = {
    "dbname": "meu_banco",
    "user": "meu_usuario",
    "password": "minha_senha",
    "host": "localhost",
    "port": "5432"
}

# Chama a função para criar a tabela
criar_tabela_clientes(conn_params)

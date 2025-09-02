import psycopg2

# Substitua com suas credenciais de acesso ao banco de dados PostgreSQL
conn_params = {
    "dbname": "meu_banco",
    "user": "meu_usuario",
    "password": "minha_senha",
    "host": "localhost",
    "port": "5432"
}

def _executar_query(query, params=None, fetch=False):
    """
    Função interna para executar comandos SQL de forma segura e simplificada.
    Garante que a conexão e o cursor sejam fechados automaticamente.
    """
    try:
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                if fetch:
                    return cursor.fetchall()
                else:
                    conn.commit()
                    return cursor.rowcount
    except psycopg2.Error as e:
        print(f"❌ Erro de banco de dados: {e}")
        return None

def inserir_cliente(nome, email):
    """Insere um novo registro na tabela clientes."""
    query = "INSERT INTO clientes (nome, email) VALUES (%s, %s);"
    row_count = _executar_query(query, (nome, email))
    if row_count is not None:
        print(f"✅ Cliente '{nome}' inserido com sucesso!")

def consultar_clientes():
    """Consulta e exibe todos os registros da tabela clientes."""
    query = "SELECT id, nome, email FROM clientes ORDER BY id;"
    clientes = _executar_query(query, fetch=True)
    
    print("\n--- Lista de Clientes ---")
    if clientes:
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}")
    else:
        print("Nenhum cliente encontrado ou erro de consulta.")
    print("-------------------------\n")

def atualizar_email_cliente(cliente_id, novo_email):
    """Atualiza o email de um cliente com base no ID."""
    query = "UPDATE clientes SET email = %s WHERE id = %s;"
    row_count = _executar_query(query, (novo_email, cliente_id))
    if row_count is not None:
        if row_count > 0:
            print(f"✅ Email do cliente ID {cliente_id} atualizado com sucesso!")
        else:
            print(f"⚠️  Nenhum cliente encontrado com o ID {cliente_id}.")

def deletar_cliente(cliente_id):
    """Deleta um registro da tabela clientes com base no ID."""
    query = "DELETE FROM clientes WHERE id = %s;"
    row_count = _executar_query(query, (cliente_id,))
    if row_count is not None:
        if row_count > 0:
            print(f"✅ Cliente ID {cliente_id} deletado com sucesso!")
        else:
            print(f"⚠️  Nenhum cliente encontrado com o ID {cliente_id}.")

# --- Demonstração do uso das funções CRUD ---
if __name__ == "__main__":
    inserir_cliente("Ana Souza", "ana.souza@email.com")
    inserir_cliente("Carlos Lima", "carlos.lima@email.com")
    inserir_cliente("Mariana Alves", "mariana.alves@email.com")
    consultar_clientes()
    print("Atualizando email do cliente 2...")
    atualizar_email_cliente(2, "carlos.lima.novo@email.com")
    consultar_clientes()
    print("Deletando cliente com ID 3...")
    deletar_cliente(3)
    consultar_clientes()

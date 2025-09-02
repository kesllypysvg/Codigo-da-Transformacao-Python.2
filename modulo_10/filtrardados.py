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

def consultar_clientes_por_nome(prefixo):
    """
    Consulta clientes cujo nome começa com um prefixo.
    Usa a cláusula LIKE para filtro.
    """
    query = "SELECT id, nome, email FROM clientes WHERE nome LIKE %s || '%';"
    clientes = _executar_query(query, (prefixo,), fetch=True)
    
    print(f"\n--- Clientes com nome começando com '{prefixo}' ---")
    if clientes:
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}")
    else:
        print("Nenhum cliente encontrado.")
    print("--------------------------------------------------\n")

def contar_clientes():
    """
    Conta o número total de registros na tabela.
    Usa a função de agregação COUNT.
    """
    query = "SELECT COUNT(*) FROM clientes;"
    total = _executar_query(query, fetch=True)
    
    if total:
        print(f"Total de clientes no banco de dados: {total[0][0]}")

def consultar_clientes_ordenados():
    """
    Consulta todos os clientes e os ordena por nome.
    Usa a cláusula ORDER BY.
    """
    query = "SELECT id, nome, email FROM clientes ORDER BY nome ASC;"
    clientes = _executar_query(query, fetch=True)
    
    print("\n--- Clientes Ordenados por Nome ---")
    if clientes:
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}")
    else:
        print("Nenhum cliente encontrado.")
    print("-------------------------------------\n")


# --- Demonstração do uso das novas funções ---
if __name__ == "__main__":
    
    # Exemplo 1: Clientes com o nome começando com "C"
    inserir_cliente("Camila Oliveira", "camila@email.com")
    inserir_cliente("João Pedro", "joao.p@email.com")
    inserir_cliente("Carlos Santos", "carlos@email.com")
    
    consultar_clientes_por_nome("C")
    
    # Exemplo 2: Contar o número de clientes
    contar_clientes()
    
    # Exemplo 3: Consultar clientes ordenados por nome
    consultar_clientes_ordenados()

from flask import Flask, request, jsonify
import sqlite3

# Define o nome do arquivo do banco de dados
DB_NAME = 'clientes.db'

# Cria a instância da aplicação Flask
app = Flask(__name__)

def _executar_db_query(query, params=(), fetch=False):
    """Função auxiliar para executar comandos no banco de dados."""
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            if fetch:
                return cursor.fetchall()
            else:
                conn.commit()
                return cursor.rowcount
    except sqlite3.Error as e:
        print(f"❌ Erro de banco de dados: {e}")
        return None

def criar_tabela_clientes():
    """Cria a tabela de clientes se ela não existir."""
    query = """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        );
    """
    _executar_db_query(query)
    print("Tabela 'clientes' pronta.")

# Rota POST para cadastrar usuários
@app.route("/cadastrar", methods=['POST'])
def cadastrar():
    dados_usuario = request.get_json()
    if not dados_usuario or not dados_usuario.get('nome') or not dados_usuario.get('email'):
        return jsonify({"erro": "Dados incompletos"}), 400

    query = "INSERT INTO clientes (nome, email) VALUES (?, ?)"
    params = (dados_usuario['nome'], dados_usuario['email'])
    
    row_count = _executar_db_query(query, params)
    
    if row_count is None:
        return jsonify({"erro": "Email já cadastrado ou erro interno"}), 409
    
    return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201

# Rota GET para listar todos os clientes
@app.route("/clientes", methods=['GET'])
def listar_clientes():
    query = "SELECT id, nome, email FROM clientes"
    clientes_raw = _executar_db_query(query, fetch=True)

    if clientes_raw is None:
        return jsonify({"erro": "Erro ao buscar clientes"}), 500
    
    clientes_formatados = [{"id": c[0], "nome": c[1], "email": c[2]} for c in clientes_raw]
    return jsonify(clientes_formatados)

if __name__ == '__main__':
    criar_tabela_clientes()
    app.run(debug=True)

# Importa as classes necessárias do Flask
from flask import Flask, request, jsonify

# Cria a instância da aplicação
app = Flask(__name__)

# Rota GET para saudação (do exemplo anterior)
@app.route("/saudacao", methods=['GET'])
def saudacao():
    return "Olá! Bem-vindo ao meu servidor Flask."

# Rota POST para cadastrar usuários
@app.route("/cadastrar", methods=['POST'])
def cadastrar():
    # Obtém os dados da requisição em formato JSON
    dados_usuario = request.get_json()
    
    # Verifica se os dados foram enviados corretamente
    if not dados_usuario:
        return jsonify({"erro": "Nenhum dado JSON recebido"}), 400
    
    # Extrai o nome e o email dos dados recebidos
    nome = dados_usuario.get("nome")
    email = dados_usuario.get("email")
    
    # Verifica se os campos essenciais estão presentes
    if not nome or not email:
        return jsonify({"erro": "Nome ou email ausentes"}), 400

    # Lógica de processamento (neste exemplo, apenas exibe os dados)
    print(f"Novo usuário cadastrado:")
    print(f"Nome: {nome}")
    print(f"Email: {email}")

    # Retorna uma resposta JSON de sucesso
    return jsonify({"mensagem": "Usuário cadastrado com sucesso!", "nome": nome, "email": email}), 201

# Bloco para rodar o servidor em modo de desenvolvimento
if __name__ == '__main__':
    app.run(debug=True)
    curl -X POST -H "Content-Type: application/json" -d '{"nome": "Alice", "email": "alice@exemplo.com"}' http://127.0.0.1:5000/cadastrar

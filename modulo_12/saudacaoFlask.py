# Importa a classe Flask
from flask import Flask

# Cria uma instância da aplicação Flask
# O nome '__name__' ajuda o Flask a encontrar os arquivos corretos
app = Flask(__name__)

# Define uma rota (endpoint) para o URL '/saudacao'
# A função abaixo será executada quando o usuário acessar essa URL
@app.route("/saudacao")
def saudacao():
    # Retorna uma mensagem de texto simples
    return "Olá! Bem-vindo ao meu servidor Flask."

# Bloco de código para rodar o servidor
# 'debug=True' permite recarregar o servidor automaticamente ao salvar o código
if __name__ == '__main__':
    app.run(debug=True)

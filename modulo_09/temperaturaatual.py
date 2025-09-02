import requests

def obter_previsao_tempo(cidade, api_key):
    """
    Obtém a previsão do tempo para uma cidade específica e exibe os dados relevantes.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Monta a URL completa para a requisição
    url_completa = f"{base_url}appid={api_key}&q={cidade}&units=metric&lang=pt_br"
    
    try:
        # Faz a requisição à API
        resposta = requests.get(url_completa)
        resposta.raise_for_status()  # Lança um erro para status de resposta ruins (4xx ou 5xx)
        
        # Converte a resposta JSON em um dicionário Python
        dados = resposta.json()
        
        # Verifica se a cidade foi encontrada
        if dados.get("cod") == 200:
            # Extrai os dados relevantes e os armazena em variáveis
            temperatura_atual = dados["main"]["temp"]
            sensacao_termica = dados["main"]["feels_like"]
            umidade = dados["main"]["humidity"]
            velocidade_vento = dados["wind"]["speed"]
            condicao_climatica = dados["weather"][0]["description"]
            
            # Exibe os dados em um formato organizado
            print("-" * 30)
            print(f"Previsão do tempo para: {cidade.title()}")
            print("-" * 40)
            print(f"🌡️  Temperatura atual: {temperatura_atual}°C")
            print(f"🌡️  Sensação térmica: {sensacao_termica}°C")
            print(f"☁️  Condições climáticas: {condicao_climatica.capitalize()}")
            print(f"💧  Umidade do ar: {umidade}%")
            print(f"💨  Velocidade do vento: {velocidade_vento} m/s")
            print("-" * 30)
            
        else:
            print(f"❌ Erro: Cidade '{cidade}' não encontrada. Verifique o nome.")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
    except KeyError as e:
        print(f"❌ Erro ao processar os dados da API. Chave ausente: {e}")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

# --- Substitua 'SUA_API_KEY' e 'SUA_CIDADE' pelas suas informações ---
api_key = "SUA_API_KEY"
cidade_desejada = "Rio de Janeiro"  # Exemplo: 'Rio de Janeiro', 'Brasilia', 'Tokyo'

# Chama a função para obter a previsão do tempo
obter_previsao_tempo(cidade_desejada, api_key)

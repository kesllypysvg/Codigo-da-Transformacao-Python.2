import requests

def obter_previsao_tempo(cidade, api_key):
    """
    Obtém a previsão do tempo para uma cidade específica usando a API do OpenWeatherMap.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Monta a URL completa para a requisição
    # A unidade 'metric' garante que a temperatura seja em Celsius
    url_completa = f"{base_url}appid={api_key}&q={cidade}&units=metric"
    
    try:
        # Faz a requisição à API
        resposta = requests.get(url_completa)
        resposta.raise_for_status()  # Lança um erro se a requisição falhar
        
        # Converte a resposta JSON em um dicionário Python
        dados = resposta.json()
        
        # Verifica se a cidade foi encontrada
        if dados["cod"] != "404":
            # Extrai as informações que queremos
            temperatura = dados["main"]["temp"]
            condicao_climatica = dados["weather"][0]["description"]
            umidade = dados["main"]["humidity"]
            
            # Formata e exibe as informações
            print(f"Previsão do tempo para {cidade}:")
            print(f"Temperatura: {temperatura}°C")
            print(f"Condição: {condicao_climatica.capitalize()}")
            print(f"Umidade: {umidade}%")
            
        else:
            print(f"Cidade '{cidade}' não encontrada.")
            
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
    except KeyError:
        print("Erro: Dados da API com formato inesperado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# --- Substitua 'SUA_API_KEY' e 'SUA_CIDADE' por suas informações ---
api_key = "SUA_API_KEY"
cidade = "São Paulo"  # Exemplo: 'São Paulo', 'London', 'Tokyo'

# Chama a função para obter e exibir a previsão do tempo
obter_previsao_tempo(cidade, api_key)

import requests
import json  # Importa a biblioteca para tratar erros de JSON

def obter_previsao_tempo_seguro(cidade, api_key):
    """
    Obtém a previsão do tempo com tratamento de erros robusto.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    url_completa = f"{base_url}appid={api_key}&q={cidade}&units=metric&lang=pt_br"
    
    try:
        # Tenta fazer a requisição e processar os dados
        resposta = requests.get(url_completa, timeout=10) # Adiciona um timeout de 10 segundos
        
        # Lança uma exceção para erros HTTP, como 404 (Não Encontrado) ou 500 (Erro do Servidor)
        resposta.raise_for_status()
        
        # Converte a resposta JSON em um dicionário Python
        dados = resposta.json()
        
        # Extrai os dados relevantes
        temperatura_atual = dados["main"]["temp"]
        sensacao_termica = dados["main"]["feels_like"]
        umidade = dados["main"]["humidity"]
        velocidade_vento = dados["wind"]["speed"]
        condicao_climatica = dados["weather"][0]["description"]
        
        # Exibe os dados de forma organizada
        print("-" * 30)
        print(f"Previsão do tempo para: {cidade.title()}")
        print("-" * 30)
        print(f"🌡️  Temperatura atual: {temperatura_atual}°C")
        print(f"🌡️  Sensação térmica: {sensacao_termica}°C")
        print(f"☁️  Condições climáticas: {condicao_climatica.capitalize()}")
        print(f"💧  Umidade do ar: {umidade}%")
        print(f"💨  Velocidade do vento: {velocidade_vento} m/s")
        print("-" * 30)
            
    except requests.exceptions.HTTPError as err_http:
        # Trata erros de requisição HTTP específicos (ex: 404, 401)
        if resposta.status_code == 404:
            print(f"❌ Erro 404: Cidade '{cidade}' não encontrada. Verifique a grafia.")
        elif resposta.status_code == 401:
            print(f"❌ Erro 401: Chave de API inválida. Verifique sua API key.")
        else:
            print(f"❌ Erro HTTP inesperado: {err_http}")
            
    except requests.exceptions.ConnectionError as err_con:
        # Trata problemas de conexão de rede (sem internet, DNS, etc.)
        print(f"❌ Erro de conexão: Falha ao conectar à internet ou ao servidor da API. {err_con}")
        
    except requests.exceptions.Timeout as err_timeout:
        # Trata caso a requisição demore demais para responder
        print(f"❌ Erro de tempo limite: A requisição demorou demais para responder. {err_timeout}")
        
    except json.JSONDecodeError:
        # Trata caso a resposta não seja um JSON válido
        print("❌ Erro de decodificação: A resposta da API não é um JSON válido.")

    except KeyError as err_key:
        # Trata caso algum campo esperado (ex: 'temp') esteja faltando na resposta
        print(f"❌ Erro de dados: O campo '{err_key}' está ausente na resposta da API.")
        
    except Exception as err:
        # Trata qualquer outro erro inesperado
        print(f"❌ Ocorreu um erro inesperado: {err}")

# --- Substitua 'SUA_API_KEY' e 'SUA_CIDADE' pelas suas informações ---
api_key = "SUA_API_KEY"
cidade_desejada = "Tokyo"

# Chama a função para obter a previsão do tempo com segurança
obter_previsao_tempo_seguro(cidade_desejada, api_key)

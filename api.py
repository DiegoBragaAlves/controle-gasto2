import requests

def obter_cotacao(moeda="USD"):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    
    try:
        response = requests.get(url)
        data = response.json()
        cotacao = data[f"{moeda}BRL"]["bid"]
        return float(cotacao)
    except:
        return None

import requests

# API publica do Open-Meteo para Curitiba
url = "https://api.open-meteo.com/v1/forecast?latitude=-25.28&longitude=-53.63&current_weather=true"
#"https://api.open-meteo.com/v1/forecast?latitude=-25.43&longitude=-49.27&current_weather=true"   public

# Fazendo a requisição
resp = requests.get(url)
clima = resp.json()

# Exibindo apenas informaÃ§Ãµes úteis
print("Temperatura atual:", clima["current_weather"]["temperature"], "Â°C")
print("Velocidade do vento:", clima["current_weather"]["windspeed"], "km/h")
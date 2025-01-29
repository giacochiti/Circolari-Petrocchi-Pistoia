import requests

# Configura il token del bot e il chat_id
TELEGRAM_BOT_TOKEN = "7305004967:AAGe1tySkfUANi9yp0Jh2uBNAJeWwHUG2SI"
TELEGRAM_CHAT_ID = "1885923992"

# Messaggio da inviare
message = "Ciao, mondo!"

# URL dell'API di Telegram per inviare messaggi
url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

# Parametri della richiesta
params = {
    "chat_id": TELEGRAM_CHAT_ID,
    "text": message
}

# Invia la richiesta
response = requests.post(url, data=params)

# Stampa la risposta (per debug)
print(response.json())

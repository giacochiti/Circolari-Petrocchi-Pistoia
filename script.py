import requests

# Token del bot Telegram
TOKEN = "7305004967:AAGe1tySkfUANi9yp0Jh2uBNAJeWwHUG2SI"  # Sostituisci con il tuo token

# Chat ID della tua conversazione (o gruppo)
CHAT_ID = "1885923992"  # Sostituisci con il tuo chat ID

# Funzione per inviare un messaggio su Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.get(url, params=params)
    return response.json()

# Esegui il test per inviare il messaggio
send_telegram_message("Il bot è attivo!")

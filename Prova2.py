import requests
import os

# Sostituisci con il token del tuo bot
TOKEN = "7305004967:AAGe1tySkfUANi9yp0Jh2uBNAJeWwHUG2SI" # Aggiungi qui il token del tuo bot
# Sostituisci con il chat ID del tuo account o gruppo
CHAT_ID = "1885923992"  # Aggiungi qui il chat ID

def send_telegram_message(message):
    """Invia un messaggio su Telegram"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.get(url, params=params)
    return response.json()

# Test: manda un messaggio di prova
send_telegram_message("Il bot è attivo!")

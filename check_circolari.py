import requests
from bs4 import BeautifulSoup
import re  # Per utilizzare espressioni regolari

# URL della pagina delle circolari
url = "https://liceoartisticopistoia.edu.it/circolari/"

# ID del tuo Telegram e token del bot
chat_id = '1885923992'  # Il tuo ID
token = '7305004967:AAGe1tySkfUANi9yp0Jh2uBNAJeWwHUG2SI'  # Il token del bot

# URL dell'API di Telegram
telegram_api_url = f"https://api.telegram.org/bot{token}/sendMessage"

# Funzione per inviare il messaggio a Telegram
def send_telegram_message(message):
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(telegram_api_url, data=payload)
    if response.status_code == 200:
        print("Messaggio inviato con successo su Telegram.")
    else:
        print("Errore nell'invio del messaggio su Telegram.")

# Effettua la richiesta HTTP al sito
response = requests.get(url)

# Controlla se la richiesta è andata a buon fine
if response.status_code == 200:
    # Parsing del contenuto HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trova il primo titolo della circolare
    ultima_circolare = soup.find('strong', class_='ptitle')

    # Estrai il numero dalla circolare usando espressioni regolari
    numero_circolare = None
    if ultima_circolare:
        match = re.search(r'Circolare n\.\s*(\d+)', ultima_circolare.text.strip())
        if match:
            numero_circolare = match.group(1)

    # Crea il messaggio
    if numero_circolare:
        message = f"Numero dell'ultima circolare: {numero_circolare}"
    else:
        message = "Numero della circolare non trovato."

    # Invia il messaggio su Telegram
    send_telegram_message(message)

else:
    print("Errore durante l'accesso al sito. Codice di stato:", response.status_code)

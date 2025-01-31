import os
import requests
from bs4 import BeautifulSoup

# Configurazione Telegram
chat_id = '1885923992'  # Il tuo ID
token = '7305004967:AAGe1tySkfUANi9yp0Jh2uBNAJeWwHUG2SI'  # Il token del bot

# URL della pagina delle circolari
url = 'https://liceoartisticopistoia.edu.it/circolari/'

# Funzione per inviare un messaggio su Telegram tramite l'API
def send_telegram_message(message):
    api_url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(api_url, data=payload)
    if response.status_code == 200:
        print("Messaggio inviato con successo!")
    else:
        print(f"Errore nell'invio del messaggio: {response.status_code}")

# Funzione per ottenere l'ultima circolare
def get_latest_circular():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trova il primo elemento della circolare più recente
    latest_circular_element = soup.find('div', class_='wpdm-link-tpl')
    circular_title = latest_circular_element.find('strong', class_='ptitle').text.strip()
    circular_link = latest_circular_element.find('a')['href']

    return circular_title, circular_link

# Funzione per gestire la creazione e l'aggiornamento del file ultima.txt
def manage_circular_file(circular_title):
    file_path = 'ultima.txt'

    # Controlla se il file esiste
    if not os.path.exists(file_path):
        # Se il file non esiste, crealo e scrivi circular_title
        with open(file_path, 'w') as file:
            file.write(circular_title)
        print(f"File creato. Titolo circolare salvato: {circular_title}")
    else:
        # Se il file esiste, leggi il contenuto
        with open(file_path, 'r') as file:
            saved_title = file.read().strip()

        # Confronta il titolo salvato con circular_title
        if saved_title == circular_title:
            # Se sono


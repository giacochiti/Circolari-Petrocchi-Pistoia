import requests
from bs4 import BeautifulSoup

# Configurazione Telegram
chat_id = '1885923992'  # Il tuo ID
token = '7305004967:AAGe1tySkfUANi9yp0Jh2uBNAJeWwHUG2SI'  # Il token del bot

# URL della pagina delle circolari
url = 'https://liceoartisticopistoia.edu.it/circolari/'

# Percorso del file
file_path = 'last_circular.txt'

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

# Funzione per leggere il contenuto del file
def read_last_circular():
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            return content
    except FileNotFoundError:
        print("Il file last_circular.txt non è stato trovato.")
        return None

# Funzione per ottenere l'ultima circolare
def get_latest_circular():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Trova il primo elemento della circolare più recente
    latest_circular_element = soup.find('div', class_='wpdm-link-tpl')
    if latest_circular_element is None:
        print("Impossibile trovare l'elemento della circolare più recente.")
        return None, None
    
    circular_title = latest_circular_element.find('strong', class_='ptitle').text.strip()
    circular_link = latest_circular_element.find('a')['href']
    
    return circular_title, circular_link

# Main
if __name__ == "__main__":
    # Leggi il contenuto del file last_circular.txt
    circular_content = read_last_circular()
    if circular_content:
        send_telegram_message(f"Contenuto di last_circular.txt:\n{circular_content}")
    else:
        print("Non è stato possibile leggere il contenuto del file.")
    
    # Ottieni l'ultima circolare dal sito
    circular_title, circular_link = get_latest_circular()
    if circular_title:
        send_telegram_message(f"Nuova circolare pubblicata:\nTitolo: {circular_title}\nLink: {circular_link}")
    else:
        print("Non è stato possibile recuperare l'ultima circolare dal sito.")

import requests
from bs4 import BeautifulSoup
import json

# Configurazione Telegram
chat_id = '1885923992'  # Il tuo ID
token = '7305004967:AAGe1tySkfUANi9yp0Jh2uBNAJeWwHUG2SI'  # Il token del bot

# URL della pagina delle circolari
url = 'https://liceoartisticopistoia.edu.it/circolari/'

# Dettagli del repository GitHub
github_token = 'tuo_github_token'
repo_owner = 'tuo_nome_utente_github'
repo_name = 'tuo_repository'
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

# Funzione per ottenere l'ultima circolare
def get_latest_circular():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Trova il primo elemento della circolare più recente
    latest_circular_element = soup.find('div', class_='wpdm-link-tpl')
    circular_title = latest_circular_element.find('strong', class_='ptitle').text.strip()
    circular_link = latest_circular_element.find('a')['href']
    
    return circular_title, circular_link

# Funzione per leggere il titolo dell'ultima circolare dal file su GitHub
def get_last_saved_circular():
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    headers = {'Authorization': f'token {github_token}'}
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        content = response.json()
        # Decodifica il contenuto del file (Base64)
        file_content = json.loads(content['content'])
        return file_content.strip()
    else:
        print(f"Errore nel recupero del file su GitHub: {response.status_code}")
        return None

# Funzione per aggiornare il titolo della circolare su GitHub
def update_last_saved_circular(new_title):
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    headers = {'Authorization': f'token {github_token}'}
    
    # Prendi l'ultima versione del file per aggiornare il contenuto
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        content = response.json()
        sha = content['sha']
        # Prepara il nuovo contenuto del file (Base64)
        new_content = json.dumps(new_title).encode('utf-8')
        
        # Carica il nuovo file su GitHub
        payload = {
            "message": "Aggiorna il titolo dell'ultima circolare",
            "content": new_content,
            "sha": sha
        }
        response = requests.put(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            print("File aggiornato con successo!")
        else:
            print(f"Errore nell'aggiornamento del file: {response.status_code}")
    else:
        print(f"Errore nel recupero del file per l'aggiornamento: {response.status_code}")

# Main
if __name__ == "__main__":
    last_saved_title = get_last_saved_circular()
    circular_title, circular_link = get_latest_circular()

    if last_saved_title != circular_title:
        # Invia il messaggio su Telegram
        message = f"Ultima circolare pubblicata:\nTitolo: {circular_title}\nLink: {circular_link}"
        send_telegram_message(message)
        
        # Aggiorna il file su GitHub con il nuovo titolo
        update_last_saved_circular(circular_title)
    else:
        print("Non ci sono nuove circolari.")


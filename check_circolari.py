import requests

# Configurazione Telegram
chat_id = '1885923992'  # Il tuo ID
token = '7305004967:AAGe1tySkfUANi9yp0Jh2uBNAJeWwHUG2SI'  # Il token del bot

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

# Main
if __name__ == "__main__":
    circular_content = read_last_circular()
    if circular_content:
        send_telegram_message(circular_content)
    else:
        print("Non è stato possibile leggere il contenuto del file.")

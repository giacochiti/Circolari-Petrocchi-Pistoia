# Percorso del file
file_path = 'last_circular.txt'

# Funzione per leggere il numero dal file
def read_last_circular():
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            # Estrai il numero dalla stringa
            number = int(content)
            return number
    except FileNotFoundError:
        print("Il file last_circular.txt non è stato trovato.")
        return None
    except ValueError:
        print("Il contenuto del file non è un numero valido.")
        return None

# Funzione per salvare il nuovo numero nel file
def save_new_circular(number):
    with open(file_path, 'w') as file:
        file.write(f"{number}")

# Main
if __name__ == "__main__":
    # Leggi il numero dal file
    last_number = read_last_circular()
    
    if last_number is not None:
        # Incrementa il numero di uno
        new_number = last_number + 1
        
        # Salva il nuovo numero nel file
        save_new_circular(new_number)
        
        print(f"Numero incrementato e salvato: {new_number}")
    else:
        print("Non è stato possibile leggere il contenuto del file.")

from app import create_app  # 👈 Importa la funzione che assembla l'app dal pacchetto 'app'

# Crea l'istanza dell'applicazione
app = create_app()

if __name__ == '__main__':
    # Avvia il server di sviluppo Flask
    app.run(debug=True)
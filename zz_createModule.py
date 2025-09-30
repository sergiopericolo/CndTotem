import os
import sys

APP_DIR = 'app'

def create_module_structure(module_name):
    module_path = os.path.join(APP_DIR, module_name)
    template_path = os.path.join(module_path, 'templates', module_name)
    html_file = os.path.join(template_path, f'{module_name}.html')
    init_file = os.path.join(module_path, '__init__.py')
    routes_file = os.path.join(module_path, 'routes.py')

    try:
        os.makedirs(template_path, exist_ok=True)
        print(f"Directory create con successo: {module_path}/ e {template_path}/")

        with open(html_file, 'w') as f:
            f.write("")
        print(f"File creato: {html_file}")        

        with open(init_file, 'w') as f:
            f.write("")
        print(f"File creato: {init_file}")

        with open(routes_file, 'w') as f:
            f.write("")
        print(f"File creato: {routes_file}")

    ### GESTIONE DEGLI ERRORI
    except Exception as e:
        print(f"ERRORE durante la creazione del modulo {module_name}: {e}")
        ### Avviso di pulizia manuale (processo interrotto)
        if os.path.exists(module_path):
             print(f"Errore critico. Potrebbe essere necessaria una pulizia manuale di {module_path}")



### CREAZIONE MODULO ###

if not os.path.isdir(APP_DIR):
    print(f"Errore: La directory '{APP_DIR}/' non esiste. Esegui questo script dalla radice del progetto.")
    sys.exit(1)

mod_name = input("Inserisci il nome del nuovo modulo: ").lower()

if not mod_name:
    print("Nome del modulo non valido. Uscita.")
    sys.exit(1)

create_module_structure(mod_name)
print(f"modulo {mod_name} creato con successo! ")

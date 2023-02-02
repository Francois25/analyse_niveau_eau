from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime
import json
import requests


# Envoi d'une requête pour récupérer le contenu de la page
url = 'http://192.168.1.33'
response = requests.get(url)

# Utilisation de BeautifulSoup pour parser le contenu HTML
volume_value = BeautifulSoup(response.content, 'html.parser').find(id='volume').get_text()
print(volume_value)

# Utilisation de Datetime pour obtenir la date du la mesure
date = datetime.today()
date = date.strftime("%d.%m.%y %X")
print(date)

# Ajout de la valeur à un fichier json
file_path = Path('H:/projet_python/analyse_niveau_eau/niveau_eau.json')
if file_path.exists():
    with open("niveau_eau.json", "r") as f:
        donnees = json.load(f)

    print(donnees)
    donnees[date]=volume_value

    with open('niveau_eau.json', 'w') as json_file:
        json.dump((donnees), json_file, indent=0, ensure_ascii=False)

else:
    print("Fichier non trouvé.")
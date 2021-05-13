import requests
from datetime import datetime




#Première source de données


#première source de données
url = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
#deuxième source de données
url_station_status = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"

try:
    reponse = requests.get(url)
    reponse_status = requests.get(url_station_status)
    temps = datetime.now().strftime("%Y%m%d_%H%M%S")
    data_1 = reponse.json()
    data_2 = reponse_status.json()
except requests.exceptions.Timeout:
    print("le serveur met trop de temps a répondre")
except requests.exceptions.TooManyRedirects:
    print("Essayez avec une autre URL")
except requests.exceptions.RequestException as e:
    raise SystemExit(e)


# récupération de la liste des stations
donnee_source_1 = data_1["data"]["stations"]
donnee_source_2 = data_2["data"]["stations"]

# transformation de la liste en dictionnaire avec la clé unique 'station_id'
stationLocalisation = {velib["station_id"]: velib for velib in donnee_source_1}
stationDisponibilite = {velib["station_id"]: velib for velib in donnee_source_2}

# Fusion des deux dictionnaire pour avoir toutes les informations nécessaires dans un seul dictionnaire

fusion_donnees = {k: {**v, **stationDisponibilite[k]} for k, v in stationLocalisation.items()}

# Filtrer les données en fonction des critères 8 velib dispo, dont au moins un velib electrique
data_finale = []

for key, value in fusion_donnees.items():
    if value["numBikesAvailable"] > 8 and value["num_bikes_available_types"][1]["ebike"] >= 1:
        data_finale.append(value)



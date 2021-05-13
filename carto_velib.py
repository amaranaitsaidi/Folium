#imports
import data
import folium
import folium.plugins
import popupCustom
import json
from shapely.geometry import shape, Point
import argparse







#initialisation de la carte
fond_carte = r'https://tile.osm.ch/switzerland/{z}/{x}/{y}.png'
map_position = [48.853, 2.35]
initial_zoom = 10
url = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"

#charger le fichier geojson du département 93
with open('./data/departement.geojson') as f:
    js = json.load(f)

#récupérer l'élément géometry dans la variable polygon
polygon = shape(js["features"][0]['geometry'])



def map_data_velib():
            """
            :param : chemin fichier de configuration
            :return: carte interactive, datée, sous format html
            """

            # initialiser la bas map à la france
            map_france = folium.Map(location=map_position,
                                    zoom_start= initial_zoom,
                                    tiles=fond_carte, attr="CartoDB positron")
            # initialiser la couche cluster
            velib_cluster = folium.plugins.MarkerCluster().add_to(map_france)

            #chargement du fichier geojson du déparement 93
            folium.GeoJson('./data/departement.geojson',
                           name='geojson'
                           ).add_to(map_france)

            # boucle sur l'ensemble des stations pour mapper les stations demandées
            for station in data.data_finale:
                latitude_velib = station["lat"]
                longetude_velib = station["lon"]
                coords = Point(longetude_velib, latitude_velib)
                if polygon.contains(coords):


                        folium.Marker([latitude_velib, longetude_velib],

                                          popup=popupCustom.popup(station["station_id"], station["name"], station["capacity"], station["numBikesAvailable"],
                                                                  station["num_bikes_available_types"][1]["ebike"],
                                                                  station["num_bikes_available_types"][0]["mechanical"],
                                                                  station["last_reported"]),
                                          icon=folium.Icon(color='green',icon='bicycle', prefix='fa')
                                          ).add_to(velib_cluster)


            # sauvegarde de la carte sous format .html avec la date
            map_france.save("index_" + data.temps  + ".html")

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="indiquer le chemin vers le fichier de configuration")
    #
    # parser.add_argument("file", help="chemin vers le fichier de configuration")
    #
    # args = parser.parse_args()

    map_data_velib()



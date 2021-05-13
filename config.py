import argparse
import configparser
import sys
import os


#chemin vers le fichier de configuration
file = './config.ini'



def main():


    if __name__ == '__main__':

        parser = configparser.ConfigParser()

        #tester si le fichier existe et le lire
        if os.path.exists(file):
            parser.read(file)

        else:
            sys.exit("le fichier est introuvable : {}".format(file))
    try:
        parser["DEFAULT"]["min_velib"],
        parser["DEFAULT"]["min_velib_electrique"],
        parser["files"]["limite_st_denis"],
        parser["files"]["url"]
        parser["files"]["url_station_status"]
    except KeyError as e :
        print(sys.exc_info()[0], e)
        print("le fichier de configuration n'est pas complet : {}".format(file))
        print("il manque : {}".format(e))
        sys.exit("Arrêt du script")


main()

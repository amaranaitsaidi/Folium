import folium


def popup(val1,val2,val3,val4,val5,val6,val7):
    """
    Fonction qui rempli un template HTML avec une variable texte
    :param valeur: objet de type str
    :return: str code html
    """
    return """
<table style="width: 200px">
    <tr>
        <td><strong>Id : </strong>{}</td>
    </tr>
     <tr>
        <td><strong>Name : </strong>{}</td>
    </tr>
     <tr>
        <td><strong>Capacité : </strong>{}</td>
    </tr>
    <tr>
        <td><strong>Velib Dispo : </strong>{}</td>
    </tr>
    <tr>
        <td><strong>Velib electrique : </strong>{}</td>
    </tr>
    <tr>
        <td><strong>Velib mecanique : </strong>{}</td>
    </tr>
    <tr>
        <td><strong>Dernière MAJ : </strong>{}</td>
    </tr>
</table>
""".format(val1,val2,val3,val4,val5,val6,val7)
import requests
from bs4 import BeautifulSoup
import bs4
import re


def obtenerCDT():
    # El url que tiene las tasas
    url = 'https://www.bancodebogota.com/wps/portal/banco-de-bogota/bogota/productos/para-ti/cdt-e-inversion/cdt-tradicional#tab-1'

    # El html de la pagina de las tasas
    html = requests.get(url).content

    # Se instancia un BeautifulSoup a partir del html
    soup = BeautifulSoup(html, 'html.parser')

    # La tabla de tasas tiene id = 'mtg', se encuentra esta tabla
    tabla = soup.find(id='mtg')  # type: bs4.Tag

    filas = []  # Filas de la tabla
    # Se recorren las filas de las tabla (<tr>)
    for child in tabla.children:
        if type(child) is bs4.Tag: # Solo nos interesan los hijos de tipo bs4.Tag
            cols = []  # Columnas en la fila de la tabla
            # Se obtienen los hijos de la <tr>, los <td>
            for td in child.children:
                if type(td) is bs4.Tag:
                    cols.append(td.string) # Se agrega a la lista de las columnas el contenido del <td>

            filas.append(cols) # Se agrega a la lista de las filas la lista de las columnas de esa fila

    tasas = {}  # Diccionario -> tasas[montoMinimo] = tasa
    # Recorre la tabla
    for fila in filas:
        for col in fila:
            if '%' in col:
                # El plazo esta en la penultima columna y la tasa en la ultima
                plazoString = fila[-2]
                tasaString = fila[-1]

                # El plazo minimo es el primer numero en el string de plazo
                plazoMinimo = [int(s) for s in plazoString.split() if s.isdigit()][0]

                # Se le quita el % y los espacios a la tasa y se convierte en float
                tasa = float(tasaString.strip().strip('%'))

                # Se agrega la tasa y el plazo al diccionario
                tasas[plazoMinimo] = tasa

    return tasas


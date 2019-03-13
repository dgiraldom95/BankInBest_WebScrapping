import requests
from bs4 import BeautifulSoup
import bs4
import re


def obtenerCDT():
    url = 'https://www.bancodebogota.com/wps/portal/banco-de-bogota/bogota/productos/para-ti/cdt-e-inversion/cdt-tradicional#tab-1'
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    # La tabla de tasas tiene id = 'mtg'
    tabla = soup.find(id='mtg')  # type: bs4.Tag

    filas = []  # Filas de la tabla
    for child in tabla.children:
        if type(child) is bs4.Tag:
            cols = []  # Columnas en la fila de la tabla

            for td in child.children:
                if type(td) is bs4.Tag:
                    cols.append(td.string)

            filas.append(cols)

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

                tasas[plazoMinimo] = tasa

    return tasas


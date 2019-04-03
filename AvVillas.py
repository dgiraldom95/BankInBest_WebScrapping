import requests
from bs4 import BeautifulSoup
import bs4
import re
from bs4 import BeautifulSoup
from CDT import CDT


class cdtAV:
    def __init__(self, monto, rango, porcentaje):
        self.monto = monto
        self.rango = rango
        self.porcentaje = porcentaje

    def __str__(self):
        cadena = "{0} {1} {2}"
        return cadena.format(self.monto, self.rango, self.porcentaje)

    def __repr__(self):
        cadena = "{0} {1} {2}"
        return cadena.format(self.monto, self.rango, self.porcentaje)


def obtenerCDT():
    url = 'https://www.avvillas.com.co/wps/portal/avvillas/banco/banca-personal/productos/ahorro-e-inversion/cdt-av-villas/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zifQIszTwsTQx8LAJ8LAwcQz28PMz8XYwtfYz0w_EpCPYw1Y8iRr8BDuBoQJx-PAqi8Bsfrh-FxwovF29D_AqMHU3wKjAODjEgoAAUSIScWZAbGhphkOmZ6aioCADbOL_N/dz/d5/L2dBISEvZ0FBIS9nQSEh/'

    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')

    tabla = soup.findAll('table')[1]

    filas = []

    cdts = []

    plazos = [90,120,180,360,540]

    montoMinimo = 10000000

    for child in tabla.children:
        if type(child) is bs4.Tag:
            for tsup in child.children:
                if type(tsup) is bs4.Tag:
                    cols = []
                    for td in tsup.children:
                        if type(td) is bs4.Tag:
                            if td.string != None:
                                cols.append(td.string)
                    if len(cols) > 0:
                        filas.append(cols)

    print(filas)

    contador = 0

    for fila in filas:
        if fila == filas[2]:
            for col in fila:
                if '%' in col:
                    col1 = col.replace('%', '')
                    tasa = float(col1)
                    cdt = CDT('AvVillas', plazos[contador], tasa, None, montoMinimo)
                    cdts.append(cdt)
    return cdts

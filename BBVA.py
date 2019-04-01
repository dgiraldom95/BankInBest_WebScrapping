import requests
from bs4 import BeautifulSoup
import bs4
import re
from bs4 import BeautifulSoup
from CDT import CDT

class cdtBBVA:
    def __init__(self,monto, rango, porcentaje):
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
    url = 'https://www.bbva.com.co/personas/productos/inversion/cdt/tradicional.html#tasas-de-interes-e.a'

    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')

    tabla = soup.findAll('div', class_='table--value')

    filas = []

    cdts = []

    montoMinimo = 1000000

    plazos= [60, 90, 129, 150, 180, 240, 370, 300, 330, 365]

    for div in tabla:
        a = div.text
        b = a.replace('\n', '')
        c = b.replace('     ', '')
        d = c.replace('   ','')
        if '$' in d:
            filas.append(d)
        else:
            e = d.replace(' ', '')
            filas.append(e)

    contador = 0
    #print(filas)

    for i in range(len(filas)):
        if filas[i].isdigit():
            if 'NOAPLICA' in filas[i+1]:
                rango = 365
                tasa = float(filas[i + 2].replace('%', '').replace(',', '.'))
                cdt = CDT('BBVA', rango, tasa, montoMinimo, None)
                cdts.append(cdt)
            else:
                rango = plazos[contador]
                tasa = float(filas[i+2].replace('%', '').replace(',','.'))
                cdt = CDT('BBVA', rango, tasa, montoMinimo, None)
                cdts.append(cdt)
                contador = contador+1
    return cdts

import requests
from bs4 import BeautifulSoup
import bs4
import re
from bs4 import BeautifulSoup

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

    montos = []

    cdts = []

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

    rango = ''
    contador = 0

    for i in range(len(filas)):
        if '$' in filas[i]:
            montos.append(filas[i])
        elif filas[i].isdigit():
            if 'NOAPLICA' in filas[i+1]:
                rango = '365'
                contador = 0
            else:
                rango = filas[i+1]
                contador = 0
        elif '%' in filas[i]:
            porcentaje = filas[i]
            cdt = cdtBBVA(montos[contador], rango, porcentaje)
            cdts.append(cdt)
            contador = contador + 1
    return cdts

from pathlib import Path
import requests
from bs4 import BeautifulSoup
import bs4
import tabula
from CDT import CDT
import re
import os

def obtenerCDT():
    url = 'https://www.bancopopular.com.co/wps/portal/bancopopular/inicio/informacion-interes/tasas#table-rates-cdt'

    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')

    tabla = soup.find_all("table", {"class": "simple-table"})[0]

    body = tabla.find('tbody')
    head = tabla.find('thead')
    i = 0
    plazos = []
    tasas = []
    montoMinimo = -1
    for child in head.children:
        if type(child) is bs4.Tag:
            if i==0:
                i+=1
            else:
                for th in child.children:
                    if type(th) is bs4.Tag:
                        plazo = int(re.search(r'\d+', th.string).group())
                        plazos.append(plazo)

    i = 0
    for child in body.children:
        if type(child) is bs4.Tag:
            for td in child.children:
                if type(td) is bs4.Tag:
                    if i == 0:
                        montoMinimo = int(td.string.split('a')[0].split('$')[1].strip('').replace('.',''))
                        print("monto = " + str(montoMinimo))
                        i=1
                    else:
                        tasa = float(td.string.strip('%').replace(',','.'))
                        tasas.append(tasa)

            break

    i = 0
    listaCdts = []
    while i < len(plazos):
        cdt = CDT('Banco Popular', plazos[i], tasas[i], montoMinimo, None)
        listaCdts.append(cdt)

    return listaCdts
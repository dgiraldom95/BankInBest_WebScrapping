from pathlib import Path
import requests
from bs4 import BeautifulSoup
import tabula
import math
from CDT import CDT
import re
import os

def obtenerCDT():
    url = 'https://www.itau.co/tasasytarifas'

    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')

    a = soup.find('a', string='Tasas productos pasivos')

    linkPDF = a['href']

    nombrePDF = 'CDTItau.pdf'

    file = Path(nombrePDF)

    pdfResponse = requests.get('https://www.itau.co' + linkPDF)
    file.write_bytes(pdfResponse.content)

    df = tabula.read_pdf(nombrePDF, relative_area=True, area=(76, 0, 96.16, 100))
    info = df.values.tolist()
    montoMinimo = 1000000
    listaCdts = []
    i = 0
    limite = len(info)
    while i < limite:
        plazo = int(re.search(r'\d+', info[i+1][0]).group())
        tasa = ''
        if isinstance(info[i][2], str):
            tasa = float(info[i][2].strip('%'))
        else:
            tasa = float(info[i+1][2].strip('%'))
        cdt = CDT('Itau', plazo, tasa, montoMinimo, None)
        listaCdts.append(cdt)
        i+=3

    os.remove(nombrePDF)
    return listaCdts
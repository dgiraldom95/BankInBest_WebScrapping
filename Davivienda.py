from pathlib import Path
from bs4 import BeautifulSoup
import requests
import os
import tabula

def obtenerCDT():
    url = 'https://www.davivienda.com/wps/portal/personas/nuevo/personas/aqui_puedo/construir_mi_futuro/inversiones/cdt/a0487af0-343f-4c94-bc79-9943220507a0/!ut/p/z1/pVPJbsIwEP0VeuBo2bEdjI8JiDZUKapSlviCnJBURs1C1tKvr9NDq4JIKnVO9vi9mXkzHijgDopUNupVVipL5Zu--2KyJ9Nn-rS0sTtbYRNZrmvP58w1vAWD298Ab8GJBiBvZvGVgR4JFD3PDhriG__ir-7x3_johlloiL-B_gz6a28THNsBMc5FsMFmXgNEf63LwQT2d63C0OnEkLx-QDfefoDRD_gaUG-ETvSQbF-3jd2IwPELgdtGRS1cp1mR6D_tdRHzUB2gjyU7GChAgFDTBJShKeDSRACzgEWY44BOTfhw1djrPuk9UcfTSVhQhFlaRe8V3LVhslf6XKRRtc-jotQbVY6RSlWosjH68chTrUZ5HR20V7PLqqhVMUrUKK6rusg6SqPBeiOj8lLsxYw3k9tiJaJTJuNOLIkBDTkFQcg44JwSjJGJmEQwT9ba0rMCIvYc5QB_2bRn8mG71t0nvUXbUg!!/dz/d5/L2dBISEvZ0FBIS9nQSEh/'

    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')

    a = soup.find('a', string = 'Ver tasas vigentes')

    linkPDF = a['href']

    nombrePDF = 'CDTDavivienda.pdf'

    file = Path(nombrePDF)

    pdfResponse = requests.get('https://www.davivienda.com' + linkPDF)
    file.write_bytes(pdfResponse.content)

    os.remove(nombrePDF)
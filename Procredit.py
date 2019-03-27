from pathlib import Path
from bs4 import BeautifulSoup
import requests
import tabula
import re

def obtenerCDT():

    url = 'https://www.bancoprocredit.com.co/es/home.html'

    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')

    a = soup.find('a', string = 'Tasas y Tarifas')

    linkPDF = a['href']

    nombrePDF = 'CDTProCredit.pdf'
    file = Path(nombrePDF)

    pdfResponse = requests.get('https://www.bancoprocredit.com.co' + linkPDF)
    file.write_bytes(pdfResponse.content)

    df = tabula.read_pdf(nombrePDF, pages = 3)
    print(df)


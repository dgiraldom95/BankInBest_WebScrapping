from pathlib import Path
from bs4 import BeautifulSoup
import requests
import tabula


def obtenerCDT():
    # El url que tiene las tasas
    url = 'https://www.bancopichincha.com.co/web/corporativo/tasas-y-tarifas'

    # El html de la pagina de las tasas
    html = requests.get(url).content

    # Se instancia un BeautifulSoup a partir del html
    soup = BeautifulSoup(html, 'html.parser')

    # Las tasas estan en un archivo pdf, el tag del link tiene el texto Tasas Vigentes
    a = soup.find('a', string='Tasas Vigentes')

    # El url del pdf
    linkPDF = a['href']

    # El archivo donde se va a guardar el pdf
    nombrePDF = 'CDTPichincha.pdf'
    file = Path(nombrePDF)

    # Guardar el pdf
    pdfResponse = requests.get('https://www.bancopichincha.com.co' + linkPDF)
    file.write_bytes(pdfResponse.content)

    # Lee el area marcada del pdf (top, left, bottom, right) y lo convierte a un dataframe
    df = tabula.read_pdf(nombrePDF, pages=3, relative_area=True, area=(50, 0, 80, 100))
    # Convierte el dataframe a una lista de listas
    info = df.values.tolist()

    tasas = {}
    for fila in info:
        for col in fila:
            if isinstance(col, str) and '%' in col:
                plazoString = fila[0]
                tasaString = fila[1]

                plazoMinimo = [int(s) for s in plazoString.split() if s.isdigit()][0]
                if 'Años' in plazoString:
                    plazoMinimo = plazoMinimo * 365
                tasa = float(tasaString.strip().strip('%').replace(',', '.'))

                tasas[plazoMinimo] = tasa

    return tasas
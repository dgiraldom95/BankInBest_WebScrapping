from pathlib import Path
from bs4 import BeautifulSoup
import requests
import tabula
from CDT import CDT


def obtenerCDT():
    # El url que tiene las tasas
    url = 'https://www.bancoomeva.com.co/publicaciones.php?id=36226'

    # El html de la pagina de las tasas
    html = requests.get(url).content

    # Se instancia un BeautifulSoup a partir del html
    soup = BeautifulSoup(html, 'html.parser')

    # Las tasas estan en un archivo pdf, el tag del link tiene el texto Tasas Vigentes
    a = soup.find('a', title='Tasas AQUÍ')

    # El url del pdf
    linkPDF = a['href']

    # El archivo donde se va a guardar el pdf
    nombrePDF = 'CDTBancoomeva.pdf'
    file = Path(nombrePDF)

    # Guardar el pdf
    pdfResponse = requests.get('https://www.bancoomeva.com.co/' + linkPDF)
    file.write_bytes(pdfResponse.content)

    # Lee el area marcada del pdf (top, left, bottom, right) y lo convierte a un dataframe
    df = tabula.read_pdf(nombrePDF, relative_area=True, area=(65, 30, 86, 100))
    # Convierte el dataframe a una lista de listas
    info = df.values.tolist()

    listaCDTs = []
    for fila in info:
        for col in fila:
            if isinstance(col, str) and '%' in col:
                plazoString = fila[1]
                tasaString = fila[3]

                plazoString = plazoString.replace('y', ' ')  # Porque los números estan quedando sin espacio
                plazoMinimo = [int(s) for s in plazoString.split() if s.isdigit()][0]

                tasa = float(tasaString.strip().strip('%').replace(',', '.'))

                cdt = CDT('Bancoomeva', plazoMinimo, tasa, None, 300_000)
                listaCDTs.append(cdt)

    return listaCDTs

from pathlib import Path
from bs4 import BeautifulSoup
import requests
import tabula

class cdtWWB:
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

    url = 'https://www.bancow.com.co/wp-content/uploads/2019/03/Precios-y-tarifas-vigentes-cdt-marzo-26-2019.pdf'

    nombrePDF = "CDTBancoWWB.pdf"
    file = Path(nombrePDF)

    pdfResponse = requests.get(url)
    file.write_bytes(pdfResponse.content)

    df = tabula.read_pdf(nombrePDF)
    #print(df)

    info = df.values.tolist()
    #print(info)

    rangos = [info[0][1], info[0][2],info[0][3],info[0][4],info[0][5],info[0][6],info[0][7],info[1][8]]

    cdts = []

    for fila in info:
        filaActual = info.index(fila)
        if filaActual >= 2 and filaActual <= 5:
            for col in fila:
                colActual = fila.index(col)
                monto = info[filaActual][0]
                if colActual > 0:
                    porcentaje = info[filaActual][colActual]
                    rangoo = rangos[colActual-1]
                    cdt = cdtWWB(monto, rangoo,porcentaje)
                    cdts.append(cdt)
    return cdts
from pathlib import Path
import requests
import tabula
from CDT import CDT
import re
import os

def obtenerCDT():
    #El url del pdf que tiene las tasas
    url = 'https://www.bancocajasocial.com/sites/default/files/files/tasascdt.pdf'

    #El archivo donde se va a guardar el pdf
    nombrePDF = "CDTBancoCajaSocial.pdf"
    file = Path(nombrePDF)

    #Guardar el pdf
    pdfResponse = requests.get(url)
    file.write_bytes(pdfResponse.content)

    # Lee el area marcada del pdf (top, left, bottom, right) y lo convierte a un dataframe
    df = tabula.read_pdf(nombrePDF, relative_area=True, area=(25, 6, 75, 94))

    info = df.values.tolist()

    montoMin = int(''.join(x for x in info[2][2] if x.isdigit()))
    listaCdts =[]
    i = 0
    for fila in info:
        if i in range(5,10):
            plazoDias = int(re.search(r'\d+', fila[0]).group())
            tasa = float(fila[1].strip('%'))
            cdt = CDT('Banco Caja Social', plazoDias, tasa, montoMin, None)
            listaCdts.append(cdt)
        i += 1

    os.remove(nombrePDF)

    return listaCdts
    # PARA CUANDO USEMOS LOS RANGOS DE DINERO
    # alto = len(info) - 5
    # ancho = len(info[0])
    # cdts = [["" for x in range(ancho)] for y in range(alto)]
    # cdts[0][0] = "Rangos balance"
    #
    #
    # for fila in info:
    #     #Extraigo los plazos de cada cdt
    #     filaActual = info.index(fila)
    #     if 5 <= filaActual <= 9:
    #         plazos = map(int, re.findall(r'\d+', fila[0]))
    #         plazoCDT = "/"
    #         for valor in plazos:
    #             plazoCDT += str(valor) + "/"
    #         cdts[filaActual-4][0] = plazoCDT
    #
    #     #Verifico los cdts
    #     for col in fila:
    #         indCol = fila.index(col)
    #         if isinstance(col, str) and '$' in col:
    #             if indCol != 3:
    #                 if indCol != 2:
    #                     if cdts[0][indCol] == "":
    #                         cdts[0][indCol] = col
    #                     else:
    #                         cdts[0][indCol] += "-" + col
    #                 else:
    #                     if cdts[0][indCol] == "":
    #                         cdts[0][indCol] = col.split(" ")[0]
    #                         cdts[0][indCol+1] = col.split(" ")[1]
    #                     else:
    #                         cdts[0][indCol] += "-" + col.split(" ")[0]
    #                         cdts[0][indCol+1] += "-" + col.split(" ")[1]
    #         elif isinstance(col, str) and '%' in col:
    #             temp = col.strip().strip('%').replace(',', '.')
    #             if indCol != 3:
    #                 try:
    #                     cdts[filaActual-4].index(temp)
    #                     cdts[filaActual-4][cdts[filaActual-4].index('')] = temp
    #                 except:
    #                     if indCol != 2:
    #                         cdts[filaActual-4][indCol] = col.strip().strip('%').replace(',', '.')
    #                     else:
    #                         cdts[filaActual-4][indCol] = col.split(" ")[0].strip().strip('%').replace(',', '.')
    #                         cdts[filaActual-4][indCol+1] = col.split(" ")[1].strip().strip('%').replace(',', '.')



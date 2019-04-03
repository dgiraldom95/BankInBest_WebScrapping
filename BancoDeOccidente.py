from pathlib import Path
import requests
import tabula
from CDT import CDT


def obtenerCDT():

    # url del pdf que contiene las tasas
    url = 'https://www.bancodeoccidente.com.co/wps/wcm/connect/banco-de-occidente/c24390e8-b984-44de-b427-e59ff152a22c/tasas-personas-2019.pdf?MOD=AJPERES&CVID=mCXPoS8'

    # El archivo donde se va a guardar el pdf
    nombrePDF = "CDTBancoDeOccidente.pdf"
    file = Path(nombrePDF)

    # guardar el pdf
    pdfResponse = requests.get(url)
    file.write_bytes(pdfResponse.content)

    # Lee el area marcada del pdf (top, left, bottom, right) y lo convierte a un dataFrame
    df = tabula.read_pdf(nombrePDF, pages=5, relative_area= True, area=(19, 72, 34, 94))

    info = df.values.tolist()

    listaCDTs = []

    for i in info:
        dias = ""

        for j in i:

            if str(j) == "nan":
                break
            else:

                if(dias == ""):
                    jAct = str(j)[:4]
                    jAct = jAct.strip("D")
                    jAct = jAct.strip()
                    dias = jAct
                else:
                    jtasas = j.replace(',', '.')
                    jtasas = jtasas.split("%")
                    del jtasas[3]

                    t = 0
                    for ts in jtasas:
                        montoMin = 0

                        if(t == 0):
                            montoMin = 1000000
                        elif(t == 1):
                            montoMin = 100000000
                        else:
                            montoMin = 500000000

                        cdt = CDT('Banco de Occidente',int(dias),float(ts),None,int(montoMin))
                        listaCDTs.append(cdt)
                        t +=1
    return listaCDTs

from pathlib import Path
import requests
import tabula

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

    tasas = {}

    for i in info:
        dia = ''
        entroDia = False
        for j in i:

            if str(j) == 'nan':
                break

            else:

                if entroDia == True:
                    jTas = str(j)[:4]
                    jTas = jTas.replace(',','.')
                    jTas = jTas.strip()
                    tasas[dia] = jTas
                    break


                else:
                    jAct = str(j)[:4]
                    jAct = jAct.strip("D")
                    jAct = jAct.strip()

                    if jAct in tasas:
                        break

                    tasas[jAct] = 0

                    dia = jAct
                    entroDia = True

    return tasas

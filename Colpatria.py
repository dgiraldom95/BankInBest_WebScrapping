from pathlib import Path
import requests
import tabula
from CDT import CDT



def obtenerCDT():
    #url del pdf que contiene las tasas
    url = 'https://cdn.agilitycms.com/scotiabank-colombia/Colpatria/pdf/acerca-de/tasas/Tasas-CDT-personas.pdf'

    #El archivo donde se va a guardar el pdf
    nombrePDF = "CDTColpatria.pdf"
    file = Path(nombrePDF)

    #guardar el pdf
    pdfResponse = requests.get(url)
    file.write_bytes(pdfResponse.content)

    # Lee el area marcada del pdf (top, left, bottom, right) y lo convierte a un dataFrame
    df = tabula.read_pdf(nombrePDF, relative_area= True, area=(25, 6, 75, 94))

    #dataFrame convertifo en lista
    info = df.values.tolist()

    print(info)

    listaCDTs = []

    plazos = []

    for i in info:
        entroPlazo = False
        montoAct = ""
        k=0
        for j in i:

            if str(j) == 'MESES' or str(j) == 'RANGOS':
                break

            elif str(j) == 'PLAZO' or entroPlazo == True:
                if str(j) == 'PLAZO':
                    entroPlazo = True
                elif(entroPlazo == True):

                    jAct = str(j)[0:3]
                    jAct = jAct.strip('-')

                    if (str(j).startswith('>')):
                        jAct = str(j)[-4:]
                        jAct = jAct.strip()

                    if jAct != 'nan':
                        plazos.append(jAct)

            else:

                if str(j) == '1.000.000 49.999.999':
                    montoAct = 1000000
                    continue
                elif str(j) == '50.000.000 99.999.999':
                    montoAct = 50000000
                    continue
                elif str(j) == '100.000.000 499.999.999':
                    montoAct = 100000000
                    continue
                elif str(j) == '> 500.000.000':
                    montoAct = 500000000
                    continue

                if str(j) == 'nan':
                    continue
                else:

                    dias = plazos[k]

                    jAct = str(j).strip('%')
                    jAct = jAct.replace(',', '.')


                    cdt = CDT('Colpatria', dias, jAct, None, montoAct)
                    listaCDTs.append(cdt)

                    k+=1

    return listaCDTs

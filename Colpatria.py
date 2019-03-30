from pathlib import Path
import requests
import tabula


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

    tasas = {}


    #variable para romper el for cuando tengamos toda la info
    k = 0

    for i in info:

        entroPlazo = False
        entroTasa = False
        if k != 0:
            break

        for j in i:

            #Extraer dias en la fila de plazos
            if str(j) == 'PLAZO':
                entroPlazo = True

            elif entroPlazo == True:

                jAct = str(j)[0:3]
                jAct =jAct.strip('-')

                if(str(j).startswith('>')):
                    jAct = str(j)[-4:]
                    jAct = jAct.strip()

                if jAct != 'nan':
                    tasas[jAct] = 0


            #extraer tasas en la fila de primer rango
            if str(j) == '1.000.000 49.999.999':
                entroTasa = True
            elif entroTasa == True:
                jAct = str(j).strip('%')
                jAct = jAct.replace(',','.')

                if jAct != 'nan':

                    #itero sobre las llaves del diccionario en orden
                    llaves = list(tasas)
                    llaveAct = llaves[k]

                    tasas[llaveAct] = jAct

                    k += 1
    return tasas

import requests
from bs4 import BeautifulSoup
import bs4


def obtenerCalificacion():
    # El url que tiene la calificacion
    url = 'http://www.brc.com.co/calificaciones_busqueda.php?fecha_desde=&fecha_hasta=&cliente=BANCO+W+S.+A.&subsector=&tipo_calificacion=&tipo_revision=&vigencia=&tipo_escala=&Submit=Realizar+B%FAsqueda'

    # El html de la pagina de la calificacion
    html = requests.get(url).content

    # Se instancia un BeautifulSoup a partir del html
    soup = BeautifulSoup(html, 'html.parser')

    myTable = soup.find('table', {'bgcolor': '#FFFFFF'})

    # diccionario que contiene el banco y su calificacion a largo plazo
    resp = {}

    filas = []  # filas de la tabla

    # Se recorren las filas de las tabla (<tr>)
    for child in myTable.children:
        if len(filas) >= 3:
            break  # solo capturamos la calificacion de la primera fila que es la ultima calificacion recibida.
        if type(child) is bs4.Tag:  # Solo nos interesan los hijos de tipo bs4.Tag
            cols = []  # Columnas en la fila de la tabla
            # Se obtienen los hijos de la <tr>, los <td>
            for td in child.children:
                if type(td) is bs4.Tag or type(td):
                    if td.string == None:
                        a = str(td).split(">")
                        val = a[1]
                        b = val.split("<")
                        final = str(b[0]).strip()

                        if len(resp) != 0 and final != "":
                            for i in resp:
                                resp[i] = final
                                break
                        elif len(resp) == 0:
                            resp[final] = ""

                        cols.append(final)
                    else:
                        cols.append(td.string)  # Se agrega a la lista de las columnas el contenido del <td>

            filas.append(cols)  # Se agrega a la lista de las filas la lista de las columnas de esa fila

    return resp

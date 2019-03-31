import BancoDeBogota
import Bancolombia
import Pichincha
import BBVA
import BancoCajaSocial
import AvVillas
import Bancoomeva
import Falabella
import WWB
import Davivienda
from CDT import CDT

funcionesCDTS = [
    Pichincha.obtenerCDT,
    AvVillas.obtenerCDT,
    BancoCajaSocial.obtenerCDT,
    Bancolombia.obtenerCDT,
    Bancoomeva.obtenerCDT,
    BBVA.obtenerCDT,
    Davivienda.obtenerCDT,
    Falabella.obtenerCDT,
    WWB.obtenerCDT,
]

if __name__ == '__main__':
    opcion = 0

    if opcion == 0:
        for funcionCdt in funcionesCDTS:
            try:
                listaCDTsBanco = funcionCdt()
                for cdt in listaCDTsBanco:
                    if isinstance(cdt, CDT):
                        cdt.POST('http://127.0.0.1:8000')
            except:
                continue

    if opcion == 1:
        tasas = BancoDeBogota.obtenerCDT()
        print(tasas)

    elif opcion == 2:
        tasas = Bancolombia.obtenerCDT()
        print(tasas)

    elif opcion == 3:
        tasas = Pichincha.obtenerCDT()
        print(tasas)

    elif opcion == 4:
        tasas = BBVA.obtenerCDT()
        print(tasas)

    elif opcion == 5:
        tasas = BancoCajaSocial.obtenerCDT()
        print(tasas)

    elif opcion == 6:
        tasas = Bancoomeva.obtenerCDT()
        print(tasas)

    elif opcion == 7:
        tasas = Falabella.obtenerCDT()
        print(tasas)

    elif opcion == 8:
        tasas = AvVillas.obtenerCDT()
        print(tasas)

    elif opcion == 9:
        tasas = WWB.obtenerCDT()
        print(tasas)

    elif opcion == 10:
        Davivienda.obtenerCDT()

import BancoDeBogota
import Bancolombia
import Pichincha
import BBVA
import BancoCajaSocial
import AvVillas
import Bancoomeva
import Falabella
import WWB

if __name__=='__main__':
    opcion = 7
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


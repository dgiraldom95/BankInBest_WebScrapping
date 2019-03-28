import BancoDeBogota
import Bancolombia
import Pichincha
import bbva
import BancoCajaSocial
import AvVillas
import Procredit
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
        tasas = bbva.obtenerCDT()
        print(tasas)

    elif opcion == 5:
        tasas = BancoCajaSocial.obtenerCDT()
        print(tasas)

    elif opcion == 6:
        tasas = AvVillas.obtenerCDT()
        print(tasas)

    elif opcion == 7:
        tasas = WWB.obtenerCDT()
        print(tasas)
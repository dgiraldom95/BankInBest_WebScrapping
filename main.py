import BancoDeBogota
import Bancolombia
import Pichincha
import BBVA
import BancoCajaSocial
import Bancoomeva

if __name__=='__main__':
    opcion = 6
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
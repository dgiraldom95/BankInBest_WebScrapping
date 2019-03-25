import BancoDeBogota
import Bancolombia
import Pichincha
import bbva

if __name__=='__main__':
    opcion = 4
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
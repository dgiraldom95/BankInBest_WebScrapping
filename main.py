import BancoDeBogota
import Bancolombia

if __name__=='__main__':
    opcion = 2
    if opcion == 1:
        tasas = BancoDeBogota.obtenerCDT()
        print(tasas)

    elif opcion == 2:
        tasas = Bancolombia.obtenerCDT()

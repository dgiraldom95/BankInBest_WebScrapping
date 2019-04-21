import BancoDeBogota
import Bancolombia
import Colpatria
import Pichincha
import BBVA
import BancoCajaSocial
import AvVillas
import Bancoomeva
import Falabella
import WWB
import Davivienda
import Itau
import BancoPopular
import BancoDeOccidente
from CDT import CDT
#importaciones de calificacion bancaria
from calificaciones import AvVillasCal
from calificaciones import BancoCajaSocialCal
from calificaciones import BancoDeBogotaCal
from calificaciones import BancoDeOccidenteCal
from calificaciones import BancolombiaCal
from calificaciones import BancoomevaCal
from calificaciones import BancoPopularCal
from calificaciones import BBVACal
from calificaciones import ColpatriaCal
from calificaciones import DaviviendaCal
from calificaciones import FalabellaCal
from calificaciones import ItauCal
from calificaciones import PichinchaCal
from calificaciones import WWBCal
from calificaciones.CalificacionBancaria import CalificacionBancaria




funcionesCDTS = [
    AvVillas.obtenerCDT,
    Bancolombia.obtenerCDT,
    BancoCajaSocial.obtenerCDT,
    Falabella.obtenerCDT,
    BancoDeBogota.obtenerCDT,
    BancoDeOccidente.obtenerCDT,
    Bancoomeva.obtenerCDT,
    BBVA.obtenerCDT,
    Colpatria.obtenerCDT,
    Davivienda.obtenerCDT,
    Itau.obtenerCDT,
    Pichincha.obtenerCDT,
    WWB.obtenerCDT,
]

funcionesCalificacion = [
    AvVillasCal.obtenerCalificacion,
    BancoCajaSocialCal.obtenerCalificacion,
    BancoDeBogotaCal.obtenerCalificacion,
    BancoDeOccidenteCal.obtenerCalificacion,
    BancolombiaCal.obtenerCalificacion,
    BancoomevaCal.obtenerCalificacion,
    BancoPopularCal.obtenerCalificacion,
    BBVACal.obtenerCalificacion,
    ColpatriaCal.obtenerCalificacion,
    DaviviendaCal.obtenerCalificacion,
    FalabellaCal.obtenerCalificacion,
    ItauCal.obtenerCalificacion,
    PichinchaCal.obtenerCalificacion,
    WWBCal.obtenerCalificacion,
]



if __name__ == '__main__':
    opcion = 0

    if opcion == 0:
        for funcionCdt in funcionesCDTS:
            try:
                listaCDTsBanco = funcionCdt()
                for cdt in listaCDTsBanco:
                    if isinstance(cdt, CDT):
                        cdt.POST('http://157.230.14.37:8000')
                print(funcionCdt, " TERMINO")
            except:
                print(funcionCdt, " FALLO")
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

    elif opcion == 11:
        Itau.obtenerCDT()

    elif opcion == 12:
        BancoPopular.obtenerCDT()

    #opcion para obtener las califiaciones Bancarias
    elif opcion == 13:
        for f in funcionesCalificacion:
            try:
                calificacion = f()
                calificacion.POST('http://157.230.14.37:8080')
                print(f ," TERMINO")
            except:
                print(f ," FALLO")
                continue




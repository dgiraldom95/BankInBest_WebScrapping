import requests
import json
import pprint


class CDT:

    def __init__(self, banco: str, plazoMinDias: int, tasaEA: float, montoInversion: int, montominimoPermitido: int):
        self.banco = banco
        self.plazoMinDias = plazoMinDias
        self.tasaEA = tasaEA
        self.montoInversion = montoInversion
        self.montominimo = montominimoPermitido

    def POST(self, urlBase):
        url = urlBase + '/api/CDTs/'

        data = {
            'banco': self.banco,
            'plazo_min_dias': self.plazoMinDias,
            'tasa': self.tasaEA,
            'monto': self.montoInversion,
            'monto_minimo': self.montominimo
        }

        r = requests.post(url, data=data)
        print(self.__repr__(), ' ', r.status_code, ' ', r.reason)
        pprint.pprint(json.loads(r.content))
        print('____________________________________________________')

    def __repr__(self):
        print('%s: p%d -> %.2f' % (self.banco, self.plazoMinDias, self.tasaEA))
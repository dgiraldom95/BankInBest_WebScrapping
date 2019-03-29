import requests

class CDT:

    def __init__(self, banco: str, tasaEA: float, montoInversion: int, montominimoPermitido: int):
        self.banco = banco
        self.tasaEA = tasaEA
        self.montoInversion = montoInversion
        self.montominimo = montominimoPermitido

    def POST(self, urlBase):
        url = urlBase + '/CDTs'

        data = {
            'banco': self.banco,
            'tasa': self.tasaEA,
            'monto': self.montoInversion,
            'montoMin': self.montominimo
        }

        r = requests.post(url, data=data)

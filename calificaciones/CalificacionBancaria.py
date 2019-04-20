import requests
import json
import pprint

class CalificacionBancaria:

    def __init__(self, banco: str, calificacion: str):
        self.banco = banco
        self.calificacion = calificacion

    def POST(self, urlBase):
        url = urlBase + '/api/calificacionBancaria/'

        data = {
            'banco': self.banco,
            'calificacion': self.calificacion
        }

        r = requests.post(url, data = data)
        print(self.__repr__(), ' ', r.status_code, ' ', r.reason)
        pprint.pprint(json.load(r.content))
        print('____________________________________________________')

    def __repr__(self):
        print(self.banco, self.calificacion)
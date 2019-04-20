import requests
import json
import pprint


class CalificacionBancaria:

    def __init__(self, banco: str, calificacion: str):
        self.banco = banco
        self.calificacion = calificacion

    def POST(self, urlBase):
        urlBanco = self.banco.replace(" ", "-")
        url = urlBase + '/api/bancos/' + urlBanco + "/"

        data = {
            'nombre': self.banco,
            'puntaje_bankinbest': self.calificacion
        }

        r = requests.patch(url, data=data)
        print(self.__repr__(), ' ', r.status_code, ' ', r.reason)
        pprint.pprint(json.loads(r.content))
        print('____________________________________________________')

    def __repr__(self):
        print(self.banco, self.calificacion)

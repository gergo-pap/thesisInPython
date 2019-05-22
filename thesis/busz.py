import json
import time

from thesis.utas import Utas


class Busz:
    def __init__(self, busz_jaratszam, kapacitas):
        self.megallok = []
        self.utasok = []
        self.aktualis_megallo = ""

        self.buszNev = busz_jaratszam
        self.busz_szabad_helyek_szama = kapacitas

    def json_beolvasasa(self, busz_jaratszam):
        with open('jaratok.json', encoding='utf-8') as data_file:
            data = json.load(data_file)
        return data[busz_jaratszam]["megallok"]  # data["160"]["megallok"][1]

    def jarat_initialize(self, busz_jaratszam):
        data = self.json_beolvasasa(busz_jaratszam)
        # if data["34"] == self.buszNev:
        for index, x in enumerate(data):
            megallo = x["name"]
            self.megallok.append(megallo)

    def busz_kozlekedik(self):
        utas = Utas.utas_generalas()

        for megallo in self.megallok:
            print(megallo)
            print(utas)

            time.sleep(.1)

    def aktualis_megallo_print(self):
        print(self.aktualis_megallo)

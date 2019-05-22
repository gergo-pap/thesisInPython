import json
import time

from Utas import Utas


class Busz:
    def __init__(self, buszJaratszam, kapacitas):
        self.megallok = []
        self.utasok = []
        self.aktualisMegallo = ""

        self.buszNev = buszJaratszam
        self.buszSzabadHelyekSzama = kapacitas

    def jSonBeolvasasa(self, buszJaratszam):
        with open('jaratok.json', encoding='utf-8') as data_file:
            data = json.load(data_file)
        return data[buszJaratszam]["megallok"]  #data["160"]["megallok"][1]

    def jaratInitialize(self, buszJaratszam):
        data = self.jSonBeolvasasa(buszJaratszam)
        # if data["34"] == self.buszNev:
        for index, x in enumerate(data):
            megallo = x["name"]
            self.megallok.append(megallo)

    def buszKozlekedik(self):
        utas = Utas.utasGeneralas()

        for megallo in self.megallok:
            print(megallo)
            print(utas)

            time.sleep(.1)

    def aktualisMegalloPrint(self):
        print(self.aktualisMegallo)

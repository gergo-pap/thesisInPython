import json
import time

from .Utas import *

megallok = []
utasok = []
aktualisMegallo = ""

class Busz():
    def __init__(self, buszJaratszam, kapacitas):
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
            megallok.append(megallo)


    def buszKozlekedik(self):
        utas = Utas.utasGeneralas(Utas)
        for megallo in megallok:
            print(megallo)
            print(utas)

            time.sleep(.1)

    def aktualisMegalloPrint(self):
        print(aktualisMegallo)

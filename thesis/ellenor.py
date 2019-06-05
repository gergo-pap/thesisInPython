from thesis.utas import Utas


class Ellenor:
    def buntet(self, utas: Utas):
        utas.utas_egyenleg -= 16000
        utas.utas_utazik_e = False
        print("Utas büntetve és leszállítva")

    def ellenoriz(self, utas: Utas):
        if not utas.utas_van_e_berlete:
            if not utas.utas_van_e_jegye:
                self.buntet(utas)

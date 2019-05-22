from Utas import Utas


class Ellenor():
    def buntet(self):
        Utas.utasEgyenleg -= 16000
        Utas.utasUtazikE = False
        print("Utas büntetve és leszállítva")

    def ellenoriz(self):
        if not Utas.utasVanEBerlete:
            if not Utas.utasVanEJegye:
                self.buntet(self)

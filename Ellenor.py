class Ellenor:
    def buntet(self, utas):
        utas.utasEgyenleg -= 16000
        utas.utasUtazikE = False
        print("Utas büntetve és leszállítva")

    def ellenoriz(self, utas):
        if not utas.utasVanEBerlete:
            if not utas.utasVanEJegye:
                self.buntet(utas)

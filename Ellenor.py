class Ellenor:
    def buntet(self, utas):
        utas.utas_egyenleg -= 16000
        utas.utas_utazik_e = False
        print("Utas büntetve és leszállítva")

    def ellenoriz(self, utas):
        if not utas.utas_van_e_berlete:
            if not utas.utas_van_e_jegye:
                self.buntet(utas)

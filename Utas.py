import random


class Utas:
    def __init__(self, utas_nev, utas_egyenleg, utas_van_e_berlete, utas_van_e_jegye, utas_utazik_e):
        self.utasNev = utas_nev
        self.utasEgyenleg = utas_egyenleg
        self.utasVanEBerlete = utas_van_e_berlete
        self.utasVanEJegye = utas_van_e_jegye
        self.utasUtazikE = utas_utazik_e

    @classmethod
    def utas_generalas(cls):
        return cls(
            utas_nev=cls.utas_nev_generator(),
            utas_egyenleg=random.randint(0, 50000),
            utas_van_e_berlete=cls.percent_base_true_or_false(70),
            utas_van_e_jegye=cls.percent_base_true_or_false(25),
            utas_utazik_e=False
        )

    def utas_felszall(self):
        self.utasUtazikE = True

    def utas_leszall(self):
        self.utasUtazikE = False

    def utas_jegyet_elhasznal(self):
        if self.utasVanEJegye:
            self.utasVanEJegye = False
        else:
            print("Nem volt jegye az utasnak")

    def utas_jegyet_vesz(self):
        if self.utasEgyenleg > 450:
            self.utasEgyenleg -= 450
            self.utasVanEJegye = True
            print("Vett jegyet")
        else:
            print("Nincs elég pénze jegyre")

    @classmethod
    def utas_nev_generator(cls):
        last_names = ("Kis", "Nagy", "Kovács", "Pap", "Szabó",
                     "Kovács", "Szűcs", "Barta", "Garaba", "Botos", "Kozma", "Szász", "Simon", "Pupek",
                     "Pomozi", "Fülöp", "Horváth", "Balogh", "Szilágyi", "Illyés", "Németh", "Csontos", "Fekete",
                     "Takács", "Détár", "Cinkóczi")
        first_names = ("András", "Virág", "Gábor", "Dóri", "Balázs", "Kristóf",
                  "Ádám", "Zoltán", "Anita", "Nikoletta", "Klári", "Zita", "Csilla", "Adrián", "Marci",
                  "Tímea", "Dominik", "Edina", "Bianka", "Marcell")

        return random.choice(last_names) + " " + random.choice(first_names)

    @classmethod
    def percent_base_true_or_false(cls, percent):
        return True if percent > random.randint(0, 100) else False

import random


class Utas:
    def __init__(self, utas_nev, utas_egyenleg, utas_van_e_berlete, utas_van_e_jegye, utas_utazik_e):
        self.utasNev = utas_nev
        self.utas_egyenleg = utas_egyenleg
        self.utas_van_e_berlete = utas_van_e_berlete
        self.utas_van_e_jegye = utas_van_e_jegye
        self.utas_utazik_e = utas_utazik_e

    @classmethod
    def utas_generalas(cls) -> "Utas":
        return cls(
            utas_nev=cls.utas_nev_generator(),
            utas_egyenleg=random.randint(0, 50000),
            utas_van_e_berlete=cls.percent_base_true_or_false(70),
            utas_van_e_jegye=cls.percent_base_true_or_false(25),
            utas_utazik_e=False
        )

    def utas_felszall(self):
        self.utas_utazik_e = True

    def utas_leszall(self):
        self.utas_utazik_e = False

    def utas_jegyet_elhasznal(self):
        if self.utas_van_e_jegye:
            self.utas_van_e_jegye = False
        else:
            print("Nem volt jegye az utasnak")

    def utas_jegyet_vesz(self):
        if self.utas_egyenleg > 450:
            self.utas_egyenleg -= 450
            self.utas_van_e_jegye = True
            print("Vett jegyet")
        else:
            print("Nincs elég pénze jegyre")

    @classmethod
    def utas_nev_generator(cls) -> str:
        last_names = ("Kis", "Nagy", "Kovács", "Pap", "Szabó",
                     "Kovács", "Szűcs", "Barta", "Garaba", "Botos", "Kozma", "Szász", "Simon", "Pupek",
                     "Pomozi", "Fülöp", "Horváth", "Balogh", "Szilágyi", "Illyés", "Németh", "Csontos", "Fekete",
                     "Takács", "Détár", "Cinkóczi")
        first_names = ("András", "Virág", "Gábor", "Dóri", "Balázs", "Kristóf",
                  "Ádám", "Zoltán", "Anita", "Nikoletta", "Klári", "Zita", "Csilla", "Adrián", "Marci",
                  "Tímea", "Dominik", "Edina", "Bianka", "Marcell")

        return random.choice(last_names) + " " + random.choice(first_names)

    @classmethod
    def percent_base_true_or_false(cls, percent: int):
        return True if percent > random.randint(0, 100) else False

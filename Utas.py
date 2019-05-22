import random


class Utas:
    def __init__(self, utasNev, utasEgyenleg, utasVanEBerlete, utasVanEJegye, utasUtazikE):
        self.utasNev = utasNev
        self.utasEgyenleg = utasEgyenleg
        self.utasVanEBerlete = utasVanEBerlete
        self.utasVanEJegye = utasVanEJegye
        self.utasUtazikE = utasUtazikE

    @classmethod
    def utasGeneralas(cls):
        return cls(
            utasNev=cls.utasNevGenerator(),
            utasEgyenleg=random.randint(0, 50000),
            utasVanEBerlete=cls.percentBaseTrueOrFalse(70),
            utasVanEJegye=cls.percentBaseTrueOrFalse(25),
            utasUtazikE=False
        )

    def utasFelszall(self):
        self.utasUtazikE = True

    def utasLeszall(self):
        self.utasUtazikE = False

    def utasJegyetElhasznal(self):
        if self.utasVanEJegye:
            self.utasVanEJegye = False
        else:
            print("Nem volt jegye az utasnak")

    def utasJegyetVesz(self):
        if self.utasEgyenleg > 450:
            self.utasEgyenleg -= 450
            self.utasVanEJegye = True
            print("Vett jegyet")
        else:
            print("Nincs elég pénze jegyre")

    @classmethod
    def utasNevGenerator(cls):
        Beginning = ("Kis", "Nagy", "Kovács", "Pap", "Szabó",
                     "Kovács", "Szűcs", "Barta", "Garaba", "Botos", "Kozma", "Szász", "Simon", "Pupek",
                     "Pomozi", "Fülöp", "Horváth", "Balogh", "Szilágyi", "Illyés", "Németh", "Csontos", "Fekete",
                     "Takács", "Détár", "Cinkóczi")
        Middle = ("András", "Virág", "Gábor", "Dóri", "Balázs", "Kristóf",
                  "Ádám", "Zoltán", "Anita", "Nikoletta", "Klári", "Zita", "Csilla", "Adrián", "Marci",
                  "Tímea", "Dominik", "Edina", "Bianka", "Marcell")

        return random.choice(Beginning) + " " + random.choice(Middle)

    @classmethod
    def percentBaseTrueOrFalse(cls, percent):
        return True if percent > random.randint(0, 100) else False

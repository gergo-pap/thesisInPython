from Busz import Busz
from Utas import Utas


def main():
    random_utas = Utas.utasGeneralas()

    busz_34 = Busz("34", 50)
    busz_34.jSonBeolvasasa("160")
    busz_34.jaratInitialize("160")
    busz_34.buszKozlekedik()


if __name__ == "__main__":
    main()

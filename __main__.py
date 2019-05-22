from busz import Busz
from utas import Utas


def main():
    random_utas = Utas.utas_generalas()

    busz_34 = Busz("34", 50)
    busz_34.json_beolvasasa("160")
    busz_34.jarat_initialize("160")
    busz_34.busz_kozlekedik()


if __name__ == "__main__":
    main()

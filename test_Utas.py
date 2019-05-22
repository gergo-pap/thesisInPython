from Utas import Utas


def utas_nev():
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasNev == "joco"


def utas_egyenleg():
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasEgyenleg == 300


def utas_van_e_berlete():
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasVanEBerlete == True


def utas_van_e_jegye():
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasVanEJegye == False


def utas_utazik_e():
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasUtazikE == False

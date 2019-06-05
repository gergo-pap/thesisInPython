from thesis.utas import Utas


def test_utas_nev():
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasNev == "joco"


def test_utas_egyenleg():
    joco = Utas("joco", 300, True, False, False)
    assert joco.utas_egyenleg == 300


def test_utas_van_e_berlete():
    joco = Utas("joco", 300, True, False, False)
    assert joco.utas_van_e_berlete == True


def test_utas_van_e_jegye():
    joco = Utas("joco", 300, True, False, False)
    assert joco.utas_van_e_jegye == False


def test_utas_utazik_e():
    joco = Utas("joco", 300, True, False, False)
    assert joco.utas_utazik_e == False

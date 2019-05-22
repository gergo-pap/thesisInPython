from Utas import Utas


def utasNev():
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasNev == "joco"


def utasEgyenleg():
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasEgyenleg == 300


def utasVanEBerlete():
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasVanEBerlete == True


def utasVanEJegye():
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasVanEJegye == False


def utasUtazikE():
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasUtazikE == False

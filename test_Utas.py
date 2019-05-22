import pytest
from Utas import *


def utasNev(self):
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasNev == "joco"


def utasEgyenleg(self):
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasEgyenleg == 300


def utasVanEBerlete(self):
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasVanEBerlete == True


def utasVanEJegye(self):
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasVanEJegye == False


def utasUtazikE(self):
    joco = Utas("joco", 300, True, False, False)
    assert joco.utasUtazikE == False

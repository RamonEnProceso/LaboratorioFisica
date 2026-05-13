import math
from .calcEpsilon import calcEpsilon

def calcCilinderR (d, h):
    return (math.pi * (d**2)*h / 4)

def calcCilinderErr (vr, ed, eh):
    return vr*((2*ed)+eh)
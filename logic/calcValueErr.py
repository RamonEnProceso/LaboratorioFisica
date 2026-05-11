from .calcMaxMin import calcMaxMin
from .calcEpsilon import calcEpsilon
from .calcCilinder import calcCilinderR, calcCilinderErr
from .calcRound import roundCatedra

def calcValueErr(data,instrumento):
    
    dataPlus = {}
    
    dataPlus["diametroErrMax"], dataPlus["diametroErrMin"] = calcMaxMin(
        data[instrumento]["medida"]["diametro"], data[instrumento]["err"])
    
    dataPlus["volumenInicial"] = calcCilinderR(
        data[instrumento]["medida"]["diametro"], 
        data[instrumento]["medida"]["altura"])
    
    dataPlus["alturaErrMax"], dataPlus["alturaErrMin"] = calcMaxMin(
        data[instrumento]["medida"]["altura"], data[instrumento]["err"])
    
    dataPlus["epsilonDiametro"] = calcEpsilon(
        data[instrumento]["medida"]["diametro"],
        data[instrumento]["err"])
    
    dataPlus["epsilonAltura"] = calcEpsilon(
        data[instrumento]["medida"]["altura"],
        data[instrumento]["err"])
    
    dataPlus["cilindroErr"] = calcCilinderErr(dataPlus["volumenInicial"],dataPlus["epsilonDiametro"],dataPlus["epsilonAltura"])
    
    dataPlus["volumen"] = roundCatedra(dataPlus["volumenInicial"],dataPlus["cilindroErr"])
    
    return dataPlus

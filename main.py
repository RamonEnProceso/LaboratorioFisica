import matplotlib.pyplot as plt
from utils.load import returnJSON
from logic.calcValueErr import calcValueErr
from utils.chart import chart

def main ():
    
    data = returnJSON("data/medidas.json")
    
    #Gráfico comparativo de la altura
    
    chart(
        calcValueErr(data, "regla")["alturaErrMax"],calcValueErr(data, "regla")["alturaErrMin"],
        data["regla"]["medida"]["altura"],
        calcValueErr(data, "regla")["alturaErrMax"],calcValueErr(data, "regla")["alturaErrMin"],
        "Hr",
        0
          )
    chart(
        calcValueErr(data, "regla")["alturaErrMax"],calcValueErr(data, "regla")["alturaErrMin"],
        data["calibre"]["medida"]["altura"],
        calcValueErr(data, "calibre")["alturaErrMax"],calcValueErr(data, "calibre")["alturaErrMin"],
        "Hc",
        0.5
          )
    plt.show()
    
    #/////////////////////
    #Gráfico comparativo del diámetro
    
    chart(
        calcValueErr(data, "regla")["diametroErrMax"],calcValueErr(data, "regla")["diametroErrMin"],
        data["regla"]["medida"]["diametro"],
        calcValueErr(data, "regla")["diametroErrMax"],calcValueErr(data, "regla")["diametroErrMin"],
        "Dr",
        0
          )
    chart(
        calcValueErr(data, "regla")["diametroErrMax"],calcValueErr(data, "regla")["diametroErrMin"],
        data["calibre"]["medida"]["diametro"],
        calcValueErr(data, "calibre")["diametroErrMax"],calcValueErr(data, "calibre")["diametroErrMin"],
        "Dc",
        0.5
          )
    
    plt.show()
    
    #/////////////////////
    #Gráfico comparativo de volumen del cilindro
    
    chart(
        calcValueErr(data, "regla")["volumenErrMax"],calcValueErr(data, "regla")["volumenErrMin"],
        calcValueErr(data, "regla")["volumen"][0],
        calcValueErr(data, "regla")["volumenErrMax"],calcValueErr(data, "regla")["volumenErrMin"],
        "Vr",
        0
          )
    chart(
        calcValueErr(data, "regla")["volumenErrMax"],calcValueErr(data, "regla")["volumenErrMin"],
        calcValueErr(data, "calibre")["volumen"][0],
        calcValueErr(data, "calibre")["volumenErrMax"],calcValueErr(data, "calibre")["volumenErrMin"],
        "Vc",
        0.5
          )
    
    plt.show()
    
    
    


main()
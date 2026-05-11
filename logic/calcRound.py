import math

def roundCatedra(v,err):
    orden = math.floor(math.log10(abs(err)))
    
    return round(v, -orden),  round(err, -orden)
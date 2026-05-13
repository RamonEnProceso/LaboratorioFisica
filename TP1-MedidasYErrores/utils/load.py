import json

def returnJSON (string):
    with open(string, "r") as archivo:
        data = json.load(archivo)
    
    return data
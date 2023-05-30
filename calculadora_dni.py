letras = ["T", "R", "W", "A", "G",
           "M", "Y", "F", "P", "D", 
           "X", "B", "N", "J", "Z", 
           "S", "Q", "V", "H", "L", 
           "C", "K", "E"
           ]
           

cantidad_letras = len(letras)
def calculadoraDNI(numero_dni):
    numero_dni = int(numero_dni)
    print(numero_dni)
    return letras[numero_dni % cantidad_letras]






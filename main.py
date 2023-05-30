from calculadora_dni import calculadoraDNI

def pideUnNum():
    # numero_dni = "01234567"
    kk = input("dame veneno ")
    print(kk)
    numero_dni = str(input("Dime un numero de 8 digitos:"))
    print(numero_dni)

    return (numero_dni)

numero_dni = pideUnNum()
letra_dni = calculadoraDNI(numero_dni)

numero_dni = str(numero_dni)
print("El dni calculado: " + (numero_dni) + "-" + (letra_dni))

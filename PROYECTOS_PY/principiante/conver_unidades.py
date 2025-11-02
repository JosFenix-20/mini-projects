# Conversor de unidades
# Temperatura, monedas, distancias.
# Modularización del código.
# Uso de diccionarios y condicionales.

dic_temp={
    'C':1,
    'F':1000,
    'K':273.15,
}
dic_dist={
    'm':1,
    'km':1000,
    'mi':1609.34,
    'ft':0.3048
}
dic_mone={
    'USD':1.0,
    'EUR':0.85,
    'PEN':3.7,
    'JPY':110.0
}

def menu():
    print(".: CONVERSOR :.")
    print("--------------------")
    print("Que conversion desea realizar")
    print("--------------------")
    print("1. temperatura\n2. distancia\n3. moneda\n4. salir")
    print("--------------------")
    OpTeclado=int(input("Escriba su apccion: "))
    if(OpTeclado==4):
        pass
    else:
        Operaciones(OpTeclado)

def Operaciones(OpTeclado):
        valor=float(input("VALOR: "))
        unidad_in=input("UNIDAD INICIAL: ")
        unidad_out=input("UNIDAD FINAL: ")
        match OpTeclado:
            case 1:
                if(unidad_in in dic_temp or unidad_out in dic_temp):
                    if unidad_in == unidad_out:
                        print(valor)
                    if unidad_in == 'C':
                        if unidad_out == 'F':
                            print((valor * 9/5) + 32)
                        elif unidad_out == 'K':
                            print(valor + 273.15)
                    elif unidad_in == 'F':
                        if unidad_out == 'C':
                            print((valor - 32) * 5/9)
                        elif unidad_out == 'K':
                            print((valor - 32) * 5/9 + 273.15)
                    elif unidad_in == 'K':
                        if unidad_out == 'C':
                            print(valor - 273.15)
                        elif unidad_out == 'F':
                            print((valor - 273.15) * 9/5 + 32)
                    print("Unidades no válidas")
            case 2:
                if(unidad_in in dic_dist or unidad_out in dic_dist):
                    valor_m = valor * dic_dist[unidad_in]
                    convertido = valor_m / dic_dist[unidad_out]
                    print(convertido)
            case 3:
                if(unidad_in in dic_mone or unidad_out in dic_mone):
                    valor_USD = valor / dic_mone[unidad_in]
                    convertido = valor_USD * dic_mone[unidad_out]
                    print(convertido)
            case _: 
                exit()
        input()
        menu()

print(menu())
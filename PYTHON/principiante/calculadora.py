# Calculadora con interfaz de consola
# Operaciones básicas.
# Uso de funciones.
# Ideal para practicar entrada/salida de datos.
from math import pow
def menu():
    print(".: CALCULADORA :.")
    print("--------------------")
    print("Que operacion desea realizar")
    print("--------------------")
    print("1. SUMA\n2. RESTAR\n3. MULTIPLICAR\n4. DIVIDIR\n5. POTENCIA")
    print("6. RAIZ\n7. PORCENTAJE\n8. MODULO\n9. SALIR")
    print("--------------------")
    OpTeclado=int(input("Escriba su apccion: "))
    if(OpTeclado==9):
        N_1=1
        N_2=1
    else:
        print("--------------------")
        print("ingrese dos numeros: ")
        band=True
        while(band):
            N_1=input("Numero 1: ")
            N_2=input("Numero 2: ")
            if((N_1.isdigit()) and (N_2.isdigit())):
                N_1=int(N_1)
                N_2=int(N_2)
                band=False
        print("--------------------")
    
    try:
        Operaciones(OpTeclado,N_1,N_2)
    except SyntaxError:
        print("error al ejeutar")

def Operaciones(OpTeclado,N_1,N_2):
    with open('historia_calculadora.txt','a') as arch:
        match OpTeclado:
            case 1:
                resultado=N_1+N_2 
                print(resultado)
                arch.write(f"{N_1}+{N_2}={resultado}\n")
            case 2:
                resultado=N_1-N_2
                print(resultado)
                arch.write(f"{N_1}-{N_2}={resultado}\n")
            case 3:
                resultado=N_1*N_2
                print(resultado)
                arch.write(f"{N_1}*{N_2}={resultado}\n")
            case 4:
                if(N_2!=0):
                    resultado=N_1/N_2 
                    print(resultado)
                    arch.write(f"{N_1}/{N_2}={resultado}\n")
                else:"no es posible la operacion"
            case 5:
                resultado=pow(N_1,N_2)
                print(resultado)
                arch.write(f"{N_1}^{N_2}={resultado}\n")
            case 6:
                N_2=1/N_2
                resultado=pow(N_1,N_2)
                print(resultado)
                arch.write(f"{N_1}^{N_2}={resultado}\n")
            case 7:
                resultado=(N_1/N_2)*100
                print(resultado,"%")
                arch.write(f"({N_1}/{N_2})*100={resultado}%\n")
            case 8:
                resultado=N_1//N_2
                print(resultado)
                arch.write(f"{N_1}mod({N_2})={resultado}\n")
            case _: 
                arch.close()
                exit()
        input()
        menu()

print(menu())
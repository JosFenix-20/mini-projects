import secrets
import string

# Función para generar una contraseña segura
def generar_contraseña(longitud, usar_letras=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ''
    if usar_letras:
        caracteres += string.ascii_letters  # Letras mayúsculas y minúsculas
    if usar_numeros:
        caracteres += string.digits         # Números del 0 al 9
    if usar_simbolos:
        caracteres += string.punctuation    # Símbolos como !@#$%

    if not caracteres:
        raise ValueError("Debes seleccionar al menos un tipo de carácter.")

    # Generar la contraseña usando secrets para mayor seguridad
    return ''.join(secrets.choice(caracteres) for _ in range(longitud))

# Función para guardar contraseñas en un archivo .txt
def guardar_contraseñas(lista_contraseñas, nombre_archivo="contraseñas_generadas.txt"):
    with open(nombre_archivo, 'w') as archivo:
        for i, contraseña in enumerate(lista_contraseñas, 1):
            archivo.write(f"Contraseña {i}: {contraseña}\n")
    print(f"✅ Contraseñas guardadas en '{nombre_archivo}'")

# Interfaz básica en consola
def main():
    try:
        cantidad = int(input("¿Cuántas contraseñas deseas generar? "))
        longitud = int(input("¿Qué longitud debe tener cada contraseña? "))
        incluir_letras = input("¿Incluir letras? (s/n): ").lower() == 's'
        incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
        incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

        contraseñas = [
            generar_contraseña(longitud, incluir_letras, incluir_numeros, incluir_simbolos)
            for _ in range(cantidad)
        ]

        print("\n🔐 Contraseñas generadas:")
        for i, pwd in enumerate(contraseñas, 1):
            print(f"{i}: {pwd}")

        guardar = input("\n¿Deseas guardar las contraseñas en un archivo .txt? (s/n): ").lower()
        if guardar == 's':
            guardar_contraseñas(contraseñas)

    except ValueError as e:
        print(f"⚠️ Error: {e}")

main()
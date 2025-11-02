import os
import pdfplumber

def validar_pdf(path):
    return os.path.isfile(path) and path.lower().endswith('.pdf')

def extraer_texto(pdf_path, paginas=None):
    texto = ""
    with pdfplumber.open(pdf_path) as pdf:
        total_paginas = len(pdf.pages)
        if paginas:
            paginas = [p for p in paginas if 1 <= p <= total_paginas]
        else:
            paginas = list(range(1, total_paginas + 1))
        for num in paginas:
            texto += pdf.pages[num - 1].extract_text() or ""
    return texto

def guardar_txt(texto, salida_path):
    with open(salida_path, 'w', encoding='utf-8') as f:
        f.write(texto)

def convertir_un_pdf():
    ruta = input("📄 Ingresa la ruta del archivo PDF: ").strip()
    if not validar_pdf(ruta):
        print("❌ Archivo inválido. Asegúrate de que sea un PDF.")
        return

    paginas = input("📑 Ingresa las páginas a extraer (ej: 1,3,5) o ENTER para todas: ").strip()
    if paginas:
        try:
            paginas = [int(p.strip()) for p in paginas.split(',')]
        except ValueError:
            print("❌ Formato de páginas inválido.")
            return
    else:
        paginas = None

    texto = extraer_texto(ruta, paginas)
    salida = os.path.splitext(ruta)[0] + "_extraido.txt"
    guardar_txt(texto, salida)
    print(f"✅ Texto guardado en: {salida}")

def convertir_en_lote():
    carpeta = input("📁 Ingresa la ruta de la carpeta con PDFs: ").strip()
    if not os.path.isdir(carpeta):
        print("❌ Carpeta inválida.")
        return

    archivos = [f for f in os.listdir(carpeta) if f.lower().endswith('.pdf')]
    if not archivos:
        print("⚠️ No se encontraron archivos PDF.")
        return

    for archivo in archivos:
        ruta = os.path.join(carpeta, archivo)
        texto = extraer_texto(ruta)
        salida = os.path.splitext(ruta)[0] + "_extraido.txt"
        guardar_txt(texto, salida)
        print(f"✅ {archivo} convertido a texto.")

def menu():
    while True:
        print("\n📚 Conversor de PDF a Texto")
        print("1. Convertir un PDF")
        print("2. Convertir múltiples PDFs (lote)")
        print("3. Salir")
        opcion = input("👉 Selecciona una opción: ").strip()

        if opcion == '1':
            convertir_un_pdf()
        elif opcion == '2':
            convertir_en_lote()
        elif opcion == '3':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()
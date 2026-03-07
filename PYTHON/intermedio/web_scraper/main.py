from scraper import obtener_html, obtener_soup
from analizador import extraer_titulares
from guardado import guardar_json, guardar_csv

def main():
    url = input("🌐 Ingresa la URL de la página de noticias: ")
    selector = input("🔍 Ingresa el selector HTML para los titulares (ej. h2, .title): ")

    html = obtener_html(url)
    soup = obtener_soup(html)
    titulares = extraer_titulares(soup, selector)

    if titulares:
        print("\n📰 Titulares encontrados:")
        for i, t in enumerate(titulares, 1):
            print(f"{i}. {t}")

        opcion = input("\n💾 ¿Guardar en (1) JSON o (2) CSV? ")
        if opcion == "1":
            guardar_json(titulares)
        elif opcion == "2":
            guardar_csv(titulares)
        else:
            print("❌ Opción inválida. No se guardó nada.")
    else:
        print("⚠️ No se encontraron titulares con ese selector.")

if __name__ == "__main__":
    main()
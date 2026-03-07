import sqlite3
import re

DB_NAME = "C:\\Users\\FENIX\\Documents\\CODE_VISUAL\\PROYECTOS_PY\\inter\\agenda_contactos_SQLite\\agenda_contactos.db"

def conectar():
    # conn = sqlite3.connect(DB_NAME)
    try:
        conn = sqlite3.connect(DB_NAME)
    except sqlite3.Error as e:
        print(f"❌ Error al conectar con la base de datos: {e}")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            correo TEXT,
            direccion TEXT
        )
    """)
    conn.commit()
    return conn

def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validar_telefono(telefono):
    return re.match(r"^\+?\d{7,15}$", telefono)

def agregar_contacto():
    nombre = input("📝 Nombre: ").strip()
    telefono = input("📞 Teléfono: ").strip()
    correo = input("📧 Correo: ").strip()
    direccion = input("🏠 Dirección: ").strip()

    if not validar_telefono(telefono):
        print("❌ Teléfono inválido.")
        return
    if correo and not validar_email(correo):
        print("❌ Correo inválido.")
        return

    conn = conectar()
    conn.execute("INSERT INTO contactos (nombre, telefono, correo, direccion) VALUES (?, ?, ?, ?)",
                 (nombre, telefono, correo, direccion))
    conn.commit()
    conn.close()
    print("✅ Contacto agregado.")

def buscar_contacto():
    criterio = input("🔍 Buscar por nombre o teléfono: ").strip()
    conn = conectar()

    try:
        cursor = conn.execute(
            "SELECT * FROM contactos WHERE nombre LIKE ? OR telefono LIKE ?",
            (f"%{criterio}%", f"%{criterio}%")
        )
        resultados = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"❌ Error al ejecutar la consulta: {e}")
        resultados = []
    finally:
        conn.close()

    if resultados:
        print(f"\n🔎 Se encontraron {len(resultados)} contacto(s):")
        for c in resultados:
            print(f"""
                🆔 ID: {c[0]}
                📛 Nombre: {c[1]}
                📞 Teléfono: {c[2]}
                📧 Correo: {c[3]}
                🏠 Dirección: {c[4]}
            """)
    else:
        print("⚠️ No se encontraron contactos que coincidan con el criterio.")

def editar_contacto():
    id_contacto = input("✏️ ID del contacto a editar: ").strip()
    conn = conectar()
    cursor = conn.execute("SELECT * FROM contactos WHERE id = ?", (id_contacto,))
    contacto = cursor.fetchone()

    if not contacto:
        print("❌ Contacto no encontrado.")
        conn.close()
        return

    print("🔄 Deja vacío para mantener el valor actual.")
    nombre = input(f"📛 Nombre ({contacto[1]}): ").strip() or contacto[1]
    telefono = input(f"📞 Teléfono ({contacto[2]}): ").strip() or contacto[2]
    correo = input(f"📧 Correo ({contacto[3]}): ").strip() or contacto[3]
    direccion = input(f"🏠 Dirección ({contacto[4]}): ").strip() or contacto[4]

    if not validar_telefono(telefono):
        print("❌ Teléfono inválido.")
        conn.close()
        return
    if correo and not validar_email(correo):
        print("❌ Correo inválido.")
        conn.close()
        return

    conn.execute("""
        UPDATE contactos SET nombre = ?, telefono = ?, correo = ?, direccion = ? WHERE id = ?
    """, (nombre, telefono, correo, direccion, id_contacto))
    conn.commit()
    conn.close()
    print("✅ Contacto actualizado.")

def eliminar_contacto():
    id_contacto = input("🗑️ ID del contacto a eliminar: ").strip()
    conn = conectar()
    cursor = conn.execute("SELECT * FROM contactos WHERE id = ?", (id_contacto,))
    if cursor.fetchone():
        conn.execute("DELETE FROM contactos WHERE id = ?", (id_contacto,))
        conn.commit()
        print("✅ Contacto eliminado.")
    else:
        print("❌ Contacto no encontrado.")
    conn.close()

def menu():
    while True:
        print("\n📒 Agenda de Contactos")
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("👉 Selecciona una opción: ").strip()

        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            buscar_contacto()
        elif opcion == '3':
            editar_contacto()
        elif opcion == '4':
            eliminar_contacto()
        elif opcion == '5':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()
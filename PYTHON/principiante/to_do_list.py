import json
import os

ARCHIVO_TAREAS = "tareas.json"

# Cargar tareas desde archivo
def cargar_tareas():
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "r") as archivo:
            return json.load(archivo)
    return []

# Guardar tareas en archivo
def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w") as archivo:
        json.dump(tareas, archivo, indent=4)

# Añadir nueva tarea
def añadir_tarea(tareas):
    descripcion = input("🆕 Escribe la descripción de la nueva tarea: ")
    tareas.append({"descripcion": descripcion, "completada": False})
    print("✅ Tarea añadida.")

# Listar todas las tareas
def listar_tareas(tareas):
    if not tareas:
        print("📭 No hay tareas registradas.")
        return
    print("\n📋 Lista de tareas:")
    for i, tarea in enumerate(tareas, 1):
        estado = "✔️" if tarea["completada"] else "❌"
        print(f"{i}. {estado} {tarea['descripcion']}")

# Marcar tarea como completada
def completar_tarea(tareas):
    listar_tareas(tareas)
    try:
        indice = int(input("🔘 Número de la tarea a marcar como completada: ")) - 1
        tareas[indice]["completada"] = True
        print("✅ Tarea marcada como completada.")
    except (IndexError, ValueError):
        print("⚠️ Número inválido.")

# Eliminar tarea
def eliminar_tarea(tareas):
    listar_tareas(tareas)
    try:
        indice = int(input("🗑️ Número de la tarea a eliminar: ")) - 1
        tarea_eliminada = tareas.pop(indice)
        print(f"🗑️ Tarea eliminada: {tarea_eliminada['descripcion']}")
    except (IndexError, ValueError):
        print("⚠️ Número inválido.")

# Menú principal
def menu():
    tareas = cargar_tareas()
    while True:
        print("\n📌 Menú de tareas:")
        print("1. Añadir tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            añadir_tarea(tareas)
        elif opcion == "2":
            listar_tareas(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            guardar_tareas(tareas)
            print("💾 Tareas guardadas. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

# Ejecutar solo si se corre directamente
menu()
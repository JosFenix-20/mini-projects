import json
import pandas as pd

def guardar_json(datos, nombre_archivo="titulares.json"):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    print(f"✅ Datos guardados en {nombre_archivo}")

def guardar_csv(datos, nombre_archivo="titulares.csv"):
    df = pd.DataFrame({"Titular": datos})
    df.to_csv(nombre_archivo, index=False, encoding="utf-8")
    print(f"✅ Datos guardados en {nombre_archivo}")
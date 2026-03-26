import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("Inventario vacío. No se puede guardar.")
        return False

    if not ruta.endswith(".csv"):
        ruta += ".csv"

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])
            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print("Inventario guardado en:", ruta)
        return True

    except Exception as e:
        print("Error al guardar:", e)
        return False
import csv
import os
import time

def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("  ✘  Inventario vacío. No se puede guardar.")
        return False

    if not ruta.lower().endswith(".csv"):
        ruta = ruta + ".csv"

    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])
            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])
        print(f"  ✔  Guardado en: {ruta}")
        return True
    except Exception as e:
        print(f"  ✘  Error al guardar: {e}")
        return False

def cargar_csv(ruta):
    inventario = []
    errores = 0

    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo)
            encabezado = next(reader)

            if encabezado != ["nombre", "precio", "cantidad"]:
                print("  ✘  Encabezado inválido.")
                return None

            filas = list(reader)

        print(f"\n  Cargando {len(filas)} fila(s) desde '{ruta}'...\n")
        time.sleep(0.3)

        for i, fila in enumerate(filas, 1):
            if len(fila) != 3:
                errores += 1
                print(f"  [{i:>3}]  ✘  Fila inválida — omitida")
                time.sleep(0.05)
                continue
            try:
                nombre   = fila[0]
                precio   = float(fila[1])
                cantidad = int(fila[2])
                if precio < 0 or cantidad < 0:
                    raise ValueError
                inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                print(f"  [{i:>3}]  ✔  {nombre:<20} ${precio:.2f}  ×{cantidad}")
                time.sleep(0.05)
            except ValueError:
                errores += 1
                print(f"  [{i:>3}]  ✘  Datos inválidos en fila {i} — omitida")
                time.sleep(0.05)

        print(f"\n  ✔  Carga completada — {len(inventario)} productos, {errores} fila(s) omitida(s).")
        return inventario

    except FileNotFoundError:
        print("  ✘  Archivo no encontrado.")
    except UnicodeDecodeError:
        print("  ✘  Error de codificación.")
    except Exception as e:
        print(f"  ✘  Error: {e}")

    return None
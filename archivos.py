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


def cargar_csv(ruta):
    inventario = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            encabezado = next(reader)

            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido")
                return None

            for fila in reader:
                if len(fila) != 3:
                    errores += 1
                    continue

                try:
                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

                except:
                    errores += 1

        print("Filas inválidas omitidas:", errores)
        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado")
    except UnicodeDecodeError:
        print("Error de codificación")
    except Exception as e:
        print("Error:", e)

    return None
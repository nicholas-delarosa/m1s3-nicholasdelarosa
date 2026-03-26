def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un producto al inventario."""
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

def mostrar_inventario(inventario):
    """Muestra todos los productos."""
    if not inventario:
        print("Inventario vacío")
        return
    for p in inventario:
        print(p)

def buscar_producto(inventario, nombre):
    """Busca un producto por nombre."""
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza precio o cantidad."""
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False

def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario."""
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False

def calcular_estadisticas(inventario):
    """Calcula estadísticas del inventario."""
    if not inventario:
        print("Inventario vacío")
        return

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)

    print("Unidades totales:", unidades_totales)
    print("Valor total:", valor_total)
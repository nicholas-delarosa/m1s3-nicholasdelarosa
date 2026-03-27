SEP = "─" * 45

def agregar_producto(inventario, nombre, precio, cantidad):
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

def mostrar_inventario(inventario):
    if not inventario:
        print("  (inventario vacío)")
        return

    COL_NUM    = 4
    COL_NOMBRE = 22
    COL_PRECIO = 12
    COL_CANT   = 12

    encabezado = (
        f"  {'#':<{COL_NUM}}"
        f"{'Nombre':<{COL_NOMBRE}}"
        f"{'Precio':>{COL_PRECIO}}"
        f"{'Cantidad':>{COL_CANT}}"
    )
    sep = "  " + "─" * (COL_NUM + COL_NOMBRE + COL_PRECIO + COL_CANT)

    print(sep)
    print(encabezado)
    print(sep)
    for i, p in enumerate(inventario, 1):
        print(
            f"  {i:<{COL_NUM}}"
            f"{p['nombre']:<{COL_NOMBRE}}"
            f"${p['precio']:>{COL_PRECIO - 1}.2f}"
            f"{p['cantidad']:>{COL_CANT - 1}} uds."
        )
    print(sep)

def buscar_producto(inventario, nombre):
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False

def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False

def calcular_estadisticas(inventario):
    if not inventario:
        print("  (inventario vacío)")
        return

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)
    mas_caro = max(inventario, key=lambda p: p["precio"])
    mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    print(f"  Productos registrados  : {len(inventario)}")
    print(f"  Unidades totales       : {unidades_totales}")
    print(f"  Valor total inventario : ${valor_total:,.2f}")
    print(f"  Producto más caro      : {mas_caro['nombre']} (${mas_caro['precio']:.2f})")
    print(f"  Mayor stock            : {mayor_stock['nombre']} ({mayor_stock['cantidad']} uds.)")
import os
from servicios import (
    agregar_producto,
    mostrar_inventario,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas
)
from archivos import guardar_csv, cargar_csv

inventario = []

SEP = "─" * 45

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\n  Presiona Enter para continuar...")
    limpiar()

def titulo(texto):
    print(f"\n{SEP}")
    print(f"  {texto}")
    print(SEP)

def ok(texto):
    print(f"  ✔  {texto}")

def error(texto):
    print(f"  ✘  {texto}")

def mostrar_menu():
    print(f"\n{'═' * 45}")
    print("        SISTEMA DE INVENTARIO")
    print(f"{'═' * 45}")
    opciones = [
        ("1", "Agregar producto"),
        ("2", "Mostrar inventario"),
        ("3", "Buscar producto"),
        ("4", "Actualizar producto"),
        ("5", "Eliminar producto"),
        ("6", "Estadísticas"),
        ("7", "Guardar CSV"),
        ("8", "Cargar CSV"),
        ("9", "Salir"),
    ]
    for num, desc in opciones:
        print(f"  [{num}]  {desc}")
    print(f"{'═' * 45}")

def pedir_nombre(mensaje):
    while True:
        valor = input(f"  {mensaje}: ").strip()
        if valor:
            return valor
        error("El nombre no puede estar vacío.")

def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(f"  {mensaje}: "))
            if valor < 0:
                raise ValueError
            return valor
        except ValueError:
            error("Debe ser un número positivo.")

def pedir_int(mensaje):
    while True:
        try:
            valor = int(input(f"  {mensaje}: "))
            if valor < 0:
                raise ValueError
            return valor
        except ValueError:
            error("Debe ser un entero positivo.")

# Bucle principal del programa
while True:
    mostrar_menu()
    opcion = input("\n  Opción → ").strip()

    if opcion == "1":
        while True:
            titulo("AGREGAR PRODUCTO")
            nombre = pedir_nombre("Nombre")
            precio = pedir_float("Precio ($)")
            cantidad = pedir_int("Cantidad")
            agregar_producto(inventario, nombre, precio, cantidad)
            ok(f"'{nombre}' agregado al inventario.")
            otro = input("  ¿Agregar otro producto? [S/N]: ").strip().lower()
            if otro != "s":
                pausar()
                break

    elif opcion == "2":
        titulo("INVENTARIO")
        mostrar_inventario(inventario)
        pausar()

    elif opcion == "3":
        while True:
            titulo("BUSCAR PRODUCTO")
            nombre = pedir_nombre("Nombre a buscar")
            producto = buscar_producto(inventario, nombre)
            if producto:
                print(f"\n  Producto : {producto['nombre']}")
                print(f"  Precio   : ${producto['precio']:.2f}")
                print(f"  Cantidad : {producto['cantidad']} uds.")
                pausar()
                break
            else:
                error("Producto no encontrado.")
                reintentar = input("  ¿Buscar otro? [S/N]: ").strip().lower()
                if reintentar != "s":
                    limpiar()
                    break

    elif opcion == "4":
        while True:
            titulo("ACTUALIZAR PRODUCTO")
            nombre = pedir_nombre("Producto a actualizar")
            precio_str = input("  Nuevo precio    (Enter para omitir): ").strip()
            cantidad_str = input("  Nueva cantidad  (Enter para omitir): ").strip()
            precio = float(precio_str) if precio_str else None
            cantidad = int(cantidad_str) if cantidad_str else None
            if actualizar_producto(inventario, nombre, precio, cantidad):
                ok(f"'{nombre}' actualizado.")
                pausar()
                break
            else:
                error("Producto no encontrado.")
                reintentar = input("  ¿Intentar con otro nombre? [S/N]: ").strip().lower()
                if reintentar != "s":
                    limpiar()
                    break

    elif opcion == "5":
        while True:
            titulo("ELIMINAR PRODUCTO")
            nombre = pedir_nombre("Producto a eliminar")
            if eliminar_producto(inventario, nombre):
                ok(f"'{nombre}' eliminado del inventario.")
                pausar()
                break
            else:
                error("Producto no encontrado.")
                reintentar = input("  ¿Intentar con otro nombre? [S/N]: ").strip().lower()
                if reintentar != "s":
                    limpiar()
                    break

    elif opcion == "6":
        titulo("ESTADÍSTICAS")
        calcular_estadisticas(inventario)
        pausar()

    elif opcion == "7":
        while True:
            titulo("GUARDAR CSV")
            ruta = input("  Ruta del archivo: ").strip()
            if guardar_csv(inventario, ruta):
                pausar()
                break
            else:
                reintentar = input("  ¿Intentar con otra ruta? [S/N]: ").strip().lower()
                if reintentar != "s":
                    limpiar()
                    break

    elif opcion == "8":
        while True:
            titulo("CARGAR CSV")
            ruta = input("  Ruta del archivo: ").strip()
            nuevos = cargar_csv(ruta)
            if nuevos is not None:
                decision = input("  ¿Sobrescribir inventario? [S/N]: ").strip().lower()
                if decision == "s":
                    inventario = nuevos
                else:
                    for p in nuevos:
                        existente = buscar_producto(inventario, p["nombre"])
                        if existente:
                            existente["cantidad"] += p["cantidad"]
                            existente["precio"] = p["precio"]
                        else:
                            inventario.append(p)
                ok("Inventario actualizado.")
                pausar()
                break
            else:
                reintentar = input("  ¿Intentar con otra ruta? [S/N]: ").strip().lower()
                if reintentar != "s":
                    limpiar()
                    break

    elif opcion == "9":
        print(f"\n{SEP}")
        print("  Hasta luego.")
        print(f"{SEP}\n")
        break

    else:
        error("Opción inválida. Elige entre 1 y 9.")
        pausar()
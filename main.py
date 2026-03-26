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

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPresiona Enter para continuar...")
    limpiar()

while True:
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        agregar_producto(inventario, nombre, precio, cantidad)

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        nombre = input("Nombre a buscar: ")
        producto = buscar_producto(inventario, nombre)
        print(producto)

    elif opcion == "4":
        nombre = input("Producto a actualizar: ")
        precio = float(input("Nuevo precio: "))
        cantidad = int(input("Nueva cantidad: "))
        actualizar_producto(inventario, nombre, precio, cantidad)

    elif opcion == "5":
        nombre = input("Producto a eliminar: ")
        eliminar_producto(inventario, nombre)

    elif opcion == "6":
        calcular_estadisticas(inventario)

    elif opcion == "7":
        ruta = input("Ruta del archivo: ")
        guardar_csv(inventario, ruta)

    elif opcion == "8":
        ruta = input("Ruta del archivo: ")
        nuevos = cargar_csv(ruta)

        if nuevos:
            decision = input("¿Sobrescribir inventario? (S/N): ").lower()

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

    elif opcion == "9":
        break

    pausar()

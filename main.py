import os
from servicios import (
    agregar_producto,
    mostrar_inventario,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas
)

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
    print("7. Salir")

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
        break

    pausar()
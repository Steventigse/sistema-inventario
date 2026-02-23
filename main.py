# Importamos las clases necesarias
from servicios.inventario import Inventario
from modelos.producto import Producto

inventario = Inventario()

while True:
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    # =========================
    # AGREGAR PRODUCTO
    # =========================
    if opcion == "1":
        try:
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        except ValueError:
            print("Error: Debe ingresar números válidos para cantidad y precio.")

    # =========================
    # ELIMINAR PRODUCTO
    # =========================
    elif opcion == "2":
        id = input("Ingrese ID a eliminar: ")
        inventario.eliminar_producto(id)

    # =========================
    # ACTUALIZAR PRODUCTO
    # =========================
    elif opcion == "3":
        try:
            id = input("ID del producto: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))

            inventario.actualizar_producto(id, cantidad, precio)

        except ValueError:
            print("Error: Debe ingresar números válidos para cantidad y precio.")

    # =========================
    # BUSCAR PRODUCTO
    # =========================
    elif opcion == "4":
        nombre = input("Nombre a buscar: ")
        resultados = inventario.buscar_producto(nombre)

        if resultados:
            for p in resultados:
                print(
                    f"ID: {p.get_id()} | "
                    f"Nombre: {p.get_nombre()} | "
                    f"Cantidad: {p.get_cantidad()} | "
                    f"Precio: {p.get_precio()}"
                )
        else:
            print("No se encontraron productos.")

    # =========================
    # MOSTRAR INVENTARIO
    # =========================
    elif opcion == "5":
        inventario.mostrar_inventario()

    # =========================
    # SALIR
    # =========================
    elif opcion == "6":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")
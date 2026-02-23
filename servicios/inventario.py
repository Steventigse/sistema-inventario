from modelos.producto import Producto
import os

class Inventario:
    
    def __init__(self):
        self.productos = []
        self.archivo = "inventario.txt"
        self.cargar_desde_archivo()

    # ==========================================
    # CARGAR INVENTARIO DESDE ARCHIVO
    # ==========================================
    def cargar_desde_archivo(self):
        try:
            # Si el archivo no existe, se crea automáticamente
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()

            with open(self.archivo, "r") as file:
                for linea in file:
                    try:
                        datos = linea.strip().split(",")
                        
                        # Validamos que la línea tenga los 4 campos esperados
                        if len(datos) == 4:
                            id, nombre, cantidad, precio = datos
                            producto = Producto(
                                id,
                                nombre,
                                int(cantidad),   # Puede lanzar ValueError
                                float(precio)    # Puede lanzar ValueError
                            )
                            self.productos.append(producto)
                    
                    # Manejo de datos corruptos en el archivo
                    except ValueError:
                        print("Advertencia: Línea con datos inválidos ignorada.")

            print("Inventario cargado correctamente desde archivo.")

        except FileNotFoundError:
            print("El archivo no existe. Se creará uno nuevo.")
        
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")
        
        except Exception as e:
            print("Error inesperado al cargar el archivo:", e)

    # ==========================================
    # GUARDAR INVENTARIO EN ARCHIVO
    # ==========================================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as file:
                for p in self.productos:
                    file.write(
                        f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    )

            print("Cambios guardados en archivo correctamente.")

        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        
        except Exception as e:
            print("Error inesperado al guardar:", e)

    # ==========================================
    # MÉTODOS DEL INVENTARIO
    # ==========================================
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("El ID ya existe.")
                return

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id):
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado.")
                return

        print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)

                self.guardar_en_archivo()
                print("Producto actualizado.")
                return

        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
            return

        for p in self.productos:
            print(
                f"ID: {p.get_id()} | "
                f"Nombre: {p.get_nombre()} | "
                f"Cantidad: {p.get_cantidad()} | "
                f"Precio: {p.get_precio()}"
            )
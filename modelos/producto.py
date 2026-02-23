# Clase que representa un producto dentro del inventario
class Producto:
    
    # Constructor: se ejecuta al crear un nuevo producto
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Métodos getters: permiten obtener los valores
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Métodos setters: permiten modificar los valores
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio
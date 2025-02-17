# Clase que representa cada producto en el inventario
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        # Constructor que inicializa los atributos del producto
        self.id = id              # ID único para cada producto
        self.nombre = nombre      # Nombre del producto
        self.cantidad = cantidad  # Cantidad de productos en stock
        self.precio = precio      # Precio de cada producto producto

    # Métodos getters y setters para cada atributo

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


# Clase Inventario, sirve para gestionar la lista de productos
class Inventario:
    def __init__(self):
        # se inicia el inventario como una lista vacía de productos
        self.productos = []

    def agregar_producto(self, producto):
        # Método para agregar un nuevo producto al inventario
        # Se verifica que el ID sea único antes de agregar
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id):
        # Metodo para eliminar un producto por su ID
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                print("Producto eliminado exitosamente.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        # Metodo para actualizar la cantidad o el precio de un producto dado su ID
        for p in self.productos:
            if p.get_id() == id:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado exitosamente.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Metodo para buscar productos por nombre (o parte del nombre)
        encontrados = []
        for p in self.productos:
            # Se hace la búsqueda sin distinguir mayúsculas/minúsculas
            if nombre.lower() in p.get_nombre().lower():
                encontrados.append(p)
        return encontrados

    def mostrar_productos(self):
        # Metodo para mostrar todos los productos en el inventario
        if not self.productos:
            print("No hay productos en el inventario.")
            return
        for p in self.productos:
            print("ID: {}, Nombre: {}, Cantidad: {}, Precio: ${}".format(
                p.get_id(), p.get_nombre(), p.get_cantidad(), p.get_precio()))


# Función que implementa la interfaz de usuario en la consola
def menu():
    inventario = Inventario()  # Se crea una instancia del inventario
    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Agregar nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Opción para agregar un nuevo producto
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            try:
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
            except ValueError:
                print("Error: La cantidad debe ser un entero y el precio un número.")
                continue
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            # Opción para eliminar un producto por su ID
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            # Opción para actualizar la cantidad o el precio de un producto
            id = input("Ingrese el ID del producto a actualizar: ")
            print("Si no desea actualizar un campo, deje el valor en blanco.")
            nueva_cantidad = input("Ingrese la nueva cantidad: ")
            nuevo_precio = input("Ingrese el nuevo precio: ")

            cantidad_val = None
            precio_val = None
            if nueva_cantidad != "":
                try:
                    cantidad_val = int(nueva_cantidad)
                except ValueError:
                    print("Error: La cantidad debe ser un entero.")
                    continue
            if nuevo_precio != "":
                try:
                    precio_val = float(nuevo_precio)
                except ValueError:
                    print("Error: El precio debe ser un número.")
                    continue
            inventario.actualizar_producto(id, cantidad_val, precio_val)

        elif opcion == "4":
            # Opción para buscar productos por nombre
            nombre = input("Ingrese el nombre (o parte del nombre) del producto a buscar: ")
            encontrados = inventario.buscar_producto(nombre)
            if encontrados:
                print("Productos encontrados:")
                for p in encontrados:
                    print("ID: {}, Nombre: {}, Cantidad: {}, Precio: ${}".format(
                        p.get_id(), p.get_nombre(), p.get_cantidad(), p.get_precio()))
            else:
                print("No se encontró ningún producto con ese nombre.")

        elif opcion == "5":
            # Opción para mostrar todos los productos
            inventario.mostrar_productos()

        elif opcion == "6":
            # Salir del sistema
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


# se inicializa el programa
if __name__ == "__main__":
    menu()

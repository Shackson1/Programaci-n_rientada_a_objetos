import os

# Clase que representa cada producto en el inventario
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        :param id: Identificador único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible en inventario.
        :param precio: Precio unitario del producto.
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """
        Representación en cadena del objeto Producto para almacenamiento en archivos.
        Se utiliza el formato CSV: "id,nombre,cantidad,precio".
        """
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"

    @staticmethod
    def from_string(data):
        """
        Método estático que convierte una línea de texto en un objeto Producto.
        :param data: Cadena en formato "id,nombre,cantidad,precio".
        :return: Instancia de Producto.
        """
        id, nombre, cantidad, precio = data.strip().split(",")
        return Producto(id, nombre, int(cantidad), float(precio))


class Inventario:
    ARCHIVO = "inventario.txt"  # Nombre del archivo donde se almacena el inventario

    def __init__(self):
        """
        Constructor de la clase Inventario.
        Se inicializa la lista de productos y se carga el inventario desde el archivo, si existe.
        Esto cumple con el requisito de recuperar datos al iniciar el programa.
        """
        self.productos = []
        self.cargar_desde_archivo()  # Recupera el inventario desde el archivo

    def guardar_en_archivo(self):
        """
        Guarda el inventario en un archivo de texto para persistencia de datos.
        Cada modificación (agregar, actualizar, eliminar) se refleja en el archivo.
        Se implementa manejo de excepciones para capturar errores, por ejemplo, falta de permisos.
        """
        try:
            with open(self.ARCHIVO, "w") as file:
                for producto in self.productos:
                    file.write(str(producto) + "\n")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

    def cargar_desde_archivo(self):
        """
        Carga los productos desde el archivo de inventario si existe.
        Se maneja la excepción en caso de que el archivo no exista o se produzca otro error.
        Si el archivo no existe, se omite la carga, y posteriormente al guardar se creará.
        """
        if not os.path.exists(self.ARCHIVO):
            # El archivo no existe, por lo que se omite la carga (se creará al guardar)
            return
        try:
            with open(self.ARCHIVO, "r") as file:
                # Se reconstruye el inventario a partir de cada línea del archivo
                self.productos = [Producto.from_string(line) for line in file]
        except FileNotFoundError:
            print("Error: El archivo de inventario no existe. Creando uno nuevo.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario, asegurando que el ID sea único.
        Luego, persiste la información actualizada en el archivo de texto.
        """
        for p in self.productos:
            if p.id == producto.id:
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()  # Guarda la actualización en el archivo
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario si su ID coincide.
        Tras la eliminación, se actualiza el archivo de inventario.
        """
        for p in self.productos:
            if p.id == id:
                self.productos.remove(p)
                self.guardar_en_archivo()  # Actualiza el archivo tras la eliminación
                print("Producto eliminado exitosamente.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad o el precio de un producto en el inventario.
        Luego, guarda los cambios en el archivo para mantener la persistencia.
        """
        for p in self.productos:
            if p.id == id:
                if nueva_cantidad is not None:
                    p.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    p.precio = nuevo_precio
                self.guardar_en_archivo()  # Guarda la actualización en el archivo
                print("Producto actualizado exitosamente.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """
        Busca productos en el inventario cuyo nombre coincida parcial o totalmente (sin distinguir mayúsculas).
        :return: Lista de productos que cumplen con el criterio de búsqueda.
        """
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

    def mostrar_productos(self):
        """
        Muestra todos los productos almacenados en el inventario.
        Si no hay productos, se notifica al usuario.
        """
        if not self.productos:
            print("No hay productos en el inventario.")
            return
        for p in self.productos:
            print(f"ID: {p.id}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: ${p.precio}")


# Interfaz de usuario en la consola
def menu():
    """
    Función principal que muestra el menú de opciones y permite interactuar con el usuario.
    Se notifica al usuario sobre el éxito o fallo de cada operación, cumpliendo con los requerimientos.
    """
    inventario = Inventario()  # Se crea una instancia del inventario, que carga los datos desde el archivo
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
            nueva_cantidad = input("Ingrese la nueva cantidad (deje en blanco para no modificar): ")
            nuevo_precio = input("Ingrese el nuevo precio (deje en blanco para no modificar): ")

            # Convertir los valores de entrada a los tipos correspondientes si se han proporcionado
            cantidad_val = int(nueva_cantidad) if nueva_cantidad else None
            precio_val = float(nuevo_precio) if nuevo_precio else None

            inventario.actualizar_producto(id, cantidad_val, precio_val)

        elif opcion == "4":
            # Opción para buscar productos por nombre (o parte del nombre)
            nombre = input("Ingrese el nombre del producto a buscar: ")
            encontrados = inventario.buscar_producto(nombre)
            if encontrados:
                for p in encontrados:
                    print(f"ID: {p.id}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: ${p.precio}")
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            # Opción para mostrar todos los productos en el inventario
            inventario.mostrar_productos()

        elif opcion == "6":
            # Opción para salir del programa
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")



if __name__ == "__main__":
    menu()

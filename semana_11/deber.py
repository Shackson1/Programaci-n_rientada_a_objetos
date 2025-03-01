import json

# Clase Producto: Representa cada ítem del inventario.
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """
        Inicializa un nuevo producto con su ID único, nombre, cantidad y precio.
        """
        self.id = id                # Identificador único del producto.
        self.nombre = nombre        # Nombre descriptivo del producto.
        self.cantidad = cantidad    # Cantidad disponible en el inventario.
        self.precio = precio        # Precio unitario del producto.

    # Métodos getter y setter para acceder y modificar los atributos del producto.
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def to_dict(self):
        """
        Convierte el producto a un diccionario.
        Esto facilita su serialización para guardar la información en un archivo.
        """
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Producto a partir de un diccionario.
        Este método se utiliza al cargar los datos del archivo para reconstruir el objeto.
        """
        return cls(data['id'], data['nombre'], data['cantidad'], data['precio'])

    def __str__(self):
        """
        Retorna una representación legible del producto.
        """
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# Clase Inventario: Gestiona la colección de productos usando un diccionario.
class Inventario:
    def __init__(self):
        """
        Inicializa el inventario utilizando un diccionario para almacenar los productos.
        - La clave del diccionario es el ID del producto (único).
        - El valor es el objeto Producto.
        Este uso de un diccionario (colección) permite un acceso rápido y eficiente a cada producto.
        """
        self.productos = {}  # Diccionario para almacenar los productos.

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario.
        Verifica si el ID del producto ya existe en la colección; si no, lo agrega.
        """
        if producto.get_id() in self.productos:
            print("El producto con ese ID ya existe en el inventario.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID.
        Se elimina directamente del diccionario.
        """
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado.")
        else:
            print("No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad y/o el precio de un producto existente.
        Se accede al producto a través del diccionario usando su ID y se modifican sus atributos.
        """
        if id in self.productos:
            producto = self.productos[id]
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            print("Producto actualizado.")
        else:
            print("No se encontró un producto con ese ID.")

    def buscar_producto_por_nombre(self, nombre):
        """
        Busca y muestra los productos cuyo nombre contenga la cadena buscada.
        Utiliza una lista por comprensión para filtrar los productos del diccionario,
        haciendo la búsqueda insensible a mayúsculas y minúsculas.
        """
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        if resultados:
            print("Productos encontrados:")
            for prod in resultados:
                print(prod)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        """
        Muestra todos los productos almacenados en el inventario.
        Recorre el diccionario y muestra la información de cada producto.
        """
        if self.productos:
            print("Inventario de productos:")
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, ruta_archivo):
        """
        Serializa y guarda el inventario en un archivo JSON.
        - Se recorre el diccionario de productos.
        - Cada producto se convierte a un diccionario mediante 'to_dict()'.
        - Los datos se guardan en el archivo en formato JSON para persistir la información.
        """
        try:
            with open(ruta_archivo, "w") as archivo:
                datos = {id: producto.to_dict() for id, producto in self.productos.items()}
                json.dump(datos, archivo, indent=4)  # Guarda el diccionario como un archivo JSON.
            print("Inventario guardado exitosamente.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def cargar_inventario(self, ruta_archivo):
        """
        Carga el inventario desde un archivo JSON y lo deserializa.
        - Abre el archivo y lee el contenido JSON.
        - Reconstruye el diccionario de productos utilizando 'from_dict()' para cada producto.
        - Esto restaura la colección de productos en memoria.
        """
        try:
            with open(ruta_archivo, "r") as archivo:
                datos = json.load(archivo)
                self.productos = {id: Producto.from_dict(info) for id, info in datos.items()}
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("El archivo no existe.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")


# Función para mostrar el menú interactivo y procesar las operaciones del inventario.
def menu():
    inventario = Inventario()  # Se crea una instancia de Inventario, que usa un diccionario para gestionar los productos.
    archivo_inventario = "inventario.json"  # Archivo para el almacenamiento persistente del inventario.

    while True:
        print("\n--- Sistema Avanzado de Gestión de Inventario ---")
        print("1. Agregar nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto")
        print("4. Buscar productos por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario en archivo")
        print("7. Cargar inventario desde archivo")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id = input("Ingrese el ID del producto: ")
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                producto = Producto(id, nombre, cantidad, precio)
                # Se agrega el producto al diccionario del inventario.
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: La cantidad debe ser un entero y el precio un número.")
        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            # Se elimina el producto del diccionario usando su ID.
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            try:
                nueva_cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea actualizar): ")
                nuevo_precio = input("Ingrese el nuevo precio (deje en blanco si no desea actualizar): ")
                cantidad_valida = int(nueva_cantidad) if nueva_cantidad.strip() != "" else None
                precio_valido = float(nuevo_precio) if nuevo_precio.strip() != "" else None
                # Se actualiza el producto especificado en el diccionario.
                inventario.actualizar_producto(id, cantidad_valida, precio_valido)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad y precio.")
        elif opcion == "4":
            nombre = input("Ingrese el nombre o parte del nombre a buscar: ")
            # Se realiza una búsqueda en la colección de productos.
            inventario.buscar_producto_por_nombre(nombre)
        elif opcion == "5":
            # Se muestran todos los productos almacenados en el inventario.
            inventario.mostrar_productos()
        elif opcion == "6":
            # Se guarda la colección (diccionario) en un archivo JSON para persistencia.
            inventario.guardar_inventario(archivo_inventario)
        elif opcion == "7":
            # Se carga el inventario desde el archivo JSON, reconstruyendo la colección en memoria.
            inventario.cargar_inventario(archivo_inventario)
        elif opcion == "8":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Punto de entrada del programa.
if __name__ == "__main__":
    menu()

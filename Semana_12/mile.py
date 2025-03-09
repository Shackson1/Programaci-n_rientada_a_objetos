#Sistema de Biblioteca Digital

class Libro:
    def __init__(self, titulo, autor, categoria, id):
        self.detalles = (titulo, autor)  # Tupla para datos inmutables
        self.categoria = categoria
        self.id = id

    def __str__(self):
        return f"{self.detalles[0]} - {self.detalles[1]} (Categoría: {self.categoria}, ID: {self.id})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.prestamos = []  # Lista de libros prestados

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.catalogo = {}  # Diccionario con ID como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor

    def agregar_libro(self, libro):
        self.catalogo[libro.id] = libro
        print(f"Se ha añadido el libro: {libro}")

    def eliminar_libro(self, id):
        if self.catalogo.pop(id, None):
            print(f"Libro con ID {id} eliminado del catálogo.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.id_usuario] = usuario
        print(f"Nuevo usuario registrado: {usuario}")

    def dar_baja_usuario(self, id_usuario):
        if self.usuarios.pop(id_usuario, None):
            print(f"El usuario con ID {id_usuario} ha sido eliminado.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, id_usuario, id):
        usuario = self.usuarios.get(id_usuario)
        libro = self.catalogo.get(id)
        if usuario and libro:
            usuario.prestamos.append(libro)
            del self.catalogo[id]
            print(f"El libro {id} ha sido prestado a {usuario.nombre}.")
        else:
            print("No se puede completar el préstamo.")

    def devolver_libro(self, id_usuario, id):
        usuario = self.usuarios.get(id_usuario)
        if usuario:
            for libro in usuario.prestamos:
                if libro.id == id:
                    usuario.prestamos.remove(libro)
                    self.catalogo[id] = libro
                    print(f"Libro {id} devuelto a la biblioteca.")
                    return
        print("El usuario no tiene este libro en préstamo.")

    def buscar_libro(self, criterio, valor):
        encontrados = [libro for libro in self.catalogo.values() if getattr(libro, criterio, None) == valor]
        return encontrados if encontrados else "No hay coincidencias en la búsqueda."

    def listar_prestamos(self, id_usuario):
        usuario = self.usuarios.get(id_usuario)
        return usuario.prestamos if usuario and usuario.prestamos else "No tiene libros en préstamo."


def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n--- Gestión de Biblioteca Digital ---")
        print("1. Añadir libro")
        print("2. Eliminar libro")
        print("3. Registrar usuario")
        print("4. Eliminar usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Mostrar libros prestados")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            id = input("ID: ")
            biblioteca.agregar_libro(Libro(titulo, autor, categoria, id))
        elif opcion == "2":
            id = input("ID del libro a eliminar: ")
            biblioteca.eliminar_libro(id)
        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.registrar_usuario(Usuario(nombre, id_usuario))
        elif opcion == "4":
            id_usuario = input("ID del usuario a eliminar: ")
            biblioteca.dar_baja_usuario(id_usuario)
        elif opcion == "5":
            id_usuario = input("ID del usuario: ")
            id = input("ID del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, id)
        elif opcion == "6":
            id_usuario = input("ID del usuario: ")
            id = input("ID del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, id)
        elif opcion == "7":
            criterio = input("Buscar por (titulo, categoria, id): ")
            valor = input("Valor: ")
            resultado = biblioteca.buscar_libro(criterio, valor)
            print(resultado)
        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            resultado = biblioteca.listar_prestamos(id_usuario)
            print(resultado)
        elif opcion == "9":
            print("Cerrando el sistema de biblioteca...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

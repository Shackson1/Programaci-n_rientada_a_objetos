#  sistema de biblioteca digital

class Libro:
    def __init__(self, titulo, autor, categoria, codigo):
        self.info = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.codigo = codigo

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (Categoría: {self.categoria}, codigo: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con codigo como clave y objeto Libro como valor
        self.usuarios_registrados = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.codigo] = libro
        print(f"Libro añadido: {libro}")

    def eliminar_libro(self, codigo):
        if self.libros_disponibles.pop(codigo, None):
            print(f"Libro con codigo {codigo} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        self.usuarios_registrados[usuario.id_usuario] = usuario
        print(f"Usuario registrado: {usuario}")

    def dar_baja_usuario(self, id_usuario):
        if self.usuarios_registrados.pop(id_usuario, None):
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, id_usuario, codigo):
        usuario = self.usuarios_registrados.get(id_usuario)
        libro = self.libros_disponibles.get(codigo)
        if usuario and libro:
            usuario.libros_prestados.append(libro)
            del self.libros_disponibles[codigo]
            print(f"Libro prestado a {usuario.nombre}: {codigo}")
        else:
            print("Préstamo no disponible.")

    def devolver_libro(self, id_usuario, codigo):
        usuario = self.usuarios_registrados.get(id_usuario)
        if usuario:
            for libro in usuario.libros_prestados:
                if libro.codigo == codigo:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[codigo] = libro
                    print(f"Libro devuelto: {codigo}")
                    return
        print("El usuario no tiene este libro en préstamo.")

    def buscar_libro(self, criterio, valor):
        encontrados = [libro for libro in self.libros_disponibles.values() if getattr(libro, criterio, None) == valor]
        return encontrados if encontrados else "No se encontraron libros."

    def listar_libros_prestados(self, id_usuario):
        usuario = self.usuarios_registrados.get(id_usuario)
        return usuario.libros_prestados if usuario and usuario.libros_prestados else "No tiene libros prestados."


def menu():
    biblioteca = Biblioteca()
    while True:
        print("\nSistema de Gestión de Biblioteca Digital")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            codigo = input("codigo: ")
            biblioteca.agregar_libro(Libro(titulo, autor, categoria, codigo))
        elif opcion == "2":
            codigo = input("codigo del libro a eliminar: ")
            biblioteca.eliminar_libro(codigo)
        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.registrar_usuario(Usuario(nombre, id_usuario))
        elif opcion == "4":
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)
        elif opcion == "5":
            id_usuario = input("ID del usuario: ")
            codigo = input("codigo del libro: ")
            biblioteca.prestar_libro(id_usuario, codigo)
        elif opcion == "6":
            id_usuario = input("ID del usuario: ")
            codigo = input("codigo del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, codigo)
        elif opcion == "7":
            criterio = input("Buscar por (titulo, categoria, codigo): ")
            valor = input("Valor: ")
            resultado = biblioteca.buscar_libro(criterio, valor)
            print(resultado)
        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            resultado = biblioteca.listar_libros_prestados(id_usuario)
            print(resultado)
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()

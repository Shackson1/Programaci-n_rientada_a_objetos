# Clase para gestionar un estudiante
class Estudiante:
    def __init__(self, nombre, edad):
        """
        Constructor: Se ejecuta al crear un nuevo estudiante
        """
        self.nombre = nombre
        self.edad = edad
        print(f"¡Estudiante {nombre} ha sido registrado!")

    def __del__(self):
        """
        Destructor: Se ejecuta cuando el objeto se elimina
        """
        print(f"¡Estudiante {self.nombre} ha sido eliminado del registro!")

    def estudiar(self):
        print(f"{self.nombre} está estudiando...")


# Clase para gestionar un curso
class Curso:
    def __init__(self, nombre_curso):
        """
        Constructor: Se ejecuta al crear un nuevo curso
        """
        self.nombre = nombre_curso
        self.estudiantes = []
        print(f"¡Curso de {nombre_curso} ha sido creado!")

    def __del__(self):
        """
        Destructor: Se ejecuta cuando el curso se elimina
        """
        print(f"¡Curso de {self.nombre} ha finalizado!")
        print(f"Se eliminaron {len(self.estudiantes)} estudiantes del curso")

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"{estudiante.nombre} agregado al curso de {self.nombre}")


# Programa principal para probar las clases
print("=== Inicio del Programa ===")

# Crear algunos estudiantes
estudiante1 = Estudiante("Juan", 20)
estudiante2 = Estudiante("María", 22)

# Crear un curso y agregar estudiantes
curso_python = Curso("Python")
curso_python.agregar_estudiante(estudiante1)
curso_python.agregar_estudiante(estudiante2)

# Hacer que un estudiante estudie
estudiante1.estudiar()

print("\n=== Fin del Programa ===")
# Los destructores se llamarán automáticamente aquí
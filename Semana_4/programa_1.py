# Programa 1: Sistema de reservas de hotel

class Habitacion:
    """Representa una habitación en el hotel."""
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        """Reserva la habitación si está disponible."""
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} reservada exitosamente.")
        else:
            print(f"Habitación {self.numero} no está disponible.")

    def liberar(self):
        """Libera la habitación."""
        self.disponible = True
        print(f"Habitación {self.numero} liberada.")

class Cliente:
    """Representa un cliente que realiza una reserva."""
    def __init__(self, nombre, id_cliente):
        self.nombre = nombre
        self.id_cliente = id_cliente

    def __str__(self):
        return f"Cliente: {self.nombre}, ID: {self.id_cliente}"

# Ejemplo de uso del sistema de reservas de hotel
habitacion1 = Habitacion(101, "Doble", 80)
cliente1 = Cliente("Carlos Pérez", 1)

habitacion1.reservar()  # Reserva la habitación
habitacion1.liberar()   # Libera la habitación

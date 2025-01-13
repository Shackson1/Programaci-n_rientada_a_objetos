# Programa 2: Sistema de gestión de inventario de una tienda

class Producto:
    """Representa un producto en la tienda."""
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def vender(self, cantidad_vendida):
        """Reduce el inventario si hay suficiente stock."""
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            print(f"Se han vendido {cantidad_vendida} unidades de {self.nombre}.")
        else:
            print(f"No hay suficiente stock de {self.nombre}.")

    def reponer(self, cantidad_repuesta):
        """Aumenta el inventario."""
        self.cantidad += cantidad_repuesta
        print(f"Se han repuesto {cantidad_repuesta} unidades de {self.nombre}.")

# Ejemplo de uso del sistema de gestión de inventario
producto1 = Producto("Laptop", 1200, 10)
producto1.vender(3)  # Vender 3 laptops
producto1.reponer(5)  # Reponer 5 laptops
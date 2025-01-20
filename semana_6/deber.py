
#Este programa emula una tienda de laptops utilizando herencia, encapsulación y polimorfismo en Python. La clase base Laptop define atributos y métodos comunes para las laptops, mientras que la clase derivada LaptopGamer añade características específicas como GPU y tasa de refresco. El atributo privado __precio está encapsulado para un manejo seguro, y el metodo mostrar_informacion se sobrescribe en la clase derivada para incluir detalles adicionales.
# Clase base
class Laptop:
    def __init__(self, marca, modelo, procesador, ram, precio):
        self.marca = marca  # Marca de la laptop
        self.modelo = modelo  # Modelo de la laptop
        self.procesador = procesador  # Procesador
        self.ram = ram  # Memoria RAM
        self.__precio = precio  # Precio (privado)

    # Metodo para mostrar información de la laptop
    def mostrar_informacion(self):
        return (f"Laptop: {self.marca} {self.modelo}, "
                f"Procesador: {self.procesador}, RAM: {self.ram}GB.")

    # Metodo para obtener el precio (encapsulación)
    def obtener_precio(self):
        return self.__precio

    # Metodo para actualizar el precio (encapsulación)
    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser positivo.")

# Clase derivada
class LaptopGamer(Laptop):
    def __init__(self, marca, modelo, procesador, ram, precio, gpu, taza_refresco):
        super().__init__(marca, modelo, procesador, ram, precio)
        self.gpu = gpu  # Tarjeta gráfica
        self.taza_refresco = taza_refresco  # Tasa de refresco

    # Sobrescribir el metodo mostrar_informacion (polimorfismo)
    def mostrar_informacion(self):
        informacion_base = super().mostrar_informacion()
        return (f"{informacion_base} GPU: {self.gpu}, Tasa de refresco: {self.taza_refresco}Hz.")

# Uso del programa

# Crear instancias de Laptop y LaptopGamer
laptop1 = Laptop("Dell", "Inspiron 15", "Intel i5", 8, 700)
laptop_gamer1 = LaptopGamer("MSI", "Stealth 15", "Intel i7", 16, 1500, "NVIDIA RTX 3060", 144)

# Mostrar información de ambas laptops
print(laptop1.mostrar_informacion())
print(f"Precio: ${laptop1.obtener_precio()}")

print(laptop_gamer1.mostrar_informacion())
print(f"Precio: ${laptop_gamer1.obtener_precio()}")

# Actualizar precio usando el metodo actualizar_precio
laptop1.actualizar_precio(750)
print(f"Nuevo precio de {laptop1.modelo}: ${laptop1.obtener_precio()}")

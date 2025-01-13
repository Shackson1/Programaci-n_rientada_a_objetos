# Conversor de temperaturas usando POO

class ConversorTemperatura:
    """Representa un conversor de temperaturas entre Celsius y Fahrenheit."""
    def __init__(self, temperatura, escala):
        # Inicializa la temperatura y la escala (Celsius o Fahrenheit)
        self.temperatura = temperatura
        self.escala = escala.lower()  # Convierte la escala a minúsculas para evitar errores

    def convertir(self):
        """Convierte la temperatura a la otra escala (Celsius o Fahrenheit)."""
        if self.escala == "celsius":
            # Convierte de Celsius a Fahrenheit
            fahrenheit = (self.temperatura * 9/5) + 32
            return fahrenheit, "Fahrenheit"
        elif self.escala == "fahrenheit":
            # Convierte de Fahrenheit a Celsius
            celsius = (self.temperatura - 32) * 5/9
            return celsius, "Celsius"
        else:
            # Maneja el caso de una escala inválida
            return None, "Escala no válida"

    def mostrar_resultado(self):
        """Muestra el resultado de la conversión de manera formateada."""
        resultado, nueva_escala = self.convertir()
        if resultado is not None:
            print(f"{self.temperatura} grados {self.escala.capitalize()} son {resultado:.2f} grados {nueva_escala}.")
        else:
            print("Escala inválida. Por favor, use 'Celsius' o 'Fahrenheit'.")

# Ejemplo de uso del conversor de temperaturas
temperatura1 = ConversorTemperatura(100, "celsius")  # Se crea una instancia con 100 grados Celsius
temperatura1.mostrar_resultado()  # Muestra el resultado de la conversión
temperatura2 = ConversorTemperatura(212, "fahrenheit")  # Se crea una instancia con 212 grados Fahrenheit
temperatura2.mostrar_resultado()  # Se muestra el resultado de la conversión
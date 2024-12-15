class ClimaSemana:

    #Clase que representa las temperaturas diarias de una semana y permite calcular el promedio.

    def __init__(self):

        #Inicializa la lista de temperaturas.

        self.temperaturas = []

    def ingresar_temperaturas(self):

        #Solicita las temperaturas diarias al usuario.

        for dia in range(1, 8):
            #búcle que solicita las temperaturas de cada día
            while True:
                try:
                    temp = float(input(f"Ingresa la temperatura del día {dia}: "))
                    self.temperaturas.append(temp)
                    break
                except ValueError:
                    print("Por favor, ingresa un número válido.")
    #se calcula el promedio de las temperaturas que se ingresaron
    def calcular_promedio(self):

        if len(self.temperaturas) == 0:
            return 0.0
        return sum(self.temperaturas) / len(self.temperaturas)
    #se muestra el resultado
    def mostrar_resultado(self):
        promedio = self.calcular_promedio()
        print(f"El promedio de temperaturas de la semana es: {promedio:.2f} grados.")


def main():
    print("\n--- Cálculo del Promedio de Temperaturas Semanales ---\n")
    clima_semana = ClimaSemana()
    clima_semana.ingresar_temperaturas()
    clima_semana.mostrar_resultado()

if __name__ == "__main__":
    main()

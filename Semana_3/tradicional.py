def solicitar_temperaturas():

    #Solicita las temperaturas diarias al usuario.

    temperaturas = []
    for dia in range(1, 8):
        while True:

            temp = float(input(f"Ingresa la temperatura del día {dia}: "))
            temperaturas.append(temp)
            break

    return temperaturas
#función que calcula el promedio de temperaturas
def calcular_promedio(temperaturas):

    return sum(temperaturas) / len(temperaturas)

def mostrar_resultado(promedio):
    """
    Muestra el promedio calculado al usuario.
    :param promedio: Valor del promedio semanal.
    """
    print(f"El promedio de temperaturas de la semana es: {promedio:.2f} grados.")

def main():
   #se llama a las funcioes y se muestra el promedio
    print("\n--- Cálculo del Promedio de Temperaturas Semanales ---\n")
    temperaturas = solicitar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    mostrar_resultado(promedio)

if __name__ == "__main__":
    main()

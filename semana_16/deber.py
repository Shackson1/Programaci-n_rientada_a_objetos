import tkinter as tk
from tkinter import messagebox

# Clase que representa la aplicación de gestión de tareas
class AplicacionGestionTareas:
    def __init__(self, ventana):
        self.ventana = ventana  # Ventana principal de la aplicación
        self.ventana.title("Gestión de Tareas")  # Título de la ventana
        self.ventana.geometry("400x400")  # Tamaño de la ventana

        self.tareas = []  # Lista para almacenar las tareas

        # Crear los elementos de la interfaz gráfica
        self.crear_widgets()

        # Vincular los atajos de teclado a las funciones correspondientes
        self.ventana.bind("<Return>", self.agregar_tarea_desde_entrada)
        self.ventana.bind("<c>", self.marcar_tarea_completada)
        self.ventana.bind("<Delete>", self.eliminar_tarea)
        self.ventana.bind("<Escape>", self.cerrar_aplicacion)

    # Función para crear los componentes de la interfaz gráfica
    def crear_widgets(self):
        # Campo de entrada para agregar nuevas tareas
        self.entrada_tarea = tk.Entry(self.ventana, width=30)
        self.entrada_tarea.pack(pady=10)  # Agregar el campo de entrada a la ventana

        # Botón para agregar una tarea
        self.boton_agregar = tk.Button(self.ventana, text="Agregar tarea", command=self.agregar_tarea_desde_boton)
        self.boton_agregar.pack(pady=5)  # Agregar el botón a la ventana

        # Lista donde se mostrarán las tareas
        self.lista_tareas = tk.Listbox(self.ventana, height=10, width=40, selectmode=tk.SINGLE)
        self.lista_tareas.pack(pady=10)  # Agregar la lista a la ventana

        # Botón para marcar una tarea como completada
        self.boton_completar = tk.Button(self.ventana, text="Marcar como completada", command=self.marcar_tarea_completada)
        self.boton_completar.pack(pady=5)  # Agregar el botón a la ventana

        # Botón para eliminar una tarea
        self.boton_eliminar = tk.Button(self.ventana, text="Eliminar tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)  # Agregar el botón a la ventana

    # Función para agregar una tarea desde el campo de entrada al presionar el botón
    def agregar_tarea_desde_boton(self):
        tarea = self.entrada_tarea.get()  # Obtener el texto del campo de entrada
        if tarea != "":
            self.tareas.append({"tarea": tarea, "completada": False})  # Agregar la tarea a la lista de tareas
            self.actualizar_lista_tareas()  # Actualizar la lista visual
            self.entrada_tarea.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingrese una tarea.")  # Mostrar advertencia si el campo está vacío

    # Función para agregar una tarea desde el campo de entrada al presionar "Enter"
    def agregar_tarea_desde_entrada(self, evento):
        self.agregar_tarea_desde_boton()  # Llamar a la función que agrega la tarea

    # Función para marcar una tarea seleccionada como completada
    def marcar_tarea_completada(self, evento=None):
        tarea_seleccionada = self.lista_tareas.curselection()  # Obtener la tarea seleccionada
        if tarea_seleccionada:
            indice = tarea_seleccionada[0]  # Obtener el índice de la tarea seleccionada
            self.tareas[indice]["completada"] = True  # Marcar la tarea como completada
            self.actualizar_lista_tareas()  # Actualizar la lista visual
        else:
            messagebox.showwarning("Selección requerida", "Por favor, seleccione una tarea para marcar como completada.")  # Mostrar advertencia si no hay tarea seleccionada

    # Función para eliminar la tarea seleccionada
    def eliminar_tarea(self, evento=None):
        tarea_seleccionada = self.lista_tareas.curselection()  # Obtener la tarea seleccionada
        if tarea_seleccionada:
            indice = tarea_seleccionada[0]  # Obtener el índice de la tarea seleccionada
            del self.tareas[indice]  # Eliminar la tarea de la lista
            self.actualizar_lista_tareas()  # Actualizar la lista visual
        else:
            messagebox.showwarning("Selección requerida", "Por favor, seleccione una tarea para eliminar.")  # Mostrar advertencia si no hay tarea seleccionada

    # Función para actualizar la lista visual de tareas
    def actualizar_lista_tareas(self):
        self.lista_tareas.delete(0, tk.END)  # Limpiar la lista
        for tarea in self.tareas:
            if tarea["completada"]:
                self.lista_tareas.insert(tk.END, f"{tarea['tarea']} - Completada")  # Mostrar tareas completadas
            else:
                self.lista_tareas.insert(tk.END, tarea["tarea"])  # Mostrar tareas pendientes

    # Función para cerrar la aplicación al presionar "Escape"
    def cerrar_aplicacion(self, evento=None):
        self.ventana.quit()  # Cerrar la ventana de la aplicación

# Código para ejecutar la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()  # Crear la ventana principal
    aplicacion = AplicacionGestionTareas(ventana)  # Crear una instancia de la aplicación
    ventana.mainloop()  # Iniciar el bucle de la interfaz gráfica

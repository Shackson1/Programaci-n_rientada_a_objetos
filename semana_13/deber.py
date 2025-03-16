#importamos la libreria
import tkinter as tk
from tkinter import ttk

# Función para agregar un elemento a la tabla
def agregar_elemento():
    dato = entrada_texto.get()
    if dato:
        tabla.insert("", "end", values=(dato,))
        entrada_texto.delete(0, tk.END)  # Limpiar solo el campo de texto después de agregar

# Función para limpiar la entrada de texto y la tabla
def limpiar_datos():
    entrada_texto.delete(0, tk.END)  # Limpia el campo de texto
    for item in tabla.get_children():
        tabla.delete(item)  # Borra todos los datos de la tabla

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")
ventana.geometry("400x300")

# Etiqueta y campo de texto para ingresar datos
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=5)

entrada_texto = tk.Entry(ventana)
entrada_texto.pack(pady=5)

# Frame para organizar los botones en la misma fila
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

# Botón para agregar datos
boton_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_elemento)
boton_agregar.pack(side=tk.LEFT, padx=5)

# Botón para limpiar la entrada y la tabla
boton_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack(side=tk.LEFT, padx=5)

# Tabla para mostrar datos
tabla = ttk.Treeview(ventana, columns=("Dato"), show="headings")
tabla.heading("Dato", text="Dato Ingresado")
tabla.pack(pady=5, fill=tk.BOTH, expand=True)

# Ejecutar la aplicación
ventana.mainloop()

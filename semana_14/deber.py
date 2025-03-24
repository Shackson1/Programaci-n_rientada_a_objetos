# Importamos las librerías necesarias
import tkinter as tk  # Para crear la interfaz gráfica
from tkinter import ttk, messagebox  # ttk: widgets mejorados, messagebox: cuadros de diálogo
from tkcalendar import DateEntry  # Para el selector de fechas tipo calendario

# Creamos la ventana principal de la aplicación
root = tk.Tk()
root.title("Agenda Personal")  # Título de la ventana
root.geometry("620x450")  # Tamaño fijo de la ventana
root.resizable(False, False)  # No permite redimensionar


# =====================================================
# FUNCIONES PRINCIPALES DE LA LÓGICA DEL PROGRAMA
# =====================================================

def agregar_evento():
    """
    Función que se ejecuta al presionar el botón 'Agregar Evento'.
    Toma los valores de los campos de entrada y los agrega al TreeView.
    """
    fecha = entry_fecha.get()  # Obtiene la fecha seleccionada
    hora = entry_hora.get()  # Obtiene el texto ingresado en hora
    descripcion = entry_desc.get()  # Obtiene el texto ingresado en descripción

    # Verifica que todos los campos estén llenos
    if fecha and hora and descripcion:
        # Inserta los datos como una nueva fila en el TreeView
        tree.insert("", "end", values=(fecha, hora, descripcion))

        # Limpia los campos de entrada (excepto la fecha)
        entry_hora.delete(0, tk.END)
        entry_desc.delete(0, tk.END)
    else:
        # Muestra una advertencia si faltan campos por llenar
        messagebox.showwarning("Datos incompletos", "Por favor, completa todos los campos.")


def eliminar_evento():
    """
    Elimina el evento seleccionado del TreeView.
    Solicita confirmación mediante un cuadro de diálogo.
    """
    selected_item = tree.selection()  # Obtiene el evento seleccionado

    # Verifica que se haya seleccionado algún evento
    if not selected_item:
        messagebox.showinfo("Selecciona un evento", "Primero selecciona un evento para eliminar.")
        return

    # Solicita confirmación al usuario
    confirm = messagebox.askyesno("Eliminar Evento", "¿Estás seguro que deseas eliminar el evento?")
    if confirm:
        # Elimina el ítem seleccionado del TreeView
        tree.delete(selected_item)


def salir_app():
    """
    Cierra la aplicación completamente.
    """
    root.quit()


# =====================================================
# SECCIÓN 1: ENTRADA DE DATOS (Fecha, Hora, Descripción)
# =====================================================

# Frame que agrupa los campos de entrada
frame_entrada = tk.LabelFrame(root, text="Nuevo Evento", padx=10, pady=10)
frame_entrada.pack(fill="x", padx=10, pady=5)

# Etiqueta y campo para la Fecha (usa un DateEntry tipo calendario)
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_fecha = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y campo para la Hora
tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
entry_hora = tk.Entry(frame_entrada, width=10)
entry_hora.grid(row=0, column=3, padx=5, pady=5)

# Etiqueta y campo para la Descripción del evento
tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_desc = tk.Entry(frame_entrada, width=50)
entry_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

# =====================================================
# SECCIÓN 2: LISTA DE EVENTOS PROGRAMADOS (TreeView)
# =====================================================

# Frame que contiene la tabla de eventos
frame_lista = tk.LabelFrame(root, text="Eventos Programados", padx=10, pady=10)
frame_lista.pack(fill="both", expand=True, padx=10, pady=5)

# Creamos el widget TreeView para mostrar los eventos en columnas
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings", height=8)

# Configuramos los encabezados de las columnas
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")

# Establecemos el ancho de cada columna
tree.column("Fecha", width=100)
tree.column("Hora", width=80)
tree.column("Descripción", width=360)

# Añadimos el TreeView al frame
tree.pack(fill="both", expand=True)

# =====================================================
# SECCIÓN 3: BOTONES DE ACCIÓN (Agregar, Eliminar, Salir)
# =====================================================

# Frame que contiene los botones de acción
frame_botones = tk.Frame(root)
frame_botones.pack(fill="x", padx=10, pady=10)

# Botón para agregar evento
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", width=20, command=agregar_evento)
btn_agregar.pack(side="left", padx=10)

# Botón para eliminar evento seleccionado
btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", width=25, command=eliminar_evento)
btn_eliminar.pack(side="left", padx=10)

# Botón para salir de la aplicación
btn_salir = tk.Button(frame_botones, text="Salir", width=15, command=salir_app)
btn_salir.pack(side="right", padx=10)

# =====================================================
# INICIO DEL LOOP PRINCIPAL DE LA APLICACIÓN
# =====================================================

# Inicia la ejecución de la ventana principal de Tkinter
root.mainloop()

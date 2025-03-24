import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Crear ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("620x450")
root.resizable(False, False)

# =============================
# Funciones
# =============================

def agregar_evento():
    """Añade un evento nuevo a la lista."""
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_desc.get()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        entry_hora.delete(0, tk.END)
        entry_desc.delete(0, tk.END)
    else:
        messagebox.showwarning("Datos incompletos", "Por favor, completa todos los campos.")

def eliminar_evento():
    """Elimina el evento seleccionado, con confirmación."""
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showinfo("Selecciona un evento", "Primero selecciona un evento para eliminar.")
        return

    confirm = messagebox.askyesno("Eliminar Evento", "¿Estás seguro que deseas eliminar el evento?")
    if confirm:
        tree.delete(selected_item)

def salir_app():
    """Cierra la aplicación."""
    root.quit()

# =============================
# Sección: Entrada de Datos
# =============================

frame_entrada = tk.LabelFrame(root, text="Nuevo Evento", padx=10, pady=10)
frame_entrada.pack(fill="x", padx=10, pady=5)

tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_fecha = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
entry_hora = tk.Entry(frame_entrada, width=10)
entry_hora.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_desc = tk.Entry(frame_entrada, width=50)
entry_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

# =============================
# Sección: Lista de Eventos
# =============================

frame_lista = tk.LabelFrame(root, text="Eventos Programados", padx=10, pady=10)
frame_lista.pack(fill="both", expand=True, padx=10, pady=5)

tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings", height=8)
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.column("Fecha", width=100)
tree.column("Hora", width=80)
tree.column("Descripción", width=360)
tree.pack(fill="both", expand=True)

# =============================
# Sección: Botones de Acción
# =============================

frame_botones = tk.Frame(root)
frame_botones.pack(fill="x", padx=10, pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", width=20, command=agregar_evento)
btn_agregar.pack(side="left", padx=10)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", width=25, command=eliminar_evento)
btn_eliminar.pack(side="left", padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", width=15, command=salir_app)
btn_salir.pack(side="right", padx=10)

# Ejecutar la aplicación
root.mainloop()

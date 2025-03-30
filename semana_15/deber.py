import tkinter as tk
from tkinter import messagebox

# Creamos la ventana principal
root = tk.Tk()
root.title("Lista de Tareas - Variante 1")
root.geometry("400x400")

# Lista para almacenar las tareas
tasks = []

# Funciones (Manejadores de Eventos)
def add_task(event=None):
    task = entry.get().strip()
    if task:
        tasks.append({"text": task, "completed": False})
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Campo Vacío", "Por favor escribe una tarea.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        display = task["text"] + (" [Hecho]" if task["completed"] else "")
        listbox.insert(tk.END, display)

def mark_completed():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = not tasks[index]["completed"]
        update_listbox()
    else:
        messagebox.showinfo("Selecciona una tarea", "Debes seleccionar una tarea para marcarla.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        update_listbox()
    else:
        messagebox.showinfo("Selecciona una tarea", "Debes seleccionar una tarea para eliminarla.")

# Componentes de la interfaz
title = tk.Label(root, text="Lista de Tareas", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)
entry.bind("<Return>", add_task)  # Asociamos la tecla Enter a agregar tareas

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Añadir Tarea", width=15, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

complete_btn = tk.Button(btn_frame, text="Marcar como Completada", width=20, command=mark_completed)
complete_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(root, text="Eliminar Tarea", width=20, command=delete_task)
delete_btn.pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Iniciar la aplicación
root.mainloop()

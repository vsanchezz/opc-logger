import customtkinter as ctk
from tkinter import filedialog

# Configuración inicial de CustomTkinter
ctk.set_appearance_mode("System")  # Modo de apariencia (System, Light, Dark)
ctk.set_default_color_theme("blue")  # Tema de color

# Función para abrir el diálogo de selección de carpeta
def seleccionar_carpeta():
    carpeta_seleccionada = filedialog.askdirectory(title="Seleccionar Carpeta")
    if carpeta_seleccionada:  # Si se selecciona una carpeta
        entry_path.delete(0, ctk.END)  # Borra el contenido actual del campo de texto
        entry_path.insert(0, carpeta_seleccionada)  # Inserta el path de la carpeta seleccionada

# Crear la ventana principal
ventana = ctk.CTk()
ventana.title("Seleccionar Carpeta")
ventana.geometry("500x150")

# Crear un frame para organizar los widgets
frame = ctk.CTkFrame(ventana)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Campo de texto para mostrar/ingresar el path de la carpeta
entry_path = ctk.CTkEntry(frame, placeholder_text="Ingresa el path de la carpeta", width=350)
entry_path.grid(row=0, column=0, padx=10, pady=10)

# Botón "Examinar" para abrir el diálogo de selección de carpeta
btn_examinar = ctk.CTkButton(frame, text="Examinar", command=seleccionar_carpeta)
btn_examinar.grid(row=0, column=1, padx=10, pady=10)

# Ejecutar la aplicación
ventana.mainloop()
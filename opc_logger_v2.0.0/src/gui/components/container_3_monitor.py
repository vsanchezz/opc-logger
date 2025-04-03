import sys
import customtkinter as ctk
from tkinter.scrolledtext import ScrolledText


class ContainerMonitor(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Crear un widget de texto con scroll para mostrar los logs
        self.text_widget = ScrolledText(
            self,
            wrap="word",
            state="disabled",
            height=20,
            width=80,
            bg="black",  # Fondo negro
            fg="#D4D4D4",  # Texto gris claro (como en Visual Studio)
            insertbackground="#D4D4D4",  # Cursor gris claro
            font=("Consolas", 12),  # Fuente alternativa si Cascadia Code no está disponible
        )
        self.text_widget.pack(fill="both", expand=True, padx=10, pady=(10, 0))

        # Crear un botón "Clear" para borrar el contenido del widget de texto
        self.clear_button = ctk.CTkButton(self, text="Clear", command=self.clear_text)
        self.clear_button.pack(side = 'left', padx = 10, pady=10)

        # Redirigir la salida estándar (stdout) al widget de texto
        self.stdout = sys.stdout  # Guardar el stdout original
        sys.stdout = self  # Redirigir stdout a esta clase

    def write(self, message):
        """Escribe el mensaje en el widget de texto."""
        self.text_widget.configure(state="normal")  # Habilitar edición temporalmente
        self.text_widget.insert("end", message)  # Insertar el mensaje al final
        self.text_widget.configure(state="disabled")  # Deshabilitar edición
        self.text_widget.see("end")  # Hacer scroll automático al final

    def flush(self):
        """Método requerido para redirigir stdout (no hace nada aquí)."""
        pass

    def clear_text(self):
        """Borra todo el contenido del widget de texto."""
        self.text_widget.configure(state="normal")  # Habilitar edición temporalmente
        self.text_widget.delete("1.0", "end")  # Borrar todo el contenido
        self.text_widget.configure(state="disabled")  # Deshabilitar edición

    def destroy(self):
        """Restaurar stdout original al destruir el frame."""
        sys.stdout = self.stdout  # Restaurar stdout original
        super().destroy()

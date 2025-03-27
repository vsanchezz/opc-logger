import sys
import customtkinter as ctk

class ConsoleEcho(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        # Crear el área de texto para la consola
        self.console = ctk.CTkTextbox(self, width=600, height=400)
        self.console.pack(padx=10, pady=10, fill="both", expand=True)

        # Crear un segundo textbox para errores (en rojo)
        self.error_console = ctk.CTkTextbox(self, width=600, height=100, text_color="red")
        self.error_console.pack(padx=10, pady=(0, 10), fill="both", expand=True)

        # Guardar los stdout y stderr originales
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr

        # Crear los redirectores
        self.stdout_redirector = StdoutEcho(self.console, self.original_stdout)
        self.stderr_redirector = StdoutEcho(self.error_console, self.original_stderr)

        # Iniciar la redirección
        sys.stdout = self.stdout_redirector
        sys.stderr = self.stderr_redirector

        # Botón para limpiar
        self.clear_button = ctk.CTkButton(self, text="Limpiar", command=self.clear_console)
        self.clear_button.pack(pady=(0, 10))

    def clear_console(self):
        self.console.delete("1.0", "end")
        self.error_console.delete("1.0", "end")

    def cleanup(self):
        # Restaurar stdout y stderr originales
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr

class StdoutEcho:
    def __init__(self, text_widget, original_stream):
        self.text_widget = text_widget
        self.original_stream = original_stream

    def write(self, string):
        # Escribir en la consola original
        self.original_stream.write(string)

        # Escribir en el widget de texto
        if string:
            self.text_widget.insert("end", string)
            self.text_widget.see("end")

    def flush(self):
        self.original_stream.flush()

# Función principal para ejecutar la aplicación
def main():
    # Configurar el tema light antes de crear la aplicación
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.title("Console Echo")
    app.geometry("700x600")

    console = ConsoleEcho(app)
    console.pack(padx=20, pady=20, fill="both", expand=True)

    def on_closing():
        console.cleanup()
        app.destroy()

    app.protocol("WM_DELETE_WINDOW", on_closing)

    # Imprimir algunos mensajes de prueba
    for i in range(20):          
        print("Aplicación iniciada correctamente")
        print("Este mensaje debería aparecer tanto en la terminal como en la GUI")
        print("Los errores aparecerán en el área roja", file=sys.stderr)

    app.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
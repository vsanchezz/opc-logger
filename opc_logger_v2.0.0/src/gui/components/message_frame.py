import customtkinter as ctk
import threading
import time

class MessageFrame(ctk.CTkFrame):
    def __init__(self, master, event_bus_mw, **kwargs):
        """
        Inicializa un frame con un label para mostrar mensajes temporales
        """
        super().__init__(master, **kwargs)
        self.event_bus_mw = event_bus_mw

        # Crear el label dentro del frame
        self.message_label = ctk.CTkLabel(
            self,
            text="",
            font = ("Arial", 14,'italic')
        )
        self.message_label.pack(side='right', padx=10)

        # Lock para manejar múltiples mensajes
        self.message_lock = threading.Lock()

        # subscribe to events to show messages
        self.event_bus_mw.subscribe("SaveConfiguration",self.show_message,'Configuration saved')
        

    def show_message(self,data, message):
        """
        Muestra un mensaje en el label por 3 segundos y luego lo borra
        """
        thread = threading.Thread(target=self._display_and_clear, args=(message,))
        thread.daemon = True
        thread.start()

    def _display_and_clear(self, message):
        """
        Método interno para mostrar y limpiar el mensaje
        """
        with self.message_lock:
            self.message_label.configure(text=message)
            time.sleep(3)
            self.message_label.configure(text="")
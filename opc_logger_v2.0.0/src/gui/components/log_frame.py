import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class LogFrame(ctk.CTkFrame):
    def __init__(self, parent, event_bus_mw, *args, **kwargs):
        """
        Inicializa el frame y se suscribe al evento 'UpdateLog'.
        :param parent: El widget padre.
        :param event_bus: Sistema de eventos al que se suscribe.
        """
        super().__init__(parent, *args, **kwargs)

        self.event_bus_mw = event_bus_mw
        self.event_bus_mw.subscribe('UpdateLog', self.update_frame)  # Suscribirse al evento
        self.columns = []  # Columnas detectadas dinámicamente
        self.data = []  # Datos actuales del log

        # Crear un contenedor para el Treeview y los Scrollbars
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Crear un Treeview para mostrar los datos
        self.tree = ttk.Treeview(self.table_frame, show="headings")
        self.tree.grid(row=0, column=0, sticky="nsew")  # Usar grid para mejor control del diseño

        # Agregar un scrollbar vertical para la tabla
        self.scrollbar_vertical = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.tree.yview)
        self.scrollbar_vertical.grid(row=0, column=1, sticky="ns")  # Colocar el scrollbar al lado derecho

        # Agregar un scrollbar horizontal para la tabla
        self.scrollbar_horizontal = ttk.Scrollbar(self.table_frame, orient="horizontal", command=self.tree.xview)
        self.scrollbar_horizontal.grid(row=1, column=0, sticky="ew")  # Colocar el scrollbar en la parte inferior

        # Configurar el Treeview para usar los Scrollbars
        self.tree.configure(yscrollcommand=self.scrollbar_vertical.set, xscrollcommand=self.scrollbar_horizontal.set)

        # Asegurar que el contenedor se expanda correctamente
        self.table_frame.grid_rowconfigure(0, weight=1)
        self.table_frame.grid_columnconfigure(0, weight=1)

    def update_frame(self, logs):
        """
        Actualiza el frame con el log recibido.
        :param logs: Lista de diccionarios con los datos del log.
        """
        if not logs:
            self.clear_table()
            return

        # Detectar columnas dinámicamente solo si cambian
        if not self.columns or self.columns != list(logs[0].keys()):
            self.columns = list(logs[0].keys())  # Obtener las claves del primer registro
            self.tree["columns"] = self.columns
            for col in self.columns:
                self.tree.heading(col, text=col)  # Configurar encabezados
                self.tree.column(col, anchor="center", width=150)  # Configurar ancho y alineación

        # Obtener los valores actuales en el Treeview
        existing_items = set(
            tuple(str(value) for value in self.tree.item(item, "values"))  # Convertir todos los valores a cadenas
            for item in self.tree.get_children()
        )

        # Agregar solo los nuevos datos
        for row in logs:
            values = tuple(str(row.get(col, "")) for col in self.columns)  # Convertir todos los valores a cadenas
            if values not in existing_items:  # Solo agregar si no está ya en el Treeview
                self.tree.insert("", "end", values=values)

    def display(self):
        """
        Muestra el contenido del log en el Treeview.
        """
        # Limpiar la tabla antes de agregar nuevos datos
        self.clear_table()

        # Agregar filas al Treeview
        for row in self.data:
            values = [row.get(col, "") for col in self.columns]
            self.tree.insert("", "end", values=values)

    def clear_table(self):
        """
        Limpia todos los datos del Treeview.
        """
        for item in self.tree.get_children():
            self.tree.delete(item)
    
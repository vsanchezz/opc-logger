import customtkinter as ctk

class SettingsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Frame para configuración del servidor
        self.server_frame = ctk.CTkFrame(self)
        self.server_frame.pack(fill="x", padx=10, pady=10)

        # Etiqueta para la dirección del servidor
        self.server_label = ctk.CTkLabel(
            self.server_frame,
            text="OPC Server Address:",
            anchor="w"
        )
        self.server_label.pack(anchor="w", padx=10, pady=5)

        # Campo para la dirección del servidor
        self.server_entry = ctk.CTkEntry(
            self.server_frame,
            width=300,
            placeholder_text="opc.tcp://localhost:4840"
        )
        self.server_entry.pack(anchor="w", padx=10, pady=5)

        # Frame para selección de variables
        self.variables_frame = ctk.CTkFrame(self)
        self.variables_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Etiqueta para selección de variables
        self.variables_label = ctk.CTkLabel(
            self.variables_frame,
            text="Select OPC Variables to Log:",
            anchor="w"
        )
        self.variables_label.pack(anchor="w", padx=10, pady=5)

        # Contenedor para variables (scrollable)
        self.variables_container = ctk.CTkScrollableFrame(
            self.variables_frame,
            width=300,
            height=300
        )
        self.variables_container.pack(fill="both", expand=True, padx=10, pady=5)

        # Botón para guardar configuración
        self.save_config_button = ctk.CTkButton(
            self,
            text="Save Configuration",
            command=self.save_configuration,
            width=150
        )
        self.save_config_button.pack(side="right", padx=10, pady=10)

        # Callback para guardar configuración
        self.on_save_config = None

    def set_callbacks(self, on_save_config=None):
        """Establecer callbacks para eventos"""
        self.on_save_config = on_save_config

    def save_configuration(self):
        """Guardar configuración"""
        server_address = self.server_entry.get()

        # Notificar a través del callback
        if self.on_save_config:
            self.on_save_config(server_address)

    def get_server_address(self):
        """Obtener dirección del servidor"""
        return self.server_entry.get()

    def set_server_address(self, address):
        """Establecer dirección del servidor"""
        self.server_entry.delete(0, "end")
        self.server_entry.insert(0, address)

    def add_variable_checkbox(self, variable_name, checked=False):
        """Añadir checkbox para una variable OPC"""
        var = ctk.BooleanVar(value=checked)
        checkbox = ctk.CTkCheckBox(
            self.variables_container,
            text=variable_name,
            variable=var
        )
        checkbox.pack(anchor="w", padx=10, pady=2)
        return var

    def clear_variables(self):
        """Limpiar todas las variables"""
        for widget in self.variables_container.winfo_children():
            widget.destroy()
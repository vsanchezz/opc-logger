import customtkinter as ctk

class ContainerSettings(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Frame para configuración del servidor
        self.server_frame = ctk.CTkFrame(self, fg_color = 'transparent')
        self.server_frame.pack(fill="both", padx=10, pady=10)

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
        self.variables_frame = ctk.CTkFrame(self, fg_color = 'transparent')
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
            fg_color = 'white',
            width=300,
            height=300,
        )
        self.variables_container.pack(fill="both", expand=True, padx=10, pady=5)

        # Botón para guardar configuración
        self.save_config_button = ctk.CTkButton(
            self.variables_frame,
            text="Save Configuration",
            #command=self.save_configuration,
            width=150
        )
        self.save_config_button.pack(side="right", padx=10, pady=10)


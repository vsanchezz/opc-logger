import customtkinter as ctk

class ContainerSettings(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)

        # Frame para configuración del servidor
        self.event_bus_mw = master.event_bus_mw
        self.server_frame = ctk.CTkFrame(self, fg_color = 'transparent')
        self.server_frame.pack(fill="both", padx=10, pady=5)

        # Etiqueta para la dirección del servidor
        self.server_label = ctk.CTkLabel(
            self.server_frame,
            text="OPC Server Address:",
            anchor="w"
        )
        self.server_label.pack(anchor="w", padx=0, pady=5)

        # Campo para la dirección del servidor
        self.server_ip_entry = ctk.CTkEntry(
            self.server_frame,
            width=300,
            placeholder_text="opc.tcp://localhost:4840"
        )
        self.server_ip_entry.pack(anchor="w", padx=10, pady=5)

        # Etiqueta para la frecuencia del logging
        self.freq_label = ctk.CTkLabel(
            self.server_frame,
            text="Logging frequency (s):",
            anchor="w"
        )
        self.freq_label.pack(anchor="w", padx=0, pady=5)

        # Campo para la frequencia del logging
        self.freq_entry = ctk.CTkEntry(
            self.server_frame,
            width=300,
        )
        self.freq_entry.pack(anchor="w", padx=10, pady=5)

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
            command= self.save_configuration,
            width=150
        )
        self.save_config_button.pack(side="right", padx=10, pady=10)

    def update_config(self,config):
        self.server_ip_entry.delete(0,'end')
        self.server_ip_entry.insert(0,config['server_ip'])
        self.freq_entry.delete(0,'end')
        self.freq_entry.insert(0,config['logging_freq'])
    
    def save_configuration(self):
        config = {}
        config['server_ip'] = self.server_ip_entry.get()
        config['logging_freq'] = self.freq_entry.get()
        self.event_bus_mw.publish("SaveConfiguration",config)


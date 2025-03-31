import customtkinter as ctk

class ContainerSettings(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)

        self.event_bus_mw = master.event_bus_mw

        # frame para campos de configuracion
        self.config_frame = ctk.CTkFrame(self, fg_color = 'transparent')
        self.config_frame.pack(fill='both', padx = 10, pady = 5)

        # Configurar las columnas del grid con los anchos especificados
        self.config_frame.grid_columnconfigure(0, weight=1, minsize=200)  # Primera columna: ancho mínimo 200
        self.config_frame.grid_columnconfigure(1, weight=1, minsize=300)  # Segunda columna: ancho mínimo 300
        self.config_frame.grid_columnconfigure(2, weight=1, minsize=100)  # Tercera columna: ancho mínimo 100

        for i in range(3):  # Tres filas
            self.config_frame.grid_rowconfigure(i, weight=1)

        # Etiqueta para la dirección del servidor
        self.server_ip_label = ctk.CTkLabel(
            self.config_frame,
            text="OPC Server Address:",
            justify="left",
        )
        self.server_ip_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Campo para la dirección del servidor
        self.server_ip_entry = ctk.CTkEntry(
            self.config_frame,
        )
        self.server_ip_entry.grid(row=0, column=1, padx=0, pady=5, sticky="nsew")

        # Etiqueta para la frecuencia del logging
        self.freq_label = ctk.CTkLabel(
            self.config_frame,
            text="Logging frequency (s):",
            justify="left",
        )
        self.freq_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Campo para la frequencia del logging
        self.freq_entry = ctk.CTkEntry(
            self.config_frame,
        )
        self.freq_entry.grid(row=1, column=1, padx=0, pady=5, sticky="nsew")

        # Etiqueta para el path de la carpeta donde se guardaran los archivos csv
        self.path_label = ctk.CTkLabel(
            self.config_frame,
            text="Data path:",
            justify="left",
        )
        self.path_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # Campo para el path de la carpeta donde se guardaran los archivos csv
        self.path_entry = ctk.CTkEntry(
            self.config_frame,
        )
        self.path_entry.grid(row=2, column=1, padx=0, pady=5, sticky="nsew")

        ### Frame para selección de variables
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


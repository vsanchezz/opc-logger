import customtkinter as ctk

class ContainerMain(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Control panel
        self.control_panel = ctk.CTkFrame(self, corner_radius=0)
        self.control_panel.pack(side = 'bottom', fill="x", padx=(0,0), pady=0)

        # Connection button
        self.connect_button = ctk.CTkButton(
            self.control_panel,
            text="Connect",
            #command=self.toggle_connection,
            width=120
        )
        self.connect_button.pack(side="left", padx=10, pady=10)

        # Start button
        self.start_button = ctk.CTkButton(
            self.control_panel,
            text="Start Logging",
            #command=self.start_logging,
            state="disabled",
            width=120
        )
        self.start_button.pack(side="left", padx=10, pady=10)

        # Stop button
        self.stop_button = ctk.CTkButton(
            self.control_panel,
            text="Stop Logging",
            #command=self.stop_logging,
            state="disabled",
            width=120
        )
        self.stop_button.pack(side="left", padx=10, pady=10)

        # Visualization area
        self.data_frame = ctk.CTkFrame(self, corner_radius=0)
        self.data_frame.pack(fill="both", expand=True, padx=(0,0), pady=00)

        # Etiqueta para el área de datos
        self.data_label = ctk.CTkLabel(
            self.data_frame,
            text="Collected Data:",
            anchor="w",
            
        )
        self.data_label.pack(anchor="w", padx=10, pady=5)

        # Área de texto para mostrar datos
        self.data_text = ctk.CTkTextbox(
            self.data_frame,
            wrap="none",
            font=("Consolas", 12)
        )
        self.data_text.pack(fill="both", expand=True, padx=10, pady=5)
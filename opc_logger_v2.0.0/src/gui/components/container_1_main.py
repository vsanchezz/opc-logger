import customtkinter as ctk
from src.gui.components.log_frame           import LogFrame

class ContainerMain(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color = 'transparent', **kwargs)

        # events
        self.event_bus_mw = master.event_bus_mw
        self.event_bus_mw.subscribe('StatusUpdate', self.status_update)

        # Control panel
        self.control_panel = ctk.CTkFrame(self, corner_radius=0)
        self.control_panel.pack(side = 'bottom', fill="x", padx=(0,0), pady=0)

        # Connection button
        self.connect_button = ctk.CTkButton(
            self.control_panel,
            text="Connect",
            command=self.toggle_connection,
            width=120
        )
        self.connect_button.pack(side="left", padx=10, pady=10)

        # Start button
        self.start_button = ctk.CTkButton(
            self.control_panel,
            text="Start Logging",
            command=self.start_logging,
            state="disabled",
            width=120
        )
        self.start_button.pack(side="left", padx=10, pady=10)

        # Stop button
        self.stop_button = ctk.CTkButton(
            self.control_panel,
            text="Stop Logging",
            command=self.stop_logging,
            state="disabled",
            width=120
        )
        self.stop_button.pack(side="left", padx=10, pady=10)

        # Visualization area
        self.data_frame = ctk.CTkFrame(self, corner_radius=0)
        self.data_frame.pack(fill="both", expand=True, padx=(0,0), pady=0)

        # Etiqueta para el área de datos
        self.data_label = ctk.CTkLabel(
            self.data_frame,
            text="Collected Data:",
            anchor="w",
            height=40
        )
        self.data_label.pack(anchor="w", padx=10, pady=5)

        # Área de texto para mostrar datos
        '''
        self.data_text = ctk.CTkTextbox(
            self.data_frame,
            wrap="none",
            font=("Consolas", 12)
        )
        self.data_text.pack(fill="both", expand=True, padx=10, pady=5)
        '''
        self.log_frame = LogFrame(self.data_frame, self.event_bus_mw)
        self.log_frame.pack(fill="both", expand=True, padx=10, pady=5)
        #'''
    def toggle_connection(self):
        if (self.connect_button.cget('text') == 'Connect') :
            self.connect_button.configure(text='Disconnect')
            self.event_bus_mw.publish('Connect',{})

        else:
            self.connect_button.configure(text='Connect')
            self.event_bus_mw.publish('Disconnect',{})
    
    def status_update(self, data):
        if data['status'] == 'Connected' :
            self.start_button.configure(state='enabled')
        
        else:
            self.start_button.configure(state='disabled')
            self.connect_button.configure(text='Connect')

    def start_logging(self):
        self.start_button.configure(state='disabled')
        self.stop_button.configure(state='enabled')
        self.event_bus_mw.publish('StartLogging',{})
    
    def stop_logging(self):
        self.start_button.configure(state='enabled')
        self.stop_button.configure(state='disabled')
        self.event_bus_mw.publish('StopLogging',{})
        


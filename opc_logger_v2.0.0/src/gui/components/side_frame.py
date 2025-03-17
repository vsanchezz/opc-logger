import customtkinter as ctk

class SideFrame(ctk.CTkFrame):
    def __init__(self, master, event_bus_mw, **kwargs):
        super().__init__(master, width=150, **kwargs)
        self.event_bus_mw = event_bus_mw

        # Botones de navegación
        self.main_button = ctk.CTkButton(
            self,
            text="Main",
            command = self.main_clicked,
            width=180,
            height=40,
            corner_radius=0,
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray75", "gray30")
        )
        self.main_button.pack(pady=(0, 5))

        self.settings_button = ctk.CTkButton(
            self,
            text="Settings",
            command = self.settings_clicked,
            width=180,
            height=40,
            corner_radius=0,
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30")
        )
        self.settings_button.pack(pady=5)

        # Resaltar el botón activo por defecto
        self.update_active_button("main")

    def main_clicked(self):
        self.event_bus_mw.publish("MainClicked",{})
        self.update_active_button("main")

    def settings_clicked(self):
        self.event_bus_mw.publish("SettingsClicked",{})
        self.update_active_button("settings")
    
    def update_active_button(self, frame_name):
        """Actualizar el estilo del botón activo"""
        self.main_button.configure(fg_color=("gray75", "gray10") if frame_name == "main" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray10") if frame_name == "settings" else "transparent")
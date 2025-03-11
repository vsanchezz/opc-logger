import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, show_frame_callback, **kwargs):
        super().__init__(master, width=200, **kwargs)

        self.show_frame_callback = show_frame_callback
        self.current_frame = "main"

        # Título de la aplicación en la barra lateral
        self.app_title = ctk.CTkLabel(
            self,
            text="OPC Data Logger",
            font=("Arial", 16, "bold")
        )
        self.app_title.pack(pady=(20, 30))

        # Botones de navegación
        self.main_button = ctk.CTkButton(
            self,
            text="Main",
            command=lambda: self.navigate_to("main"),
            width=180,
            height=40,
            corner_radius=0,
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30")
        )
        self.main_button.pack(pady=(0, 5))

        self.settings_button = ctk.CTkButton(
            self,
            text="Settings",
            command=lambda: self.navigate_to("settings"),
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

    def navigate_to(self, frame_name):
        """Navegar al frame seleccionado"""
        self.update_active_button(frame_name)
        self.show_frame_callback(frame_name)
        self.current_frame = frame_name

    def update_active_button(self, frame_name):
        """Actualizar el estilo del botón activo"""
        self.main_button.configure(fg_color=("gray75", "gray25") if frame_name == "main" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if frame_name == "settings" else "transparent")
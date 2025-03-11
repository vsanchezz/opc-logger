import tkinter as tk
from tkinter import ttk

class DashboardExample:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard con Grid")
        self.root.geometry("800x600")

        # Configurar expansión de filas y columnas
        for i in range(4):  # 4 columnas
            root.grid_columnconfigure(i, weight=1)
        for i in range(6):  # 6 filas
            root.grid_rowconfigure(i, weight=1)

        self.create_widgets()

    def create_widgets(self):
        # 1. Header - Span completo en la parte superior
        header_frame = ttk.Frame(self.root, style='Header.TFrame')
        header_frame.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        ttk.Label(
            header_frame,
            text="Dashboard Example",
            font=('Helvetica', 24)
        ).pack(pady=10)

        # 2. Panel lateral - Ocupa varias filas
        side_panel = ttk.LabelFrame(self.root, text="Navigation")
        side_panel.grid(row=1, column=0, rowspan=4, sticky="nsew", padx=5, pady=5)

        buttons = ["Home", "Profile", "Settings", "Reports"]
        for i, text in enumerate(buttons):
            ttk.Button(side_panel, text=text).grid(
                row=i, column=0, pady=5, padx=10, sticky="ew"
            )

        # 3. Panel principal - Ocupa 2 columnas y 2 filas
        main_panel = ttk.LabelFrame(self.root, text="Main Content")
        main_panel.grid(
            row=1, column=1, columnspan=2, rowspan=2,
            sticky="nsew", padx=5, pady=5
        )

        # Contenido del panel principal
        ttk.Label(
            main_panel,
            text="Welcome to the Dashboard",
            font=('Helvetica', 16)
        ).grid(row=0, column=0, pady=20)

        ttk.Label(
            main_panel,
            text="This is a demonstration of grid layout with spans",
            wraplength=300
        ).grid(row=1, column=0, pady=10)

        # 4. Panel de estadísticas - Una columna, dos filas
        stats_panel = ttk.LabelFrame(self.root, text="Statistics")
        stats_panel.grid(
            row=1, column=3, rowspan=2,
            sticky="nsew", padx=5, pady=5
        )

        stats = ["Users: 1,234", "Active: 891", "Posts: 4,567"]
        for i, stat in enumerate(stats):
            ttk.Label(stats_panel, text=stat).grid(
                row=i, column=0, pady=10, padx=5
            )

        # 5. Panel inferior izquierdo
        bottom_left = ttk.LabelFrame(self.root, text="Recent Activity")
        bottom_left.grid(
            row=3, column=1, rowspan=2,
            sticky="nsew", padx=5, pady=5
        )

        activities = ["User login - 2 min ago",
                     "New post - 15 min ago",
                     "System update - 1 hour ago"]
        for i, activity in enumerate(activities):
            ttk.Label(bottom_left, text=activity).grid(
                row=i, column=0, pady=5, padx=5, sticky="w"
            )

        # 6. Panel inferior derecho
        bottom_right = ttk.LabelFrame(self.root, text="Quick Actions")
        bottom_right.grid(
            row=3, column=2, columnspan=2, rowspan=2,
            sticky="nsew", padx=5, pady=5
        )

        actions = [("New Post", 0, 0), ("Send Message", 0, 1),
                  ("Generate Report", 1, 0), ("Update Profile", 1, 1)]
        for text, row, col in actions:
            ttk.Button(bottom_right, text=text).grid(
                row=row, column=col, pady=5, padx=5, sticky="nsew"
            )

        # 7. Barra de estado - Span completo en la parte inferior
        status_bar = ttk.Label(
            self.root,
            text="Status: Connected | Last updated: 2 minutes ago",
            relief="sunken"
        )
        status_bar.grid(
            row=5, column=0, columnspan=4, sticky="ew",
            padx=5, pady=5
        )

def main():
    root = tk.Tk()
    app = DashboardExample(root)
    root.mainloop()

if __name__ == "__main__":
    main()
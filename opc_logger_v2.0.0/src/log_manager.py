import csv
from datetime import datetime

class LogManager:
    def __init__(self, event_bus):
        # Lista para almacenar los registros de datos
        self.logs = []
        # Lista dinámica de columnas (se detectan automáticamente)
        self.columns = set(['date', 'time'])  # Siempre incluirá 'date' y 'time'
        self.event_bus = event_bus

        # subscription to events
        self.event_bus.subscribe('NewReading', self.add_log)
        self.event_bus.subscribe('PrintLog', self.print_log)
        self.event_bus.subscribe('ExportCsv',self.export_to_csv,'nombre_archivo')

    def add_log(self, data):
        """
        Procesa y agrega un nuevo registro al log.
        Detecta automáticamente las variables en los datos recibidos.
        :param data: Diccionario con los datos recibidos del servidor.
        """
        # Procesar el timestamp para separar fecha y hora
        if 'timestamp' not in data:
            raise ValueError("El dato recibido no contiene un campo 'timestamp'.")

        timestamp = datetime.fromisoformat(data['timestamp'])
        date = timestamp.strftime('%Y-%m-%d')
        time = timestamp.strftime('%H:%M:%S')

        # Crear un registro formateado
        log_entry = {'date': date, 'time': time}

        # Agregar las demás variables dinámicamente
        for key, value in data.items():
            if key != 'timestamp':  # Excluir el timestamp del registro
                log_entry[key] = value
                self.columns.add(key)  # Agregar la columna a la lista dinámica

        # Agregar el registro a la lista de logs
        self.logs.append(log_entry)
        self.event_bus.publish('UpdateLog', self.logs)

    def export_to_csv(self, file_name):
        """
        Exporta los logs almacenados a un archivo CSV.
        :param file_name: Nombre del archivo CSV.
        """
        # Asegurarse de que las columnas estén ordenadas
        fieldnames = ['date', 'time'] + sorted(self.columns - {'date', 'time'})

        # Escribir los datos en el archivo CSV
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Escribir los encabezados
            writer.writerows(self.logs)  # Escribir los registros

        print(f"Logs exportados a {file_name} con éxito.")

    def print_log(self):
        """
        Imprime el log actual en formato tabular.
        """
        if not self.logs:
            print("El log está vacío.")
            return

        # Obtener las columnas ordenadas
        fieldnames = ['date', 'time'] + sorted(self.columns - {'date', 'time'})

        # Imprimir encabezados
        print(" | ".join(fieldnames))
        print("-" * (len(fieldnames) * 15))  # Línea separadora

        # Imprimir cada registro
        for log in self.logs:
            row = [str(log.get(col, "")) for col in fieldnames]
            print(" | ".join(row))
    
    def clear_log(self):
        """
        Limpia todo el log actual, eliminando todos los registros almacenados.
        """
        self.logs = []  # Vaciar la lista de registros
        self.columns = set(['date', 'time'])  # Restablecer las columnas dinámicas
        print("El log ha sido limpiado.")
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QTabWidget, QLabel, QTableWidget, QTableWidgetItem
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hotel Paraíso Resort")
        self.resize(900, 800)  # Tamaño de ventana (puedes ajustarlo)

        # Contenedor principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Menú lateral
        self.side_menu = QWidget()
        side_layout = QVBoxLayout(self.side_menu)

        self.btn_entradas = QPushButton("ENTRADAS")
        self.btn_salidas = QPushButton("SALIDAS")
        self.btn_estado_hotel = QPushButton("ESTADO DEL HOTEL")

        side_layout.addWidget(self.btn_entradas)
        side_layout.addWidget(self.btn_salidas)
        side_layout.addWidget(self.btn_estado_hotel)

        side_layout.addStretch()  # Espacio flexible para empujar botones de abajo

        self.btn_modificar = QPushButton("MODIFICAR")
        self.btn_salir = QPushButton("SALIR")
        side_layout.addWidget(self.btn_modificar)
        side_layout.addWidget(self.btn_salir)

        # Pestañas superiores
        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(self.create_hotel_state_tab(), "ESTADO DEL HOTEL")
        self.tab_widget.addTab(self.create_daily_report_tab(), "REPORTE DIARIO")
        self.tab_widget.addTab(self.create_room_state_tab(), "ESTADO DE HABITACIÓN")

        # Se agregan el menú lateral y el QTabWidget al layout principal
        main_layout.addWidget(self.side_menu, 1)
        main_layout.addWidget(self.tab_widget, 4)

    def create_hotel_state_tab(self):
        """
        Pestaña: 'ESTADO DEL HOTEL'
        Puedes personalizarla según tus necesidades.
        """
        widget = QWidget()
        layout = QVBoxLayout(widget)

        layout.addWidget(QLabel("Aquí irá la información del estado general del hotel."))

        return widget

    def create_daily_report_tab(self):
        """
        Pestaña: 'REPORTE DIARIO'
        Contiene dos tablas: Entradas del día y Salidas del día.
        """
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Etiqueta y tabla de Entradas
        layout.addWidget(QLabel("Entradas del día"))
        self.entradas_table = QTableWidget()
        self.entradas_table.setColumnCount(4)
        self.entradas_table.setHorizontalHeaderLabels(["N° Habitación", "Tipo Habitación", "Costo", "Fecha de Entrega"])
        # Ejemplo de fila
        self.entradas_table.insertRow(0)
        self.entradas_table.setItem(0, 0, QTableWidgetItem("1"))
        self.entradas_table.setItem(0, 1, QTableWidgetItem("Suite"))
        self.entradas_table.setItem(0, 2, QTableWidgetItem("$1200"))
        self.entradas_table.setItem(0, 3, QTableWidgetItem("2025-03-11"))
        layout.addWidget(self.entradas_table)

        # Etiqueta y tabla de Salidas
        layout.addWidget(QLabel("Salidas del día"))
        self.salidas_table = QTableWidget()
        self.salidas_table.setColumnCount(4)
        self.salidas_table.setHorizontalHeaderLabels(["N° Habitación", "Tipo Habitación", "Costo", "Fecha de Salida"])
        # Ejemplo de fila
        self.salidas_table.insertRow(0)
        self.salidas_table.setItem(0, 0, QTableWidgetItem("2"))
        self.salidas_table.setItem(0, 1, QTableWidgetItem("Estándar"))
        self.salidas_table.setItem(0, 2, QTableWidgetItem("$800"))
        self.salidas_table.setItem(0, 3, QTableWidgetItem("2025-03-11"))
        layout.addWidget(self.salidas_table)

        return widget

    def create_room_state_tab(self):
        """
        Pestaña: 'ESTADO DE HABITACIÓN'
        Muestra la tabla con la limpieza, costo, salida, etc.
        """
        widget = QWidget()
        layout = QVBoxLayout(widget)

        layout.addWidget(QLabel("Reporte del estado de habitación"))

        self.room_state_table = QTableWidget()
        self.room_state_table.setColumnCount(5)
        self.room_state_table.setHorizontalHeaderLabels([
            "N° Habitación", "Limpieza", "H. Costo", "H. Salida", "H. Vacíos"
        ])

        # Ejemplo de varias filas
        for i in range(6):
            self.room_state_table.insertRow(i)
            self.room_state_table.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.room_state_table.setItem(i, 1, QTableWidgetItem("Pendiente" if i % 2 == 0 else "Listo"))
            self.room_state_table.setItem(i, 2, QTableWidgetItem("1200" if i == 0 else "800"))
            self.room_state_table.setItem(i, 3, QTableWidgetItem("2025-03-11"))
            self.room_state_table.setItem(i, 4, QTableWidgetItem("OK"))

        layout.addWidget(self.room_state_table)
        return widget


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    # (Opcional) Puedes agregar estilos con Qt Style Sheets (QSS) si quieres.
    # style = """
    # QMainWindow {
    #     background-color: #f0f0f0;
    # }
    # """
    # app.setStyleSheet(style)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

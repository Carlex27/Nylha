from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Entradas(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1382, 810)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(2, 0, 0, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setStyleSheet("background-color: white;")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 500))
        self.widget_4.setStyleSheet("background-color: rgb(178, 210, 201);")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_habita_dispo = QtWidgets.QWidget(self.widget_4)
        self.btn_habita_dispo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_habita_dispo.setStyleSheet("QWidget{\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QWidget#btn_habita_dispo:hover{\n"
"border:3px solid Black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.btn_habita_dispo.setObjectName("btn_habita_dispo")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.btn_habita_dispo)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.btn_habita_dispo)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.btn_habita_dispo)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Images/camita_icon.png"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_3.addWidget(self.btn_habita_dispo)
        self.btn_registro = QtWidgets.QWidget(self.widget_4)
        self.btn_registro.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_registro.setStyleSheet("QWidget{\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QWidget#btn_registro:hover{\n"
"border:3px solid Black;\n"
"}")
        self.btn_registro.setObjectName("btn_registro")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.btn_registro)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.btn_registro)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.btn_registro)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Images/registro_icon.png"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_3.addWidget(self.btn_registro)
        self.btn_historial_registro = QtWidgets.QWidget(self.widget_4)
        self.btn_historial_registro.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_historial_registro.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_historial_registro.setStyleSheet("QWidget{\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QWidget#btn_historial_registro:hover{\n"
"border:3px solid Black;\n"
"}")
        self.btn_historial_registro.setObjectName("btn_historial_registro")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.btn_historial_registro)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.btn_historial_registro)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.btn_historial_registro)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("Images/historial_icon.png"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.horizontalLayout_3.addWidget(self.btn_historial_registro)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setContentsMargins(4, 0, 0, 11)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.widget_5)
        self.label_8.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:3px solid black;\n"
"border-right-color:0px rgb(255, 255, 255);\n"
"border-left-color: 0px rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_5)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Pagina_habit = QtWidgets.QWidget()
        self.Pagina_habit.setObjectName("Pagina_habit")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Pagina_habit)
        self.verticalLayout_7.setContentsMargins(25, 20, 25, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabla_habitaciones_disponi = QtWidgets.QTableWidget(self.Pagina_habit)
        self.tabla_habitaciones_disponi.setStyleSheet("font: 10pt \"Roboto\";\n"
"")
        self.tabla_habitaciones_disponi.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tabla_habitaciones_disponi.setLineWidth(1)
        self.tabla_habitaciones_disponi.setAutoScroll(True)
        self.tabla_habitaciones_disponi.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_habitaciones_disponi.setTabKeyNavigation(True)
        self.tabla_habitaciones_disponi.setProperty("showDropIndicator", True)
        self.tabla_habitaciones_disponi.setDragEnabled(False)
        self.tabla_habitaciones_disponi.setDragDropOverwriteMode(True)
        self.tabla_habitaciones_disponi.setShowGrid(True)
        self.tabla_habitaciones_disponi.setWordWrap(True)
        self.tabla_habitaciones_disponi.setCornerButtonEnabled(True)
        self.tabla_habitaciones_disponi.setRowCount(100)
        self.tabla_habitaciones_disponi.setObjectName("tabla_habitaciones_disponi")
        self.tabla_habitaciones_disponi.setColumnCount(3)
        self.tabla_habitaciones_disponi.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_habitaciones_disponi.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_habitaciones_disponi.setHorizontalHeaderItem(1, item)
        
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_habitaciones_disponi.setHorizontalHeaderItem(2, item)

        self.tabla_habitaciones_disponi.horizontalHeader().setStretchLastSection(True)
        self.tabla_habitaciones_disponi.verticalHeader().setVisible(False)
        self.verticalLayout_7.addWidget(self.tabla_habitaciones_disponi)
        self.stackedWidget.addWidget(self.Pagina_habit)
        self.page_registro_0 = QtWidgets.QWidget()
        self.page_registro_0.setStyleSheet("")
        self.page_registro_0.setObjectName("page_registro_0")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_registro_0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_10 = QtWidgets.QWidget(self.page_registro_0)
        self.widget_10.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_11 = QtWidgets.QWidget(self.widget_10)
        self.widget_11.setStyleSheet("QWidget{\n"
"    border:3px solid black;\n"
"    \n"
"    background-color: rgb(160, 255, 184);\n"
"}\n"
"\n"
"QWidget#widget_11{\n"
"    border:0px;    \n"
"    background-color: white;\n"
"}\n"
"\n"
"QLabel{\n"
"    border:0px\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border:0px;\n"
"}\n"
"\n"
"spinBox{\n"
"    border:0px;\n"
"}")
        self.widget_11.setObjectName("widget_11")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_11)
        self.gridLayout_2.setContentsMargins(20, 33, 20, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_13 = QtWidgets.QWidget(self.widget_11)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.widget_13)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 9pt \"Verdana\";")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_10.addWidget(self.label_9)
        self.nombre = QtWidgets.QLineEdit(self.widget_13)
        self.nombre.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.nombre.setFont(font)
        self.nombre.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.nombre.setObjectName("nombre")
        self.verticalLayout_10.addWidget(self.nombre)
        self.gridLayout_2.addWidget(self.widget_13, 0, 0, 1, 1)
        self.widget_15 = QtWidgets.QWidget(self.widget_11)
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.widget_15)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font: 9pt \"Verdana\";")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_12.addWidget(self.label_11)
        self.no_ninios = QtWidgets.QSpinBox(self.widget_15)
        self.no_ninios.setMinimumSize(QtCore.QSize(0, 40))
        self.no_ninios.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid black;\n"
"border-radius: 10px;\n"
"\n"
"font: 9pt \"Verdana\";\n"
"\n"
"")
        self.no_ninios.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.no_ninios.setObjectName("no_ninios")
        self.verticalLayout_12.addWidget(self.no_ninios)
        self.gridLayout_2.addWidget(self.widget_15, 0, 2, 1, 1)
        self.widget_19 = QtWidgets.QWidget(self.widget_11)
        self.widget_19.setStyleSheet("border-top-color: 0px rgb(255, 255, 255);\n"
"border-left-color: 0px rgb(255, 255, 255);\n"
"border-right-color: 0px rgb(255, 255, 255);")
        self.widget_19.setObjectName("widget_19")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.widget_19)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_16 = QtWidgets.QLabel(self.widget_19)
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("font: 9pt \"Verdana\";")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_17.addWidget(self.label_16)
        self.telefono = QtWidgets.QLineEdit(self.widget_19)
        self.telefono.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.telefono.setFont(font)
        self.telefono.setStyleSheet("QLineEdit{\n"
"    font: 9pt \"Verdana\";\n"
"    background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}")
        self.telefono.setText("")
        self.telefono.setObjectName("telefono")
        self.verticalLayout_17.addWidget(self.telefono)
        self.gridLayout_2.addWidget(self.widget_19, 1, 1, 1, 1)
        self.widget_20 = QtWidgets.QWidget(self.widget_11)
        self.widget_20.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_20.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_20.setStyleSheet("border-top-color: 0px rgb(255, 255, 255);\n"
"")
        self.widget_20.setObjectName("widget_20")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget_20)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_15 = QtWidgets.QLabel(self.widget_20)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("font: 9pt \"Verdana\";")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_16.addWidget(self.label_15)
        self.email = QtWidgets.QLineEdit(self.widget_20)
        self.email.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.email.setFont(font)
        self.email.setStyleSheet("QLineEdit{\n"
"    font: 9pt \"Verdana\";\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid black;\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.email.setObjectName("email")
        self.verticalLayout_16.addWidget(self.email)
        self.gridLayout_2.addWidget(self.widget_20, 1, 0, 1, 1)
        self.widget_14 = QtWidgets.QWidget(self.widget_11)
        self.widget_14.setStyleSheet("border-right-color:0px rgb(255, 255, 255);\n"
"border-left-color:0px rgb(255, 255, 255);")
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.widget_14)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 9pt \"Verdana\";")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_11.addWidget(self.label_10)
        self.no_adultos = QtWidgets.QSpinBox(self.widget_14)
        self.no_adultos.setMinimumSize(QtCore.QSize(0, 40))
        self.no_adultos.setStyleSheet("border:1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"font: 9pt \"Verdana\";")
        self.no_adultos.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.no_adultos.setObjectName("no_adultos")
        self.verticalLayout_11.addWidget(self.no_adultos)
        self.gridLayout_2.addWidget(self.widget_14, 0, 1, 1, 1)
        self.widget_21 = QtWidgets.QWidget(self.widget_11)
        self.widget_21.setStyleSheet("border-top-color: 0px rgb(255, 255, 255);\n"
"")
        self.widget_21.setObjectName("widget_21")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.widget_21)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_17 = QtWidgets.QLabel(self.widget_21)
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 9pt \"Verdana\";")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_18.addWidget(self.label_17)
        self.no_matricula = QtWidgets.QLineEdit(self.widget_21)
        self.no_matricula.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.no_matricula.setFont(font)
        self.no_matricula.setStyleSheet("QLineEdit{\n"
"    font: 9pt \"Verdana\";\n"
"    background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.no_matricula.setText("")
        self.no_matricula.setObjectName("no_matricula")
        self.verticalLayout_18.addWidget(self.no_matricula)
        self.gridLayout_2.addWidget(self.widget_21, 1, 2, 1, 1)
        self.verticalLayout_9.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget_10)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_19.setContentsMargins(0, 25, 20, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.siguiente_btn = QtWidgets.QPushButton(self.widget_12)
        self.siguiente_btn.setMinimumSize(QtCore.QSize(250, 50))
        self.siguiente_btn.setStyleSheet("background-color: rgb(29, 124, 23);\n"
"font: 87 11pt \"Roboto Black\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"")
        self.siguiente_btn.setObjectName("siguiente_btn")
        self.verticalLayout_19.addWidget(self.siguiente_btn)
        self.verticalLayout_9.addWidget(self.widget_12, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout_8.addWidget(self.widget_10)
        self.stackedWidget.addWidget(self.page_registro_0)
        self.page_registro_1 = QtWidgets.QWidget()
        self.page_registro_1.setObjectName("page_registro_1")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_registro_1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.widget_16 = QtWidgets.QWidget(self.page_registro_1)
        self.widget_16.setStyleSheet("QWidget{\n"
"    border:3px solid black;\n"
"    background-color: rgb(160, 255, 184);\n"
"}\n"
"\n"
"QWidget#widget_16{\n"
"    border:0px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"")
        self.widget_16.setObjectName("widget_16")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_16)
        self.gridLayout_3.setContentsMargins(20, 33, 20, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_18 = QtWidgets.QWidget(self.widget_16)
        self.widget_18.setStyleSheet("QWidget{\n"
"border-right-color: 0px rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"border:0px;\n"
"}")
        self.widget_18.setObjectName("widget_18")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.widget_18)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_19 = QtWidgets.QLabel(self.widget_18)
        self.label_19.setStyleSheet("font: 9pt \"Verdana\";")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_21.addWidget(self.label_19)
        self.gridLayout_3.addWidget(self.widget_18, 0, 0, 1, 2)
        self.widget_22 = QtWidgets.QWidget(self.widget_16)
        self.widget_22.setStyleSheet("QWidget{\n"
"border-right-color: 0px rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"border:0px;\n"
"}")
        self.widget_22.setObjectName("widget_22")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.widget_22)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_20 = QtWidgets.QLabel(self.widget_22)
        self.label_20.setStyleSheet("font: 9pt \"Verdana\";")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_23.addWidget(self.label_20)
        self.gridLayout_3.addWidget(self.widget_22, 0, 2, 1, 2)
        self.widget_23 = QtWidgets.QWidget(self.widget_16)
        self.widget_23.setStyleSheet("QLabel{\n"
"    border:0px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"    border:0px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.widget_23.setObjectName("widget_23")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.widget_23)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_21 = QtWidgets.QLabel(self.widget_23)
        self.label_21.setStyleSheet("font: 9pt \"Verdana\";")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_22.addWidget(self.label_21)
        self.no_habitacion = QtWidgets.QSpinBox(self.widget_23)
        self.no_habitacion.setMinimumSize(QtCore.QSize(0, 35))
        self.no_habitacion.setStyleSheet("font: 9pt \"Verdana\";\n"
"border:1px solid gray;")
        self.no_habitacion.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.no_habitacion.setObjectName("no_habitacion")
        self.verticalLayout_22.addWidget(self.no_habitacion)
        self.gridLayout_3.addWidget(self.widget_23, 0, 4, 1, 2)
        self.widget_24 = QtWidgets.QWidget(self.widget_16)
        self.widget_24.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_24.setStyleSheet("QWidget{\n"
"    border-right-color: 0px rgb(255, 255, 255);\n"
"    border-top-color:0px rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"    Border:0px;\n"
"}\n"
"\n"
"QDateEdit{\n"
"    border:0px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.widget_24.setObjectName("widget_24")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_24)
        self.verticalLayout_14.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_12 = QtWidgets.QLabel(self.widget_24)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_14.addWidget(self.label_12, 0, QtCore.Qt.AlignTop)
        self.fecha_entrada = QtWidgets.QDateEdit(self.widget_24)
        self.fecha_entrada.setMinimumSize(QtCore.QSize(0, 65))
        self.fecha_entrada.setStyleSheet("font: 10pt \"Verdana\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid gray;")
        self.fecha_entrada.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.fecha_entrada.setAccelerated(False)
        self.fecha_entrada.setObjectName("fecha_entrada")
        self.verticalLayout_14.addWidget(self.fecha_entrada, 0, QtCore.Qt.AlignTop)
        self.gridLayout_3.addWidget(self.widget_24, 1, 0, 1, 1)
        self.widget_25 = QtWidgets.QWidget(self.widget_16)
        self.widget_25.setStyleSheet("QWidget{\n"
"border-right-color: 0px rgb(255, 255, 255);\n"
"border-top-color:0px rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"    border: 0px;\n"
"}\n"
"\n"
"QDateEdit{\n"
"    border:0px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"\n"
"")
        self.widget_25.setObjectName("widget_25")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget_25)
        self.verticalLayout_15.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_13 = QtWidgets.QLabel(self.widget_25)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_15.addWidget(self.label_13, 0, QtCore.Qt.AlignTop)
        self.fecha_salida = QtWidgets.QDateEdit(self.widget_25)
        self.fecha_salida.setMinimumSize(QtCore.QSize(0, 65))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.fecha_salida.setFont(font)
        self.fecha_salida.setStyleSheet("border:1px solid gray;")
        self.fecha_salida.setFrame(True)
        self.fecha_salida.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.fecha_salida.setObjectName("fecha_salida")
        self.verticalLayout_15.addWidget(self.fecha_salida, 0, QtCore.Qt.AlignTop)
        self.gridLayout_3.addWidget(self.widget_25, 1, 1, 1, 2)
        self.widget_26 = QtWidgets.QWidget(self.widget_16)
        self.widget_26.setStyleSheet("QWidget{\n"
"border-right-color: 0px rgb(255, 255, 255);\n"
"border-top-color:0px rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"border: 0px;\n"
"}\n"
"\n"
"\n"
"")
        self.widget_26.setObjectName("widget_26")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.widget_26)
        self.verticalLayout_20.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_14 = QtWidgets.QLabel(self.widget_26)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_20.addWidget(self.label_14, 0, QtCore.Qt.AlignTop)
        self.cant_noches = QtWidgets.QSpinBox(self.widget_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cant_noches.sizePolicy().hasHeightForWidth())
        self.cant_noches.setSizePolicy(sizePolicy)
        self.cant_noches.setMinimumSize(QtCore.QSize(0, 65))
        self.cant_noches.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Verdana\";\n"
"border:1px solid gray;\n"
"")
        self.cant_noches.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.cant_noches.setObjectName("cant_noches")
        self.verticalLayout_20.addWidget(self.cant_noches, 0, QtCore.Qt.AlignTop)
        self.gridLayout_3.addWidget(self.widget_26, 1, 3, 1, 2)
        self.widget_27 = QtWidgets.QWidget(self.widget_16)
        self.widget_27.setStyleSheet("QWidget{\n"
"border-top-color:0px rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"border:0px solid white;\n"
"}\n"
"\n"
"QTextEdit{\n"
"border:1px solid gray;\n"
"}\n"
"\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.widget_27.setObjectName("widget_27")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.widget_27)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_18 = QtWidgets.QLabel(self.widget_27)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_24.addWidget(self.label_18, 0, QtCore.Qt.AlignTop)
        self.observaciones = QtWidgets.QTextEdit(self.widget_27)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.observaciones.sizePolicy().hasHeightForWidth())
        self.observaciones.setSizePolicy(sizePolicy)
        self.observaciones.setMinimumSize(QtCore.QSize(0, 0))
        self.observaciones.setMaximumSize(QtCore.QSize(16777215, 16777204))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.observaciones.setFont(font)
        self.observaciones.setStyleSheet("font: 9pt \"Verdana\";")
        self.observaciones.setObjectName("observaciones")
        self.verticalLayout_24.addWidget(self.observaciones)
        self.gridLayout_3.addWidget(self.widget_27, 1, 5, 1, 1)
        self.verticalLayout_13.addWidget(self.widget_16)
        self.widget_17 = QtWidgets.QWidget(self.page_registro_1)
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout_4.setContentsMargins(0, 20, 25, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton_3.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(29, 124, 23);\n"
"font: 87 11pt \"Roboto Black\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_13.addWidget(self.widget_17, 0, QtCore.Qt.AlignTop)
        self.stackedWidget.addWidget(self.page_registro_1)
        self.page_historial = QtWidgets.QWidget()
        self.page_historial.setObjectName("page_historial")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.page_historial)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.widget_29 = QtWidgets.QWidget(self.page_historial)
        self.widget_29.setObjectName("widget_29")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.widget_29)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.widget_28 = QtWidgets.QWidget(self.widget_29)
        self.widget_28.setObjectName("widget_28")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_28)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
    
        ###############################################################
        self.btn_fecha_inicial = QtWidgets.QPushButton("Fecha Inicial", self.widget_28)
        self.btn_fecha_inicial.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_fecha_inicial.setStyleSheet("font: 10pt \"Verdana\";")
        
        self.btn_fecha_final = QtWidgets.QPushButton("Fecha Final", self.widget_28)
        self.btn_fecha_final.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_fecha_final.setStyleSheet("font: 10pt \"Verdana\";")
        
        self.horizontalLayout_5.addWidget(self.btn_fecha_inicial)
        self.horizontalLayout_5.addWidget(self.btn_fecha_final)
         # Conectamos los botones a métodos que abrirán un calendario en un QDialog
        self.btn_fecha_inicial.clicked.connect(self.seleccionarFechaInicial)
        self.btn_fecha_final.clicked.connect(self.seleccionarFechaFinal)

        self.btn_limpiar = QtWidgets.QPushButton("Limpiar Fechas", self.widget_28)
        self.btn_limpiar.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_limpiar.setStyleSheet("font: 10pt \"Verdana\";")
        self.horizontalLayout_5.addWidget(self.btn_limpiar)

        self.btn_limpiar.clicked.connect(self.limpiarFechas)

        self.verticalLayout_26.addWidget(self.widget_28)
        self.tabla_historial_registro = QtWidgets.QTableWidget(self.widget_29)

        self.tabla_historial_registro.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_historial_registro.setStyleSheet("font: 10pt \"Roboto\";\n"
"background-color: rgb(250, 255, 237);\n"
"border:1px solid black;")
        self.tabla_historial_registro.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tabla_historial_registro.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tabla_historial_registro.setRowCount(50)
        self.tabla_historial_registro.setObjectName("tabla_historial_registro")
        self.tabla_historial_registro.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_historial_registro.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_historial_registro.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_historial_registro.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_historial_registro.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_historial_registro.setHorizontalHeaderItem(4, item)
        self.tabla_historial_registro.horizontalHeader().setDefaultSectionSize(125)
        self.tabla_historial_registro.horizontalHeader().setStretchLastSection(True)
        self.tabla_historial_registro.verticalHeader().setVisible(False)
        self.tabla_historial_registro.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tabla_historial_registro.verticalHeader().setVisible(False)
        self.verticalLayout_26.addWidget(self.tabla_historial_registro)
        self.verticalLayout_25.addWidget(self.widget_29)
        self.stackedWidget.addWidget(self.page_historial)
        self.verticalLayout_6.addWidget(self.stackedWidget)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.horizontalLayout.addWidget(self.widget_3)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.btn_habita_dispo.mousePressEvent = self.mousePressedHD
        self.btn_registro.mousePressEvent = self.mousePressedRg
        self.btn_historial_registro.mousePressEvent = self.mousePressedHR
        self.siguiente_btn.mousePressEvent = self.mousePressedRG_Sig

        self.label_2.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.label_3.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.label_4.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.label_5.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.label_6.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.label_7.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        self.retranslateUi()
        self.stackedWidget.setCurrentIndex(0)
    def limpiarFechas(self):
        self.btn_fecha_inicial.setText("Fecha Inicial")
        self.btn_fecha_final.setText("Fecha Final")

    def seleccionarFechaInicial(self):
        #Muestra un diálogo con un QCalendarWidget para la fecha inicial."""
                dialog = QtWidgets.QDialog(self)
                dialog.setWindowTitle("Seleccionar fecha inicial")
                
                layout = QtWidgets.QVBoxLayout(dialog)
                
                calendar = QtWidgets.QCalendarWidget(dialog)
                calendar.setGridVisible(True)  # Opcional: muestra líneas de cuadrícula
                layout.addWidget(calendar)
                
                btn_aceptar = QtWidgets.QPushButton("Aceptar", dialog)
                layout.addWidget(btn_aceptar)
                
                # Cuando presione "Aceptar", manejamos la fecha y cerramos el diálogo
                btn_aceptar.clicked.connect(lambda: self._handleFechaInicial(calendar.selectedDate(), dialog))
                
                dialog.exec_()  # Abre el diálogo de forma modal
        
    def _handleFechaInicial(self, fecha_seleccionada, dialog):
        """Recoge la fecha del calendario y la muestra en el botón."""
        fecha_str = fecha_seleccionada.toString("dd/MM/yyyy")
        self.btn_fecha_inicial.setText(fecha_str)
        # Podrías guardar la fecha en una variable si quieres usarla luego:
        # self.fecha_inicial = fecha_seleccionada
        dialog.accept()
    
    def seleccionarFechaFinal(self):
        """Muestra un diálogo con un QCalendarWidget para la fecha final."""
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Seleccionar fecha final")
        
        layout = QtWidgets.QVBoxLayout(dialog)
        
        calendar = QtWidgets.QCalendarWidget(dialog)
        calendar.setGridVisible(True)
        layout.addWidget(calendar)
        
        btn_aceptar = QtWidgets.QPushButton("Aceptar", dialog)
        layout.addWidget(btn_aceptar)
        
        btn_aceptar.clicked.connect(lambda: self._handleFechaFinal(calendar.selectedDate(), dialog))
        
        dialog.exec_()
    
    def _handleFechaFinal(self, fecha_seleccionada, dialog):
        """Recoge la fecha y la muestra en el botón."""
        fecha_str = fecha_seleccionada.toString("dd/MM/yyyy")
        self.btn_fecha_final.setText(fecha_str)
        # self.fecha_final = fecha_seleccionada
        dialog.accept()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText("HABITACIONES DISPONIBLES")
        self.label_3.setText("REGISTRO")
        self.label_4.setText("HISTORIAL DE REGISTRO")
        self.label_8.setText("<html><head/><body><p>HABITACIONES DISPONIBLES</p></body></html>")
        item = self.tabla_habitaciones_disponi.horizontalHeaderItem(0)
        item.setText("No. Habitación")
        item = self.tabla_habitaciones_disponi.horizontalHeaderItem(1)
        item.setText("Tipo de habitación")
        item = self.tabla_habitaciones_disponi.horizontalHeaderItem(2)
        item.setText("Costo")
        self.label_9.setText("Nombre[Name]:")
        self.label_11.setText("No. De niños[Children]:")
        self.label_16.setText("Teléfono[Phone]:")
        self.label_15.setText("Correo electrónico[Email]:")
        self.label_10.setText("No. Adultos[Adult]:")
        self.label_17.setText("No. Matricula del carro[Car license plates]:")
        self.siguiente_btn.setText("SIGUIENTE")
        self.label_19.setText("Dirección[Adress]:Paseo del Riscal S/N. Colonia<br>Vicente Guerrero, Zihuatanejo de Azueta")
        self.label_20.setText("Nombre del hotel[Hotel<br> name]: Hotel Posada el Riscal")
        self.label_21.setText("No. Habitación[room number]:")
        self.label_12.setText("Fecha de entrada[Check in date]:")
        self.label_13.setText("Fecha de salida[Check out date]:")
        self.label_14.setText("Cantidad de noche:")
        self.label_18.setText("Observaciones:")
        self.pushButton_3.setText("FINALIZAR REGISTRO")
        item = self.tabla_historial_registro.horizontalHeaderItem(0)
        item.setText("No. Habitación")
        item = self.tabla_historial_registro.horizontalHeaderItem(1)
        item.setText("Nombre")
        item = self.tabla_historial_registro.horizontalHeaderItem(2)
        item.setText("Tipo de habitación")
        item = self.tabla_historial_registro.horizontalHeaderItem(3)
        item.setText("Costo")
        item = self.tabla_historial_registro.horizontalHeaderItem(4)
        item.setText("Fecha de entrada")


    def mousePressedHD(self, event):
        self.stackedWidget.setCurrentIndex(0)
        self.label_8.setText("HABITACIONES DISPONIBLES")

    def mousePressedRg(self, event):
        self.stackedWidget.setCurrentIndex(1)
        self.label_8.setText("REGISTRO")

    def mousePressedRG_Sig(self, event):
        self.stackedWidget.setCurrentIndex(2)

    def mousePressedHR(self, event):
        self.stackedWidget.setCurrentIndex(3)
        self.label_8.setText("HISTORIAL DE REGISTRO")   



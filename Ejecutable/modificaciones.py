from PyQt5 import QtCore, QtGui, QtWidgets

class modificaciones(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1026, 749)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(self)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 500))
        self.widget_4.setStyleSheet("background-color: rgb(230, 230, 250);")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btn_elimn = QtWidgets.QWidget(self.widget_4)
        self.btn_elimn.setMinimumSize(QtCore.QSize(210, 160))
        self.btn_elimn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_elimn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"background-color: #d3d3d3;")
        self.btn_elimn.setObjectName("btn_elimn")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.btn_elimn)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.btn_elimn)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.btn_elimn)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Images/eliminar.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_3.addWidget(self.btn_elimn)
        self.btn_modif = QtWidgets.QWidget(self.widget_4)
        self.btn_modif.setMinimumSize(QtCore.QSize(210, 160))
        self.btn_modif.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_modif.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"background-color: #d3d3d3;")
        self.btn_modif.setObjectName("btn_modif")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.btn_modif)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.btn_modif)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.btn_modif)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/editar.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_3.addWidget(self.btn_modif)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget_4)
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:3px solid black;\n"
"border-right-color:0px rgb(255, 255, 255);\n"
"border-left-color: 0px rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Hab_ocu_pag = QtWidgets.QWidget()
        self.Hab_ocu_pag.setStyleSheet("")
        self.Hab_ocu_pag.setObjectName("Hab_ocu_pag")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Hab_ocu_pag)
        self.verticalLayout_8.setContentsMargins(0, 20, 0, 0)
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_3 = QtWidgets.QWidget(self.Hab_ocu_pag)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setContentsMargins(30, -1, 30, -1)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_10 = QtWidgets.QWidget(self.widget_3)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.widget_10)
        self.label_9.setMinimumSize(QtCore.QSize(40, 40))
        self.label_9.setStyleSheet("border-bottom:1px solid black;")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../Images/lupa_2.png"))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.linetext_buscar_modifi = QtWidgets.QLineEdit(self.widget_10)
        self.linetext_buscar_modifi.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.linetext_buscar_modifi.setFont(font)
        self.linetext_buscar_modifi.setStyleSheet("border-top:0px;\n"
"border-bottom:1px solid black;")
        self.linetext_buscar_modifi.setObjectName("linetext_buscar_modifi")
        self.horizontalLayout_4.addWidget(self.linetext_buscar_modifi)
        self.verticalLayout_6.addWidget(self.widget_10)
        self.tabla_resv_mod = QtWidgets.QTableWidget(self.widget_3)
        self.tabla_resv_mod.setStyleSheet("font: 10pt \"Roboto\";\n"
"background-color: rgb(250, 255, 237);\n"
"border:1px solid black;")
        self.tabla_resv_mod.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_resv_mod.setRowCount(50)
        self.tabla_resv_mod.setObjectName("tabla_resv_mod")
        self.tabla_resv_mod.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_resv_mod.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_resv_mod.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_resv_mod.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_resv_mod.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_resv_mod.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_resv_mod.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_resv_mod.setHorizontalHeaderItem(6, item)
        self.tabla_resv_mod.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_resv_mod.horizontalHeader().setDefaultSectionSize(135)
        self.tabla_resv_mod.horizontalHeader().setStretchLastSection(True)
        self.tabla_resv_mod.verticalHeader().setVisible(False)
        self.verticalLayout_6.addWidget(self.tabla_resv_mod)
        self.verticalLayout_8.addWidget(self.widget_3)
        self.stackedWidget.addWidget(self.Hab_ocu_pag)
        self.Salidas_pag = QtWidgets.QWidget()
        self.Salidas_pag.setObjectName("Salidas_pag")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Salidas_pag)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_11 = QtWidgets.QWidget(self.Salidas_pag)
        self.widget_11.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_9.setContentsMargins(20, 33, 20, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_12 = QtWidgets.QWidget(self.widget_11)
        self.widget_12.setStyleSheet("QWidget{\n"
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
        self.widget_12.setObjectName("widget_12")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_12)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_13 = QtWidgets.QWidget(self.widget_12)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.widget_13)
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
        self.verticalLayout_10.addWidget(self.label_10)
        self.Nombre_modifi = QtWidgets.QLineEdit(self.widget_13)
        self.Nombre_modifi.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.Nombre_modifi.setFont(font)
        self.Nombre_modifi.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.Nombre_modifi.setObjectName("Nombre_modifi")
        self.verticalLayout_10.addWidget(self.Nombre_modifi)
        self.gridLayout_2.addWidget(self.widget_13, 0, 0, 1, 1)
        self.widget_15 = QtWidgets.QWidget(self.widget_12)
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
        self.no_ninios_modifi = QtWidgets.QSpinBox(self.widget_15)
        self.no_ninios_modifi.setMinimumSize(QtCore.QSize(0, 40))
        self.no_ninios_modifi.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid black;\n"
"border-radius: 10px;\n"
"\n"
"font: 9pt \"Verdana\";\n"
"\n"
"")
        self.no_ninios_modifi.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.no_ninios_modifi.setObjectName("no_ninios_modifi")
        self.verticalLayout_12.addWidget(self.no_ninios_modifi)
        self.gridLayout_2.addWidget(self.widget_15, 0, 2, 1, 1)
        self.widget_19 = QtWidgets.QWidget(self.widget_12)
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
        self.Telefono_modific = QtWidgets.QLineEdit(self.widget_19)
        self.Telefono_modific.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Telefono_modific.setFont(font)
        self.Telefono_modific.setStyleSheet("QLineEdit{\n"
"    font: 9pt \"Verdana\";\n"
"    background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}")
        self.Telefono_modific.setText("")
        self.Telefono_modific.setObjectName("Telefono_modific")
        self.verticalLayout_17.addWidget(self.Telefono_modific)
        self.gridLayout_2.addWidget(self.widget_19, 1, 1, 1, 1)
        self.widget_20 = QtWidgets.QWidget(self.widget_12)
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
        self.email_modifi = QtWidgets.QLineEdit(self.widget_20)
        self.email_modifi.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.email_modifi.setFont(font)
        self.email_modifi.setStyleSheet("QLineEdit{\n"
"    font: 9pt \"Verdana\";\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid black;\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.email_modifi.setObjectName("email_modifi")
        self.verticalLayout_16.addWidget(self.email_modifi)
        self.gridLayout_2.addWidget(self.widget_20, 1, 0, 1, 1)
        self.widget_14 = QtWidgets.QWidget(self.widget_12)
        self.widget_14.setStyleSheet("border-right-color:0px rgb(255, 255, 255);\n"
"border-left-color:0px rgb(255, 255, 255);")
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.widget_14)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("font: 9pt \"Verdana\";")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_11.addWidget(self.label_12)
        self.no_adultos_modifi = QtWidgets.QSpinBox(self.widget_14)
        self.no_adultos_modifi.setMinimumSize(QtCore.QSize(0, 40))
        self.no_adultos_modifi.setStyleSheet("border:1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"font: 9pt \"Verdana\";")
        self.no_adultos_modifi.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.no_adultos_modifi.setObjectName("no_adultos_modifi")
        self.verticalLayout_11.addWidget(self.no_adultos_modifi)
        self.gridLayout_2.addWidget(self.widget_14, 0, 1, 1, 1)
        self.widget_21 = QtWidgets.QWidget(self.widget_12)
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
        self.matricula_carro_modifi = QtWidgets.QLineEdit(self.widget_21)
        self.matricula_carro_modifi.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.matricula_carro_modifi.setFont(font)
        self.matricula_carro_modifi.setStyleSheet("QLineEdit{\n"
"    font: 9pt \"Verdana\";\n"
"    background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.matricula_carro_modifi.setText("")
        self.matricula_carro_modifi.setObjectName("matricula_carro_modifi")
        self.verticalLayout_18.addWidget(self.matricula_carro_modifi)
        self.gridLayout_2.addWidget(self.widget_21, 1, 2, 1, 1)
        self.verticalLayout_9.addWidget(self.widget_12)
        self.widget_16 = QtWidgets.QWidget(self.widget_11)
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_19.setContentsMargins(0, 25, 20, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.siguiente_btn_mod = QtWidgets.QPushButton(self.widget_16)
        self.siguiente_btn_mod.setMinimumSize(QtCore.QSize(250, 50))
        self.siguiente_btn_mod.setStyleSheet("background-color: rgb(29, 124, 23);\n"
"font: 87 11pt \"Roboto Black\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"")
        self.siguiente_btn_mod.setObjectName("siguiente_btn_mod")
        self.verticalLayout_19.addWidget(self.siguiente_btn_mod)
        self.verticalLayout_9.addWidget(self.widget_16, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.widget_11)
        self.stackedWidget.addWidget(self.Salidas_pag)
        self.page_historial = QtWidgets.QWidget()
        self.page_historial.setObjectName("page_historial")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_historial)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_17 = QtWidgets.QWidget(self.page_historial)
        self.widget_17.setStyleSheet("QWidget{\n"
"    border:3px solid black;\n"
"    background-color: rgb(160, 255, 184);\n"
"}\n"
"\n"
"QWidget#widget_17{\n"
"    border:0px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"")
        self.widget_17.setObjectName("widget_17")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_17)
        self.gridLayout_3.setContentsMargins(20, 33, 20, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_18 = QtWidgets.QWidget(self.widget_17)
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
        self.widget_22 = QtWidgets.QWidget(self.widget_17)
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
        self.widget_23 = QtWidgets.QWidget(self.widget_17)
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
        self.no_habitacion_modif = QtWidgets.QSpinBox(self.widget_23)
        self.no_habitacion_modif.setMinimumSize(QtCore.QSize(0, 35))
        self.no_habitacion_modif.setStyleSheet("font: 9pt \"Verdana\";\n"
"border:1px solid gray;")
        self.no_habitacion_modif.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.no_habitacion_modif.setObjectName("no_habitacion_modif")
        self.verticalLayout_22.addWidget(self.no_habitacion_modif)
        self.gridLayout_3.addWidget(self.widget_23, 0, 4, 1, 2)
        self.widget_24 = QtWidgets.QWidget(self.widget_17)
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
        self.label_13 = QtWidgets.QLabel(self.widget_24)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_14.addWidget(self.label_13, 0, QtCore.Qt.AlignTop)
        self.Fecha_entrada_modifi = QtWidgets.QDateEdit(self.widget_24)
        self.Fecha_entrada_modifi.setMinimumSize(QtCore.QSize(0, 65))
        self.Fecha_entrada_modifi.setStyleSheet("font: 10pt \"Verdana\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid gray;")
        self.Fecha_entrada_modifi.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.Fecha_entrada_modifi.setAccelerated(False)
        self.Fecha_entrada_modifi.setObjectName("Fecha_entrada_modifi")
        self.verticalLayout_14.addWidget(self.Fecha_entrada_modifi, 0, QtCore.Qt.AlignTop)
        self.gridLayout_3.addWidget(self.widget_24, 1, 0, 1, 1)
        self.widget_25 = QtWidgets.QWidget(self.widget_17)
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
        self.label_14 = QtWidgets.QLabel(self.widget_25)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_15.addWidget(self.label_14, 0, QtCore.Qt.AlignTop)
        self.Fecha_salida_modifi = QtWidgets.QDateEdit(self.widget_25)
        self.Fecha_salida_modifi.setMinimumSize(QtCore.QSize(0, 65))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.Fecha_salida_modifi.setFont(font)
        self.Fecha_salida_modifi.setStyleSheet("border:1px solid gray;")
        self.Fecha_salida_modifi.setFrame(True)
        self.Fecha_salida_modifi.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.Fecha_salida_modifi.setObjectName("Fecha_salida_modifi")
        self.verticalLayout_15.addWidget(self.Fecha_salida_modifi, 0, QtCore.Qt.AlignTop)
        self.gridLayout_3.addWidget(self.widget_25, 1, 1, 1, 2)
        self.widget_26 = QtWidgets.QWidget(self.widget_17)
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
        self.label_18 = QtWidgets.QLabel(self.widget_26)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_20.addWidget(self.label_18, 0, QtCore.Qt.AlignTop)
        self.noches_modfi = QtWidgets.QSpinBox(self.widget_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noches_modfi.sizePolicy().hasHeightForWidth())
        self.noches_modfi.setSizePolicy(sizePolicy)
        self.noches_modfi.setMinimumSize(QtCore.QSize(0, 65))
        self.noches_modfi.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Verdana\";\n"
"border:1px solid gray;\n"
"")
        self.noches_modfi.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.noches_modfi.setObjectName("noches_modfi")
        self.verticalLayout_20.addWidget(self.noches_modfi, 0, QtCore.Qt.AlignTop)
        self.gridLayout_3.addWidget(self.widget_26, 1, 3, 1, 2)
        self.widget_27 = QtWidgets.QWidget(self.widget_17)
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
        self.label_22 = QtWidgets.QLabel(self.widget_27)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_24.addWidget(self.label_22, 0, QtCore.Qt.AlignTop)
        self.observaciones_modifi = QtWidgets.QTextEdit(self.widget_27)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.observaciones_modifi.sizePolicy().hasHeightForWidth())
        self.observaciones_modifi.setSizePolicy(sizePolicy)
        self.observaciones_modifi.setMinimumSize(QtCore.QSize(0, 0))
        self.observaciones_modifi.setMaximumSize(QtCore.QSize(16777215, 16777204))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.observaciones_modifi.setFont(font)
        self.observaciones_modifi.setStyleSheet("font: 9pt \"Verdana\";")
        self.observaciones_modifi.setObjectName("observaciones_modifi")
        self.verticalLayout_24.addWidget(self.observaciones_modifi)
        self.gridLayout_3.addWidget(self.widget_27, 1, 5, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_17)
        self.widget_28 = QtWidgets.QWidget(self.page_historial)
        self.widget_28.setObjectName("widget_28")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_28)
        self.horizontalLayout_5.setContentsMargins(0, 20, 25, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_finalizar = QtWidgets.QPushButton(self.widget_28)
        self.btn_finalizar.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.btn_finalizar.setFont(font)
        self.btn_finalizar.setStyleSheet("background-color: rgb(29, 124, 23);\n"
"font: 87 11pt \"Roboto Black\";\n"
"color: rgb(255, 255, 255);")
        self.btn_finalizar.setObjectName("btn_finalizar")
        self.horizontalLayout_5.addWidget(self.btn_finalizar, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.widget_28)
        self.stackedWidget.addWidget(self.page_historial)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi()
        self.stackedWidget.setCurrentIndex(0)

    def retranslateUi(self):
        self.label.setText("ELIMINAR")
        self.label_4.setText("MODIFICAR")
        self.label_8.setText("<html><head/><body><p>RESERVACIONES</p></body></html>")
        item = self.tabla_resv_mod.horizontalHeaderItem(0)
        item.setText("No. Habitación")
        item = self.tabla_resv_mod.horizontalHeaderItem(1)
        item.setText("Reponsable")
        item = self.tabla_resv_mod.horizontalHeaderItem(2)
        item.setText("No. de personas")
        item = self.tabla_resv_mod.horizontalHeaderItem(3)
        item.setText("Fecha de entrada")
        item = self.tabla_resv_mod.horizontalHeaderItem(4)
        item.setText("Fecha de salida")
        item = self.tabla_resv_mod.horizontalHeaderItem(5)
        item.setText("Teléfono")
        item = self.tabla_resv_mod.horizontalHeaderItem(6)
        item.setText("No. Matriculas")
        self.label_10.setText("Nombre[Name]:")
        self.label_11.setText("No. De niños[Children]:")
        self.label_16.setText("Teléfono[Phone]:")
        self.label_15.setText("Correo electrónico[Email]:")
        self.label_12.setText("No. Adultos[Adult]:")
        self.label_17.setText("No. Matricula del carro[Car license plates]:")
        self.siguiente_btn_mod.setText("SIGUIENTE")
        self.label_19.setText("Dirección[Adress]:Paseo del Riscal S/N. Colonia<br>Vicente Guerrero, Zihuatanejo de Azueta")
        self.label_20.setText("Nombre del hotel[Hotel<br> name]: Hotel Posada el Riscal")
        self.label_21.setText("No. Habitación[room number]:")
        self.label_13.setText("Fecha de entrada[Check in date]:")
        self.label_14.setText("Fecha de salida[Check out date]:")
        self.label_18.setText("Cantidad de noche:")
        self.label_22.setText("Observaciones:")
        self.btn_finalizar.setText("FINALIZAR REGISTRO")


from PyQt5 import QtCore, QtGui, QtWidgets
from Entradas import Entradas
from Estado_hotel import Estado_hotel
from modificaciones import modificaciones
from Salidas import Salidas

class Ui_Menu(QtWidgets.QWidget):
    def __init__(self):
        menu_Entradas = Entradas()
        menu_Estado_hotel = Estado_hotel()
        menu_Modificaciones = modificaciones()
        menu_Salidas = Salidas()

        super().__init__()
        self.resize(984, 810)
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
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(350, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(350, 16777215))
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
"background-color: rgb(178, 210, 201);\n"
"border:3px solid black;\n"
"}\n"
"\n"
"QWidget#widget_9{\n"
"background-color: rgb(178, 210, 201);\n"
"}\n"
"\n"
"QLabel{\n"
"border:0px solid black;\n"
"background-color: rgb(178, 210, 201);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(70)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/logo_hotel.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.entrada_btn = QtWidgets.QPushButton(self.widget_2)
        self.entrada_btn.setMinimumSize(QtCore.QSize(300, 70))
        self.entrada_btn.setMaximumSize(QtCore.QSize(330, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.entrada_btn.setFont(font)
        self.entrada_btn.setToolTipDuration(-2)
        self.entrada_btn.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"font: 87 12pt \"Roboto Black\";\n"
"background-color:white;\n"
"border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:3px solid Black;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/palma.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.entrada_btn.setIcon(icon)
        self.entrada_btn.setIconSize(QtCore.QSize(70, 70))
        self.entrada_btn.setObjectName("entrada_btn")
        self.verticalLayout.addWidget(self.entrada_btn, 0, QtCore.Qt.AlignHCenter)
        self.salida_btn = QtWidgets.QPushButton(self.widget_2)
        self.salida_btn.setMinimumSize(QtCore.QSize(300, 70))
        self.salida_btn.setMaximumSize(QtCore.QSize(330, 16777215))
        self.salida_btn.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"font: 87 12pt \"Roboto Black\";\n"
"background-color:white;\n"
"border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:3px solid Black;\n"
"}")
        self.salida_btn.setIcon(icon)
        self.salida_btn.setIconSize(QtCore.QSize(70, 70))
        self.salida_btn.setObjectName("salida_btn")
        self.verticalLayout.addWidget(self.salida_btn, 0, QtCore.Qt.AlignHCenter)
        self.Estado_hotel_btn = QtWidgets.QPushButton(self.widget_2)
        self.Estado_hotel_btn.setMinimumSize(QtCore.QSize(300, 70))
        self.Estado_hotel_btn.setMaximumSize(QtCore.QSize(330, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Estado_hotel_btn.setFont(font)
        self.Estado_hotel_btn.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"font: 87 12pt \"Roboto Black\";\n"
"background-color:white;\n"
"border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:3px solid Black;\n"
"}")
        self.Estado_hotel_btn.setIcon(icon)
        self.Estado_hotel_btn.setIconSize(QtCore.QSize(70, 70))
        self.Estado_hotel_btn.setObjectName("Estado_hotel_btn")
        self.verticalLayout.addWidget(self.Estado_hotel_btn, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.widget_9 = QtWidgets.QWidget(self.widget_2)
        self.widget_9.setStyleSheet("")
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.salir_btn = QtWidgets.QPushButton(self.widget_9)
        self.salir_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.salir_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Roboto\";")
        self.salir_btn.setObjectName("salir_btn")
        self.horizontalLayout_2.addWidget(self.salir_btn)
        self.modificar_btn = QtWidgets.QPushButton(self.widget_9)
        self.modificar_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.modificar_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Roboto\";")
        self.modificar_btn.setObjectName("modificar_btn")
        self.horizontalLayout_2.addWidget(self.modificar_btn)
        self.verticalLayout.addWidget(self.widget_9)
        self.horizontalLayout.addWidget(self.widget_2)

        self.Mostrar_menu = QtWidgets.QStackedWidget(self.widget)
        self.horizontalLayout.addWidget(self.Mostrar_menu)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.Mostrar_menu.addWidget(menu_Entradas)
        self.Mostrar_menu.addWidget(menu_Salidas)
        self.Mostrar_menu.addWidget(menu_Estado_hotel)
        self.Mostrar_menu.addWidget(menu_Modificaciones)

        self.entrada_btn.clicked.connect(self.mostarMenuEntradas)
        self.modificar_btn.clicked.connect(self.mostarMenuModificaciones)
        self.salida_btn.clicked.connect(self.mostarMenuSalidas)
        self.Estado_hotel_btn.clicked.connect(self.mostarMenuEstadoHotel)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def mostarMenuEntradas(self):
        self.Mostrar_menu.setCurrentIndex(0)

    def mostarMenuSalidas(self):
        self.Mostrar_menu.setCurrentIndex(1)

    def mostarMenuEstadoHotel(self):
        self.Mostrar_menu.setCurrentIndex(2)

    def mostarMenuModificaciones(self):
        self.Mostrar_menu.setCurrentIndex(3)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Menu", "Form"))
        self.entrada_btn.setText(_translate("Menu", "ENTRADAS"))
        self.salida_btn.setText(_translate("Menu", "SALIDAS"))
        self.Estado_hotel_btn.setText(_translate("Menu", "ESTADO DEL HOTEL"))
        self.salir_btn.setText(_translate("Menu", "SALIR"))
        self.modificar_btn.setText(_translate("Menu", "MODIFICAR"))

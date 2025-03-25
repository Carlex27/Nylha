from PyQt5 import QtCore, QtGui, QtWidgets
from Menu import Ui_Menu
from Loging import login

class main_window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.lg = login()
        self.menu = Ui_Menu()

        self.resize(787, 531)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.stackedWidget.setObjectName("stackedWidget")
        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.stackedWidget.addWidget(self.lg)
        self.stackedWidget.addWidget(self.menu)

        self.lg.Button_session.clicked.connect(self.sesion_activada)
        self.menu.salir_btn.clicked.connect(self.sesion_desacticada)

    def sesion_activada(self):
        self.stackedWidget.setCurrentIndex(1)
        pass

    def sesion_desacticada(self):
        self.stackedWidget.setCurrentIndex(0)
        pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = main_window()
    ui.show()
    sys.exit(app.exec_())

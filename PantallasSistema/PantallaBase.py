"""Base para pantallas apiladas: QWidget"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

class PantallaBase(QWidget):
    def __init__(self, ParientePantalla=None):
        super().__init__(ParientePantalla)
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.hide()

    def CentrarComponentes(self):
        self.componentes.setGeometry(0, 0, self.width(), self.height())

    def showEvent(self, event):
        super().showEvent(event)
        self.componentes.show()
        self.CentrarComponentes()
        if hasattr(self, "Entrada"):
            self.Entrada()

    def hideEvent(self, event):
        super().hideEvent(event)
        if hasattr(self, "Salida"):
            self.Salida()
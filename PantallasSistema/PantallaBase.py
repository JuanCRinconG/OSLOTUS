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
        # SOLO intentar centrar si existen componentes
        if hasattr(self, "componentes"):
            self.componentes.setGeometry(0, 0, self.width(), self.height())

    def reescalar(self):
        if hasattr(self, "componentes"):
            comp = self.componentes
            if hasattr(comp, "cuadrar") and callable(getattr(comp, "cuadrar")):
                comp.cuadrar()
                return
            for nombre in dir(comp):
                if nombre.startswith("CuadrarComponentes"):
                    getattr(comp, nombre)()
                    return

    def CuadrarComponentes(self):
        self.reescalar()

    def showEvent(self, event):
        super().showEvent(event)
        # SOLO mostrar si existen componentes
        if hasattr(self, "componentes"):
            self.componentes.show()
            self.CentrarComponentes()
            self.reescalar()
            
        if hasattr(self, "Entrada"):
            self.Entrada()

    def hideEvent(self, event):
        super().hideEvent(event)
        if hasattr(self, "Salida"):
            self.Salida()
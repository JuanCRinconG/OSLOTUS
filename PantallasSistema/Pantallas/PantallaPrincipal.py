from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from PantallasSistema.PantallaBase import PantallaBase
from PantallasSistema.Componentes import ComponentesPrincipal


class PantallaPrincipal(PantallaBase):
    """Escritorio principal del OS simulado (placeholder hasta ComponentesPrincipal)."""

    def __init__(self, Controlador=None):
        super().__init__()

        self.Controlador = Controlador

        self.componentes = ComponentesPrincipal(self)
        

        self.etiqueta_placeholder = QLabel(self, text="Escritorio principal")
        self.etiqueta_placeholder.setAlignment(Qt.AlignCenter)
        self.etiqueta_placeholder.setStyleSheet("color: #cccccc; font-size: 18px;")

        self.setStyleSheet("""background-color: #1a1a1a; border: 2px solid #333333;""")
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.hide()

    def CentrarComponentes(self):
        self.etiqueta_placeholder.setGeometry(0, 0, self.width(), self.height())

    def showEvent(self, event):
        super().showEvent(event)
        self.etiqueta_placeholder.show()
        self.CentrarComponentes()

    def hideEvent(self, event):
        super().hideEvent(event)

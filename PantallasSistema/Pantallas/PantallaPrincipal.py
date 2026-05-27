from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from PantallasSistema.PantallaBase import PantallaBase
from PantallasSistema.Componentes.ComponentesPrincipal import ComponentesPrincipal
from PantallasSistema.Componentes.ComponentesBarraTareas import ComponentesBarraTareas, ALTURA_BARRA

class PantallaPrincipal(PantallaBase):
    """Escritorio principal con Pomodoro y Barra de Tareas."""

    def __init__(self, Controlador=None):
        super().__init__()
        self.Controlador = Controlador

        # 1. Escritorio (Tu lógica de Pomodoro y Apps)
        self.componentes = ComponentesPrincipal(self.Controlador, self)

        # 2. Barra de tareas (Nueva funcionalidad)
        self.barra_tareas = ComponentesBarraTareas(self)

        # UI del placeholder
        self.etiqueta_placeholder = QLabel(self, text="Escritorio principal")
        self.etiqueta_placeholder.setAlignment(Qt.AlignCenter)
        self.etiqueta_placeholder.setStyleSheet("color: #cccccc; font-size: 18px;")

        self.setStyleSheet("background-color: #1a1a1a; border: 2px solid #333333;")
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.hide()

    def CuadrarComponentes(self):
        """El escritorio ocupa todo MENOS la barra de tareas"""
        self.componentes.setGeometry(
            0, 0,
            self.width(),
            self.height() - ALTURA_BARRA
        )
        self.barra_tareas.CuadrarBarraTareas()

    def reescalar(self):
        super().reescalar()
        self.CentrarEtiqueta()

    def Entrada(self):
        self.CuadrarComponentes()
        print("Pantalla Principal entered")

    def Salida(self):
        print("Pantalla Principal exited")

    def CentrarEtiqueta(self):
        self.etiqueta_placeholder.setGeometry(0, 0, self.width(), self.height())
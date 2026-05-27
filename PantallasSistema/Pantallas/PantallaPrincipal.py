from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from PantallasSistema.PantallaBase import PantallaBase
from PantallasSistema.Componentes.ComponentesPrincipal import ComponentesPrincipal
from PantallasSistema.Componentes.ComponentesBarraTareas import ComponentesBarraTareas, ALTURA_BARRA

class PantallaPrincipal(PantallaBase):
    """Escritorio principal integrado con Pomodoro y Barra de Tareas."""

    def __init__(self, Controlador=None):
        super().__init__()
        self.Controlador = Controlador

        # CORRECTO: Inicialización pasando el Controlador para que el Pomodoro/Firewall funcione
        self.componentes = ComponentesPrincipal(self.Controlador, self)

        # Inicialización de la barra de tareas
        self.barra_tareas = ComponentesBarraTareas(self)

        self.setStyleSheet("background-color: #1a1a1a; border: 2px solid #333333;")
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.hide()

    def CuadrarComponentes(self):
        """Calcula el espacio dejando el hueco para la barra inferior"""
        # El escritorio ocupa todo MENOS la altura de la barra
        self.componentes.setGeometry(
            0, 0,
            self.width(),
            self.height() - ALTURA_BARRA
        )
        # Posiciona la barra de tareas
        self.barra_tareas.CuadrarBarraTareas()

    def Entrada(self):
        self.CuadrarComponentes()
        print("Pantalla Principal entered")

    def Salida(self):
        print("Pantalla Principal exited")

    def reescalar(self):
        super().reescalar()
        self.CuadrarComponentes()
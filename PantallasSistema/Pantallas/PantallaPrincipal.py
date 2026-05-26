from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore    import Qt

from PantallasSistema.PantallaBase   import PantallaBase
from PantallasSistema.Componentes    import ComponentesPrincipal, ComponentesBarraTareas
from PantallasSistema.Componentes.ComponentesBarraTareas import ALTURA_BARRA


class PantallaPrincipal(PantallaBase):

    def __init__(self, Controlador=None):
        super().__init__()
        self.Controlador = Controlador

        # Escritorio
        self.componentes = ComponentesPrincipal(self)

        # Barra de tareas
        self.barra_tareas = ComponentesBarraTareas(self)

        self.setStyleSheet("background-color: #1a1a1a; border: 2px solid #333333;")
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.hide()

    def CuadrarComponentes(self):
        # El escritorio ocupa todo MENOS la barra
        self.componentes.setGeometry(
            0, 0,
            self.width(),
            self.height() - ALTURA_BARRA
        )
        self.barra_tareas.CuadrarBarraTareas()

    def Entrada(self):
        self.CuadrarComponentes()
        print("Pantalla Principal entered")

    def Salida(self):
        print("Pantalla Principal exited")
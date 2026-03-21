from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PantallasSistema.Componentes.ComponentesBootup import ComponentesBootup

class PantallaBootUp(QWidget):
    def __init__(self, Controlador=None):
        super().__init__()
        self.Controlador = Controlador

        self.componentes = ComponentesBootup(self)

        self.componentes.CambiarPagina.connect(self.IrUsuario)

        self.setStyleSheet("""background-color: black; border: 2px solid black;""")
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.hide()

       
    def CentrarComponentes(self):
        self.componentes.setGeometry(0, 0, self.width(), self.height())
        self.componentes.CuadrarComponentesBootup()


    def IrUsuario(self):
        if self.Controlador:
            self.Controlador.IrPantallaUsuario()

    def showEvent(self, event):
        super().showEvent(event)
        self.componentes.show()
        self.CentrarComponentes()
        print("Pantalla bootup entered")

    def hideEvent(self, event):
        super().hideEvent(event)
        print("Pantalla bootup exited")



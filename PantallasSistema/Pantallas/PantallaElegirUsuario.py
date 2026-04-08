from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PantallasSistema.Componentes import ComponentesElegirUsuario
from Recursos import PC_AzulOSLotus

class PantallaElegirUsuario(QWidget):
    def __init__(self, Controlador=None):
        super().__init__()
        self.Controlador = Controlador

        self.componentes = ComponentesElegirUsuario(self)
        self.componentes.IngresarSistema.connect(self.IrPantallaPrincipal)


        self.setStyleSheet(f"""background-color:{PC_AzulOSLotus}; border: 2px solid black;""")
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.hide()

       
    def CentrarComponentes(self):
        self.componentes.setGeometry(0, 0, self.width(), self.height())
        self.componentes.CuadrarComponentesElegirUsuario()

    def IrPantallaPrincipal(self):
        if self.Controlador:
            self.Controlador.IrPantalla("PantallaPrincipal")

    def showEvent(self, event):
        super().showEvent(event)
        self.componentes.show()
        self.CentrarComponentes()
        print("Pantalla elegir usuario entered")

    def hideEvent(self, event):
        super().hideEvent(event)
        print("Pantalla elegir usuario exited")



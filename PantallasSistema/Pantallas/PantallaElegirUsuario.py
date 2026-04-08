from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PantallasSistema.Componentes import ComponentesElegirUsuario
from PantallasSistema import PantallaBase
from Recursos import PC_AzulOSLotus

class PantallaElegirUsuario(PantallaBase):
    def __init__(self, Controlador=None):
        super().__init__()
        self.Controlador = Controlador

        self.componentes = ComponentesElegirUsuario(self)
        self.componentes.IngresarSistema.connect(self.IrPantallaPrincipal)


        self.setStyleSheet(f"""background-color:{PC_AzulOSLotus}; border: 2px solid black;""")
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.hide()

    def CuadrarComponentes(self):
        self.componentes.CuadrarComponentesElegirUsuario()

    def Entrada(self):
        self.CuadrarComponentes()
        print("Pantalla elegir usuario entered")

    def Salida(self):
        print("Pantalla elegir usuario exited")

    def IrPantallaPrincipal(self):
        if self.Controlador:
            self.Controlador.IrPantalla("PantallaPrincipal")





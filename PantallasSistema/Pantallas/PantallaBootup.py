from PantallasSistema.Componentes import ComponentesBootup
from PantallasSistema.PantallaBase import PantallaBase

class PantallaBootUp(PantallaBase):
    def __init__(self, ControladorSistema=None):
        super().__init__()
        self.Controlador = ControladorSistema
        self.componentes = ComponentesBootup(self)

        self.componentes.CambiarPagina.connect(self.IrElegirUsuario)

        self.setStyleSheet("""background-color: black; border: 2px solid black;""")


    def IrElegirUsuario(self):
        if self.Controlador:
            self.Controlador.IrPantalla("PantallaElegirUsuario")

    def CuadrarComponentes(self):
        self.componentes.CuadrarComponentesBootup()

    def Entrada(self):
        self.CuadrarComponentes()
        print("Pantalla bootup entered")

    def Salida(self):
        print("Pantalla bootup exited")



from Recursos import DR_OverlayEjemplo_Alto, DR_OverlayEjemplo_Ancho
from PantallasSistema.Componentes import ComponentesOverlayEjemplo
from PantallasSistema.PantallaBase import PantallaBase

class PantallaOverlayEjemplo(PantallaBase):
    def __init__(self, ControladorSistema=None, ParientePantalla=None):
        super().__init__(ParientePantalla)
        self.Controlador = ControladorSistema

        self.componentes = ComponentesOverlayEjemplo(self)

        self.componentes.CerrarPrograma.connect(self.ElegirUsuario)

        self.setStyleSheet("""background-color: red; border: 2px solid black;""")
        self.CuadrarPantalla()

    def CuadrarPantalla(self):
        p = self.parent()
        if not p:
            return
        w = max(1, int(p.width() * DR_OverlayEjemplo_Ancho))
        h = max(1, int(p.height() * DR_OverlayEjemplo_Alto))
        self.setFixedSize(w, h)
        parent_rect = p.rect()
        self.move(parent_rect.center() - self.rect().center())

    def CuadrarComponentes(self):
        self.componentes.CuadrarComponentesOverlayEjemplo()

    def ElegirUsuario(self):
        if self.Controlador:
            print("Boton de elegir usuario presionado")
            self.Controlador.BorrarTodasPantallas()


    def Entrada(self):
        print("PantallaOverlayEjemplo entered")
        self.CuadrarPantalla()
        self.CuadrarComponentes()


    def Salida(self):
        print("PantallaOverlayEjemplo exited")

    


from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from LogicaMadre.ControladorEventos import ControladorEventos
from PantallasSistema.Componentes.ComponentesUsuario import ComponentesUsuario


class PantallaUsuario(QWidget, ControladorEventos):
    def __init__(self, Controlador=None,  Pariente=None):
        super().__init__(Pariente)
        self.Controlador = Controlador

        self.container = ComponentesUsuario(self)

        self.container.CerrarPrograma.connect(self.ElegirUsuario)

        self.setStyleSheet("""background-color: red; border: 2px solid black;""")
        self.setFixedSize(600, 400)
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.hide()

    def CentrarPantalla(self):
        if self.parent():
            parent_rect = self.parent().rect()
            self.move(parent_rect.center() - self.rect().center())


    def CentrarComponentes(self):
        parent_rect = self.rect()
        container_rect = self.container.rect()
        x = (parent_rect.width() - container_rect.width()) // 2
        y = (parent_rect.height() - container_rect.height()) // 2
        self.container.move(x, y)

    def Entrada(self):
        self.container.show()
        self.CentrarPantalla()
        self.CentrarComponentes()


    def ElegirUsuario(self):
        if self.Controlador:
            print("Boton de elegir usuario presionado")
            self.Controlador.LimpiarPaginas()

    


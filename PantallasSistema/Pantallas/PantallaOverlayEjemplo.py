from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PantallasSistema.Componentes.ComponentesOverlayEjemplo import ComponentesOverlayEjemplo


class PantallaOverlayEjemplo(QWidget):
    def __init__(self, Controlador=None,  Pariente=None):
        super().__init__(Pariente)
        self.Controlador = Controlador

        self.componentes = ComponentesOverlayEjemplo(self)

        self.componentes.CerrarPrograma.connect(self.ElegirUsuario)

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
        container_rect = self.componentes.rect()
        x = (parent_rect.width() - container_rect.width()) // 2
        y = (parent_rect.height() - container_rect.height()) // 2
        self.componentes.move(x, y)


    def ElegirUsuario(self):
        if self.Controlador:
            print("Boton de elegir usuario presionado")
            self.Controlador.LimpiarPaginas()

    def showEvent(self, event):
        super().showEvent(event)
        print("PantallaOverlayEjemplo entered")
        self.componentes.show()
        self.CentrarPantalla()
        self.CentrarComponentes()

    def hideEvent(self, event):
        super().hideEvent(event)
        print("PantallaOverlayEjemplo exited")

    


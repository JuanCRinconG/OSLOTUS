from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QEvent, Qt
from Logica_madre.ControladorEventos import ControladorEventos
from PantallasSistema.Componentes.ComponentesUsuario import ComponentesUsuario


#problema existente: la pagina usuario crea una nueva ventana al llamarla
#solucion: hacer que la pagina usuario sea un widget hijo de la pagina bootup, y mostrarla como un overlay centrado en la pagina bootup, asi no se crean nuevas ventanas y se mantiene todo dentro de la misma ventana principal


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

    def center_on_parent(self):
        if self.parent():
            parent_rect = self.parent().rect()
            self.move(parent_rect.center() - self.rect().center())

        

    def center_container(self):
        parent_rect = self.rect()
        container_rect = self.container.rect()

        x = (parent_rect.width() - container_rect.width()) // 2
        y = (parent_rect.height() - container_rect.height()) // 2

        self.container.move(x, y)

    def Entrada(self):
        self.container.show()
        self.center_on_parent()
        self.center_container()

    def showEvent(self, event):
        super().showEvent(event)

        if self.parent():
            self.parent().installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.parent() and event.type() == QEvent.Resize:
            self.center_container()
            self.center_on_parent()
        return super().eventFilter(obj, event)


    def ElegirUsuario(self):
        if self.Controlador:
            print("Boton de elegir usuario presionado")
            self.Controlador.LimpiarPaginas()

    


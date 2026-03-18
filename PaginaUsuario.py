from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class PaginaUsuario(QWidget):
    def __init__(self, Controlador=None, Pariente=None):
        super().__init__(Pariente)
        self.Controlador = Controlador
        EstructuraUsuario = QVBoxLayout()

        self.setStyleSheet("""background-color: red; border: 2px solid black;""")
        self.setFixedSize(300, 200)
        
        #Elementos que van adentro de la pagina
        self.LabelUsuario = QLabel(self, text='Elegir un usuario')
        self.LabelUsuario.setAlignment(Qt.AlignCenter)
        self.BotonPaginaPrincipal = QPushButton(self, text='Usuario 1')
        self.BotonPaginaPrincipal.clicked.connect(self.ElegirUsuario)


        EstructuraUsuario.addWidget(self.LabelUsuario)
        EstructuraUsuario.addWidget(self.BotonPaginaPrincipal)
        self.setLayout(EstructuraUsuario)

    def ElegirUsuario(self):
        if self.Controlador:
            print("Boton de elegir usuario presionado")
            self.Controlador.LimpiarPaginas()

    def center_on_parent(self):
        if self.parent():
            parent_rect = self.parent().geometry()
            self.move(parent_rect.center() - self.rect().center())
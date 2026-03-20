from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QPixmap
import os
from PyQt5.QtCore import pyqtSignal
from Logica_madre.ControladorEventos import ControladorEventos


class ComponentesUsuario(QWidget, ControladorEventos):
    CerrarPrograma = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("""background-color: red;border-radius: 2px;""")
        self.setFixedSize(400, 300)

        EstructuraUsuario = QGridLayout()

        

        #Elementos que van adentro de la pagina
        self.LabelUsuario = QLabel(self, text='Elegir un usuario')
        self.LabelUsuario.setAlignment(Qt.AlignCenter)
        
        ruta = os.path.join("Imagenes", "LotusOS_solid.png")

        self.LogoLotus = QLabel()
        self.LogoLotus.setAlignment(Qt.AlignCenter)
        Imagen = QPixmap(ruta).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.LogoLotus.setPixmap(Imagen)


        self.BotonPaginaPrincipal = QPushButton(self, text='Usuario 1')
        self.BotonPaginaPrincipal.clicked.connect(self.CerrarPrograma.emit)
        

        EstructuraUsuario.addWidget(self.LabelUsuario, 1, 1)
        EstructuraUsuario.addWidget(self.LogoLotus, 0, 0)
        EstructuraUsuario.addWidget(self.BotonPaginaPrincipal, 2, 2)

        
        self.setLayout(EstructuraUsuario)

    def center_on_parent(self):
        parent = self.parent()
        if not parent:
            return

        x = (parent.width() - self.width()) // 2
        y = (parent.height() - self.height()) // 2

 
        self.move(x, y)
        
    def showEvent(self, event):
        super().showEvent(event)

        if self.parent():
            self.parent().installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.parent() and event.type() == QEvent.Resize:
            self.center_container()
            self.center_on_parent()
        return super().eventFilter(obj, event)


    def Entrada(self):
        self.center_on_parent()

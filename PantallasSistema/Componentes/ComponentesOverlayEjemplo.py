from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os
from PyQt5.QtCore import pyqtSignal


class ComponentesOverlayEjemplo(QWidget):
    CerrarPrograma = pyqtSignal()

    def __init__(self, ParientePantalla=None):
        super().__init__(ParientePantalla)

        self.setStyleSheet("""background-color: red;border-radius: 2px;""")

        EstructuraOverlay = QGridLayout()

        

        #Elementos que van adentro de la pagina
        self.LabelUsuario = QLabel(self, text='Elegir un usuario')
        self.LabelUsuario.setAlignment(Qt.AlignCenter)
        
        ruta = os.path.join("Recursos", "LotusOS_solid.png")

        self.LogoLotus = QLabel(self)
        self.LogoLotus.setAlignment(Qt.AlignCenter)
        Imagen = QPixmap(ruta).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.LogoLotus.setPixmap(Imagen)


        self.BotonPaginaPrincipal = QPushButton(self, text='Usuario 1')
        self.BotonPaginaPrincipal.clicked.connect(self.CerrarPrograma.emit)
        

        EstructuraOverlay.addWidget(self.LabelUsuario, 1, 1)
        EstructuraOverlay.addWidget(self.LogoLotus, 0, 0)
        EstructuraOverlay.addWidget(self.BotonPaginaPrincipal, 2, 2)

        
        self.setLayout(EstructuraOverlay)

    def CuadrarComponentesOverlayEjemplo(self):
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())

    def showEvent(self, event):
        super().showEvent(event)
        print("ComponentesOverlayEjemplo entered")

    def hideEvent(self, event):
        super().hideEvent(event)
        print("ComponentesOverlayEjemplo exited")
        

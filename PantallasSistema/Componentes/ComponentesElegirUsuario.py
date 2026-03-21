from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import QTimer, Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QFont, QFontMetrics
from Recursos.AnimacionesPyQt5 import AnimacionesPyQt5

import os
import time

class ComponentesElegirUsuario(QWidget, AnimacionesPyQt5):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("""background-color: transparent;border-radius: 2px;""")

        GothicNormal = QFont("Century Gothic") 
        

        #Elementos que van adentro de la pagina
        self.LabelElegirUsuario = QLabel(self, text="ElegirUsuario")
        self.LabelElegirUsuario.setAlignment(Qt.AlignCenter)
        self.LabelElegirUsuario.setFont(GothicNormal)
        self.LabelElegirUsuario.setStyleSheet("color: white")

    def CuadrarComponentesElegirUsuario(self):  
        self.LabelElegirUsuario.setAlignment(Qt.AlignCenter)

    def showEvent(self, event):
        super().showEvent(event)
        self.CuadrarComponentesElegirUsuario()
        print("Componente elegir usuario entered")
    
    
    

    def hideEvent(self, event):
        super().hideEvent(event)
        print("Componente elegir usuario exited")
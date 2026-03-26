from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt
from Recursos import AnimacionesPyQt5
from Recursos import GothicNormal
from Recursos import PC_Blanco, PC_Transparente


class ComponentesElegirUsuario(QWidget, AnimacionesPyQt5):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet(
            f"background-color: {PC_Transparente}; border-radius: 2px;"
        )

        #Elementos que van adentro de la pagina
        self.LabelElegirUsuario = QLabel(self, text="ElegirUsuario")
        self.LabelElegirUsuario.setAlignment(Qt.AlignCenter)
        self.LabelElegirUsuario.setFont(GothicNormal)
        self.LabelElegirUsuario.setStyleSheet(f"color: {PC_Blanco}")

    def CuadrarComponentesElegirUsuario(self):  
        self.LabelElegirUsuario.setAlignment(Qt.AlignCenter)

    def showEvent(self, event):
        super().showEvent(event)
        self.CuadrarComponentesElegirUsuario()
        print("Componente elegir usuario entered")
    
    
    

    def hideEvent(self, event):
        super().hideEvent(event)
        print("Componente elegir usuario exited")
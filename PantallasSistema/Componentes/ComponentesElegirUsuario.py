from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from Recursos import AnimacionesPyQt5
from Recursos import GothicNormal
from Recursos import PC_Blanco, PC_Transparente
import os


class ComponentesElegirUsuario(QWidget, AnimacionesPyQt5):
    IngresarSistema = pyqtSignal()
    def __init__(self, parent=None):
        
        super().__init__(parent)

        self.setStyleSheet(
            f"background-color: {PC_Transparente}; border-radius: 2px;"
        )

        #Elementos que van adentro de la pagina
        ruta = os.path.join("Recursos", "PantallaElegirUsuarioImagen.png")


        self.Imagen = QPixmap(ruta)
        self.LabelElegirUsuario = QLabel(self)
        self.LabelElegirUsuario.setScaledContents(False)

        self.BotonPantallaPrincipal = QPushButton(self, text="Ingresar")
        self.BotonPantallaPrincipal.setFont(GothicNormal)
        self.BotonPantallaPrincipal.clicked.connect(self.IngresarSistema.emit)



    def CuadrarComponentesElegirUsuario(self):  
        w = self.width()
        h = self.height()
        if w < 1 or h < 1:
            return
    
        if self.Imagen.isNull():
            return
        ImagenCorrecta = self.Imagen.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.LabelElegirUsuario.setPixmap(ImagenCorrecta)
        ImagenW = ImagenCorrecta.width()
        ImagenH = ImagenCorrecta.height()
        self.LabelElegirUsuario.setGeometry((w - ImagenW) // 2, (h - ImagenH) // 2, ImagenW, ImagenH)

        self.BotonPantallaPrincipal.setGeometry((w - self.BotonPantallaPrincipal.width()) // 2, int(((h - self.BotonPantallaPrincipal.height()) // 2)*1.7), 
                                                self.BotonPantallaPrincipal.width(), self.BotonPantallaPrincipal.height())




    def showEvent(self, event):
        super().showEvent(event)
        self.CuadrarComponentesElegirUsuario()
        print("Componente elegir usuario entered")
    
    

    def hideEvent(self, event):
        super().hideEvent(event)
        print("Componente elegir usuario exited")
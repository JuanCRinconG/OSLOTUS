from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from LogicaMadre.ControladorEventos import ControladorEventos

class PantallaBootUp(QWidget, ControladorEventos):
    def __init__(self, Controlador=None):
        super().__init__()
        self.Controlador = Controlador
        EstructuraBoot = QVBoxLayout()

        self.setStyleSheet("background-color: orange;")
        
        #Elementos que van adentro de la pagina
        self.LabelBoot = QLabel(self, text='Bienvenido al sistema')
        self.LabelBoot.setAlignment(Qt.AlignCenter)
        self.BotonUsuario = QPushButton(self, text='Iniciar sesion')
        self.BotonUsuario.clicked.connect(self.IrUsuario)


        EstructuraBoot.addWidget(self.LabelBoot)
        EstructuraBoot.addWidget(self.BotonUsuario)
        self.setLayout(EstructuraBoot)

    def IrUsuario(self):
        if self.Controlador:
            self.Controlador.IrPantallaUsuario()

    def Entrada(self):
        print("Pantalla bootup entered")

    def Salida(self):
        print("Pantalla bootup exited")



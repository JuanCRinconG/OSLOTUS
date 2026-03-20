from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence

from GestorPantallas import GestorPantallas
from ControladorPantallas import ControladorPantallas

from PantallasSistema.Pantallas.PantallaBootup import PantallaBootUp
from PantallasSistema.Pantallas.PantallaUsuario import PantallaUsuario

#definir clase de aplicacion y sus atributos, aqui van los atajos de teclado y teclas
class Lotus(QMainWindow):
    def __init__(self):
        super().__init__()

        #Estilo de ventana
        self.setWindowTitle("Sistema operativo LOTUS")
        self.setGeometry(100, 100, 600, 400)
        

        # Contenedor principal para multiples mini paginas (procesos)
        self.container = QWidget()
        self.setCentralWidget(self.container)

        #Alterar funciones del teclado para que hagan cosas especificas en la pagina, usando funciones y vinculandolas
        PantallaCompleta = QShortcut(QKeySequence("Escape"), self)
        PantallaCompleta.activated.connect(self.PantallaCompleta)

        self.showFullScreen()
        self.container.setStyleSheet("background-color: black;")


        self.EstructuraSistema = QVBoxLayout()
        self.container.setLayout(self.EstructuraSistema)

        #Inicializar el gestor de paginas como 'Gestor' y el controlador de paginas como 'Controlador'
        self.Gestor = GestorPantallas()
        #Y pasar el gestor al controlador para que este pueda manejar las paginas
        self.Controlador = ControladorPantallas(self.Gestor)
        self.setCentralWidget(self.Gestor)

        #Agregar la pagina de bootup al gestor de paginas, y agregarle el controlador
        self.Gestor.AgregarPantalla("PantallaBootup", PantallaBootUp, self.Controlador)
        self.Gestor.AgregarSobrepantalla("PantallaUsuario", PantallaUsuario, self.Controlador, self)
        #Mostrar la pagina de bootup al iniciar la aplicacion
        self.Gestor.MostrarPantalla("PantallaBootup")

    def PantallaCompleta(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()
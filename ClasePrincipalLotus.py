from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
from GestorDePaginas import GestorDePaginas
from ControlladorDePaginas import ControladorDePaginas
import sys

from PaginaBootup import PaginaBootUp
from PaginaUsuario import PaginaUsuario

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
        self.Gestor = GestorDePaginas()
        #Y pasar el gestor al controlador para que este pueda manejar las paginas
        self.Controlador = ControladorDePaginas(self.Gestor)
        self.setCentralWidget(self.Gestor)

        #Agregar la pagina de bootup al gestor de paginas, y agregarle el controlador
        self.Gestor.AgregarPagina("PaginaBootup", PaginaBootUp, self.Controlador)
        self.Gestor.AgregarPagina("PaginaUsuario", PaginaUsuario, self.Controlador)
        #Mostrar la pagina de bootup al iniciar la aplicacion
        self.Gestor.MostrarPagina("PaginaBootup")

    def PantallaCompleta(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

     
#A diferencia de tkinter, el motor de PyQt5 se ejecuta en un loop separado de la clase principal.
#por lo que se debe crear una instancia de QApplication para que sea el motor de las ventanas que creemos 
#y asi registrar cosas como inputs de mouse o teclado,
#y ejecutar el loop para que la aplicación funcione correctamente.
MotorQT = QApplication(sys.argv)
Lotus = Lotus()
Lotus.show()
sys.exit(MotorQT.exec_())
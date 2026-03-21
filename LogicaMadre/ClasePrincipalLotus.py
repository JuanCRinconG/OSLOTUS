from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence

from LogicaMadre.GestorPantallas import GestorPantallas
from LogicaMadre.ControladorPantallas import ControladorPantallas

from PantallasSistema.Pantallas.PantallaBootup import PantallaBootUp
from PantallasSistema.Pantallas.PantallaElegirUsuario import PantallaElegirUsuario
from PantallasSistema.Pantallas.PantallaOverlayEjemplo import PantallaOverlayEjemplo

#definir clase de aplicacion y sus atributos, aqui van los atajos de teclado y teclas
class Lotus(QMainWindow):
    def __init__(self):
        super().__init__()

        #Estilo de ventana
        self.setWindowTitle("Sistema operativo LOTUS")
        self.setGeometry(100, 100, 1200, 800)
    

        #Alterar funciones del teclado para que hagan cosas especificas en la pagina, usando funciones y vinculandolas
        PantallaCompleta = QShortcut(QKeySequence("Escape"), self)
        PantallaCompleta.activated.connect(self.PantallaCompleta)

        self.showFullScreen()

        #Inicializar el gestor de paginas como 'Gestor' y el controlador de paginas como 'Controlador'
        self.Gestor = GestorPantallas()
        #Y pasar el gestor al controlador para que este pueda manejar las paginas
        self.Controlador = ControladorPantallas(self.Gestor)
        self.setCentralWidget(self.Gestor)

        #Agregar la pagina de bootup al gestor de paginas, y agregarle el controlador
        self.Gestor.AgregarPantalla("PantallaBootup", PantallaBootUp, self.Controlador)
        self.Gestor.AgregarPantalla("PantallaElegirUsuario", PantallaElegirUsuario, self.Controlador)
        self.Gestor.AgregarSobrepantalla("PantallaOverlayEjemplo", PantallaOverlayEjemplo, self.Controlador, self.Gestor)
        #Mostrar la pagina de bootup al iniciar la aplicacion
        self.Gestor.MostrarPantalla("PantallaBootup")

    def PantallaCompleta(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()
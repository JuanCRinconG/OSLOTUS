from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence


from PantallasSistema import PantallaBootUp, PantallaElegirUsuario, PantallaOverlayEjemplo

#definir clase de aplicacion y sus atributos
class Lotus(QMainWindow):
    def __init__(self, GestorPantallas=None, ControladorSistema=None):
        super().__init__()

        #Estilo de ventana
        self.setWindowTitle("Sistema operativo LOTUS")
        self.setGeometry(100, 100, 1200, 800)
    

        #Alterar funciones del teclado para que hagan cosas especificas en la pagina, usando funciones y vinculandolas
        PantallaCompleta = QShortcut(QKeySequence("Escape"), self)
        PantallaCompleta.activated.connect(self.PantallaCompleta)

        self.showFullScreen()

        #Inicializar el gestor de paginas como 'Gestor'
        self.Gestor = GestorPantallas
        self.Controlador = ControladorSistema

        self.setCentralWidget(self.Gestor)
        self.CrearPantallas()

    def PantallaCompleta(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    #Crear las pantallas y agregarlas al gestor de paginas
    def CrearPantallas(self):
        self.Gestor.AgregarPantalla("PantallaBootup", PantallaBootUp, self.Controlador)
        self.Gestor.AgregarPantalla("PantallaElegirUsuario", PantallaElegirUsuario, self.Controlador)
        self.Gestor.AgregarSobrepantalla("PantallaOverlayEjemplo", PantallaOverlayEjemplo, self.Controlador, self.Gestor)
    
    def IniciarAplicacion(self):
        self.Controlador.IrPantalla("PantallaBootup")
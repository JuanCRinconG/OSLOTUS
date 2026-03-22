#Es el controlador de la logica madre del sistema
#Se encarga de controlar y comunicar la logica del Sistema Operativo
#Con la logica de la Interfaz de Usuario
#Para no llenar clases como el gestor de pantallas con logica de sistema

class ControladorSistema:
    def __init__(self, GestorPantallas):
        self.Gestor = GestorPantallas

    def IrPantallaBootup(self):
        #Aca podria ir logica
        self.Gestor.MostrarPantalla("PantallaBootup")

    def IrPantallaOverlayEjemplo(self):
        #Aca podria ir logica y animaciones de salida
        self.Gestor.MostrarSobrepantalla("PantallaOverlayEjemplo")

    def IrPantalla(self, Pantalla):
        #Tratar de no poner mucha logica de diversas pantallas en funciones generales como esta
        #Aqui podrian ir animaciones de salida de todas las pantallas, si las tienen, con in if hasattr(clase, 'atributo')
        self.Gestor.MostrarPantalla(Pantalla)

    def BorrarTodasPantallas(self):
        #Aca podria ir logica y animaciones de salida
        self.Gestor.BorrarTodasPantallas()
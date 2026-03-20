

class ControladorPantallas:
    def __init__(self, GestorPantallas):
        self.Gestor = GestorPantallas

    def IrPantallaBootup(self):
        self.Gestor.MostrarPantalla("PantallaBootup")

    def IrPantallaUsuario(self):
        print('Funcion IrPantallaUsuario llamada')
        self.Gestor.MostrarSobrepantalla("PantallaUsuario")

    def IrPantalla(self, Pantalla):
        self.Gestor.MostrarPantalla(Pantalla)

    def LimpiarPaginas(self):
        self.Gestor.LimpiarPantallas()
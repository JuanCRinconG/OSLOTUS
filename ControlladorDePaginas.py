from PaginaUsuario import PaginaUsuario

class ControladorDePaginas:
    def __init__(self, GestorDePaginas):
        self.Gestor = GestorDePaginas

    def IrPaginaBootup(self):
        self.Gestor.MostrarPagina("boot")

    def IrPaginaUsuario(self, PaginaPariente=None):
        self.usuario_overlay = PaginaUsuario(self, PaginaPariente)
        self.usuario_overlay.center_on_parent()
        self.usuario_overlay.show()

    def IrPagina(self, Pagina):
        self.Gestor.MostrarPagina(Pagina)

    def LimpiarPaginas(self):
        self.Gestor.LimpiarPaginas()
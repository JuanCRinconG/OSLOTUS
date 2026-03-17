from PyQt5.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

class GestorDePaginas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.FilaPaginas = QStackedWidget()
        self.Paginas = {}
        self.HistorialPaginas = []

        EstructuraPaginas = QVBoxLayout()
        EstructuraPaginas.addWidget(self.FilaPaginas)
        self.setLayout(EstructuraPaginas)
        self.FilaPaginas.setStyleSheet("background-color: black;")

    def AgregarPagina(self, NombrePagina, ClasePagina, controller=None):
        if NombrePagina not in self.Paginas:
            NuevaPagina = ClasePagina(controller)
            self.Paginas[NombrePagina] = NuevaPagina
            self.FilaPaginas.addWidget(NuevaPagina)

    def MostrarPagina(self, NombrePagina):
        if NombrePagina in self.Paginas:
            PaginaActual = self.FilaPaginas.currentWidget()

            if PaginaActual and hasattr(PaginaActual, "on_exit"):
                PaginaActual.on_exit()

            next_page = self.Paginas[NombrePagina]

            if hasattr(next_page, "on_enter"):
                next_page.on_enter()

            self.FilaPaginas.setCurrentWidget(self.Paginas[NombrePagina])
    
    def QuitarPagina(self, NombrePagina):
        if NombrePagina in self.Paginas:
            Pagina = self.Paginas.pop(NombrePagina)
            self.FilaPaginas.removeWidget(Pagina)
            Pagina.deleteLater()

    def RestaurarPagina(self, NombrePagina):
        if NombrePagina in self.Paginas:
            Pagina = self.Paginas[NombrePagina]
            if hasattr(Pagina, "reset"):
                Pagina.reset()

    def LimpiarPaginas(self):
        for i in reversed(range(self.FilaPaginas.count())):
            widget = self.FilaPaginas.widget(i)
            self.FilaPaginas.removeWidget(widget)
            widget.deleteLater()
        self.Paginas.clear()
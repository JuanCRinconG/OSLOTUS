from PyQt5.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

class GestorPantallas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


        #Sistema de pantallas
        self.FilaPantallas = QStackedWidget()
        self.Pantallas = {}
        self.HistorialPantallas = []


        #Sistema de sobrepantallas
        self.Sobrepantallas = {}
        self.HistorialSobrepantallas = []


        #Estructura general del gestor de pantallas
        self.EstructuraPantallas = QVBoxLayout(self)
        self.EstructuraPantallas.setContentsMargins(0, 0, 0, 0)


        #Agregar el sistema de pantallas a la estructura general
        self.EstructuraPantallas.addWidget(self.FilaPantallas)

        self.setStyleSheet("background-color: black;")


        #Mantiene referencia a la sobrepantalla actual (si existe)
        self.SobrepantallasActuales = []
        

    def AgregarPantalla(self, NombrePantalla, ClasePantalla, controller=None):
        if NombrePantalla in self.Pantallas:
            return
        NuevaPantalla = ClasePantalla(controller)
        self.Pantallas[NombrePantalla] = NuevaPantalla
        self.FilaPantallas.addWidget(NuevaPantalla)


    def AgregarSobrepantalla(self, NombrePantalla, ClaseSobrepantalla, Controlador=None, Pariente=None):
        if NombrePantalla in self.Sobrepantallas:
            return
        NuevaPantalla = ClaseSobrepantalla(Controlador, Pariente)
        self.Sobrepantallas[NombrePantalla] = NuevaPantalla


    def MostrarPantalla(self, NombrePantalla):
        if NombrePantalla not in self.Pantallas:
            return
        if self.Pantallas[NombrePantalla] == self.FilaPantallas.currentWidget():
            return
        
        PantallaActual = self.FilaPantallas.currentWidget()
        SiguientePantalla = self.Pantallas[NombrePantalla]
        print("CURRENT:", PantallaActual)
        print("NEXT:", SiguientePantalla)

        #Cambiar pagina
        self.FilaPantallas.setCurrentWidget(SiguientePantalla)


    def MostrarSobrepantalla(self, NombrePantalla):
        if NombrePantalla not in self.Sobrepantallas:
            return
        if NombrePantalla in self.SobrepantallasActuales:
            return
        SobrepantallaNueva = self.Sobrepantallas[NombrePantalla]
        self.SobrepantallasActuales.append(NombrePantalla)
        print("NEXT:", SobrepantallaNueva)

        SobrepantallaNueva.show()
        SobrepantallaNueva.raise_()


    def BorrarPantalla(self, NombrePantalla):
        if NombrePantalla not in self.Pantallas:
            return
        Pantalla = self.Pantallas.pop(NombrePantalla)

        self.FilaPantallas.removeWidget(Pantalla)
        Pantalla.deleteLater()


    def RestaurarPantalla(self, NombrePantalla):
        if NombrePantalla not in self.Pantallas:
            return
        Pantalla = self.Pantallas[NombrePantalla]
        #Si la pantalla tiene un metodo reset, ejecutarlo para restaurar su estado inicial
        if hasattr(Pantalla, "reset"):
            Pantalla.reset()

    #Sacan pantallas de la memoria
    def QuitarSobrepantalla(self, NombrePantalla):
        if NombrePantalla not in self.Sobrepantallas:
            return
        if NombrePantalla not in self.SobrepantallasActuales:
            return
        
        Sobrepantalla = self.Sobrepantallas.pop(NombrePantalla)
        self.SobrepantallasActuales.remove(NombrePantalla)

        Sobrepantalla.deleteLater()

    #Sacan pantallas de la memoria
    def LimpiarPantallas(self):
        #Limpiar pantallas visibles y ejecutar eventos de salida
        for Pantalla in reversed(range(self.FilaPantallas.count())):
            widget = self.FilaPantallas.widget(Pantalla)

            self.FilaPantallas.removeWidget(widget)
            widget.deleteLater()
        #Limpiar sobrepantallas visibles y ejecutar eventos de salida
        for Nombre in self.SobrepantallasActuales:
            self.Sobrepantallas[Nombre].deleteLater()

        self.current_overlay = None
        
        #Limpiar referencias a pantallas y sobrepantallas
        self.Pantallas.clear()
        self.Sobrepantallas.clear()
        self.SobrepantallasActuales.clear()


    def SincronizarSobrepantallas(self):
        if len(self.SobrepantallasActuales) == 0:
            return
        for nombre in self.SobrepantallasActuales:
            Sobrepantalla = self.Sobrepantallas.get(nombre)
            if Sobrepantalla is None:
                continue
            if hasattr(Sobrepantalla, "CentrarPantalla"):
                Sobrepantalla.CentrarPantalla()
            if hasattr(Sobrepantalla, "CentrarComponentes"):
                Sobrepantalla.CentrarComponentes()

    def SincronizarPantallas(self):
        if self.FilaPantallas.currentWidget() is None:
            return
        PantallaActual = self.FilaPantallas.currentWidget()
        if hasattr(PantallaActual, "CentrarComponentes"):
            PantallaActual.CentrarComponentes()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.SincronizarSobrepantallas()
        self.SincronizarPantallas()
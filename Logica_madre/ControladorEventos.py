from PyQt5.QtWidgets import QWidget

class ControladorEventos:
    def Entrada(self):
        pass

    def Salida(self):
        pass

    def PropagarEntrada(self):
        #Ejecutar evento de entrada de la pagina actual
        if hasattr(self, "Entrada"):
            self.Entrada()
        #Propagar evento de entrada a los hijos que tengan el metodo Entrada
        for child in self.findChildren(QWidget):
            if hasattr(child, "Entrada"):
                child.Entrada()

    def PropagarSalida(self):
        #Ejecutar evento de salida de la pagina actual
        if hasattr(self, "Salida"):
            self.Salida()
        #Propagar evento de salida a los hijos que tengan el metodo Salida
        for child in self.findChildren(QWidget):
            if hasattr(child, "Salida"):
                child.Salida()
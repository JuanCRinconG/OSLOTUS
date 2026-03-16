import tkinter as tk
from PaginaBootup import PaginaBootUp

#definir clase de aplicacion y sus atributos, aqui van los atajos de teclado y teclas
class SistemaOperativoLotus(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema operativo LOTUS")
        self.geometry("600x400")
        self.attributes('-fullscreen', True)
        
        #Alterar funciones del teclado para que hagan cosas especificas en la pagina, usando funciones y vinculandolas
        def PantallaCompleta(event=None):
            if self.attributes("-fullscreen"):
                self.attributes("-fullscreen", False)
            else:
                self.attributes("-fullscreen", True)

        self.bind("<Escape>", PantallaCompleta)

        # Contenedor principal para multiples mini paginas (procesos)
        self.container = tk.Frame(self, bg="black")
        self.container.pack(fill="both", expand=True)

        # Diccionario en el que se incluyen las paginas actuales o procesos
        self.Paginas = {}
        
        #Contador para definir que paginas estan en uso, y mostrador de pagina
        self.PaginasActivas = []
        self.MostrarPagina(PaginaBootUp, "both", True)


    def MostrarPagina(self, PaginaElegida, Orientacion=None, Expandir=None):
        PaginaNueva = PaginaElegida(self.container, self)
        self.PaginasActivas.append(PaginaNueva)
        PaginaNueva.pack(fill=Orientacion, expand=Expandir)

    def SobreponerPagina(self, PaginaElegida, CordenadaX=None, CordenadaY=None, Ancla=None):
        PaginaNueva = PaginaElegida(self.container, self)
        self.PaginasActivas.append(PaginaNueva)
        PaginaNueva.place(relx=CordenadaX, rely=CordenadaY, anchor=Ancla)
    
    def DestruirPagina(self, PaginaEspecifica=None):
        if len(self.PaginasActivas) > 0:
            if PaginaEspecifica:
                PaginaEspecifica.destroy()
                self.PaginasActivas.remove(PaginaEspecifica)

    def LimpiarPantalla(self):
        for i in self.PaginasActivas:
            i.destroy()
        self.PaginasActivas = []

        

        




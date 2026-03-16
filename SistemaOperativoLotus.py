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
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Diccionario en el que se incluyen las paginas actuales o procesos
        self.Paginas = {}
        
        #Contador para definir que pagina esta en uso, y mostrador de pagina
        self.PaginaActual = None
        self.MostrarPagina(PaginaBootUp)

    def MostrarPagina(self, frame_class):
        PaginaNueva = frame_class(self.container, self)
        self.PaginaActual = PaginaNueva
        self.PaginaActual.pack(fill="both", expand=True)
    
    def DestruirPagina(self):
        if self.PaginaActual is not None:
            self.PaginaActual.destroy()
            self.PaginaActual = None

        

        




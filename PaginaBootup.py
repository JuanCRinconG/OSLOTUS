import tkinter as tk
from PaginaUsuario import PaginaUsuario

class PaginaBootUp(tk.Frame):
    def __init__(self, pariente, controller):
        super().__init__(pariente)
        self.controller = controller
        
        #Elementos que van adentro de la pagina
        LabelBoot = tk.Label(self, text='Bienvenido al sistema')
        BotonUsuario = tk.Button(self, text='Iniciar sesion', command=lambda: controller.MostrarPagina(PaginaUsuario))

        LabelBoot.pack(pady=10)
        BotonUsuario.pack(pady=10)



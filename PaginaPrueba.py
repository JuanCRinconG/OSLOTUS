import tkinter as tk
from PaginaUsuario import PaginaUsuario

class PaginaBootUp(tk.Frame):
    def __init__(self, pariente, controller):
        super().__init__(pariente, bg="#db8d34", highlightthickness=2, highlightbackground="white")
        self.controller = controller
        
        #Elementos que van adentro de la pagina
        LabelBoot = tk.Label(self, text='Bienvenido al sistema')
        BotonUsuario = tk.Button(self, text='Iniciar sesion', command=lambda: controller.SobreponerPagina(PaginaUsuario, 0.5, 0.5, "center"))

        LabelBoot.pack(pady=10)
        BotonUsuario.pack(pady=10)
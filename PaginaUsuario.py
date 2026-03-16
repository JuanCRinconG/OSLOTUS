import tkinter as tk

class PaginaUsuario(tk.Frame):
    def __init__(self, pariente, controller):
        super().__init__(pariente)
        self.controller = controller
        
        #Elementos que van adentro de la pagina
        LabelUsuario = tk.Label(self, text='Elegir Usuario')
        BotonUsuario = tk.Button(self, text='Usuario1', command=self.destroy)

        LabelUsuario.pack(pady=10)
        BotonUsuario.pack(pady=10)
import tkinter as tk

class PaginaUsuario(tk.Frame):
    def __init__(self, pariente, controller):
        super().__init__(pariente, bg="#3498db", highlightthickness=2, highlightbackground="white")
        self.controller = controller
        self.config(width=300, height=200)
        self.pack_propagate(False)
        
        #Elementos que van adentro de la pagina
        LabelUsuario = tk.Label(self, text='Elegir Usuario')
        BotonUsuario = tk.Button(self, text='Usuario1', command=lambda: controller.LimpiarPantalla())

        LabelUsuario.pack(pady=10)
        BotonUsuario.pack(pady=10)
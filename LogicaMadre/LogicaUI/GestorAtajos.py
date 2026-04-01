#Es el gestor de atajos de la clase principal lotus, aqui se podrian
#Poner atajos del teclado y no llenar la clase principal con logica de atajos

# LogicaOS/GestorAtajos.py

from PyQt5.QtWidgets import QShortcut #Escucha combinaciones de teclas
from PyQt5.QtGui import QKeySequence #el atajo o clave que se va a escuchar, como Ctrl+Q o Space


class GestorAtajos:
    def __init__(self, ventana, gestor_pantallas): #constructor,metodo que ejecuta cuando creas el objeto
        self.ventana = ventana
        self.gestor_pantallas = gestor_pantallas

        # Diccionario de atajos
        self.atajos = {
            "Ctrl+Q": self.salir,
            "Ctrl+P": self.abrir_pomodoro,
            "Ctrl+A": self.abrir_admin_tareas,
            "Space": self.test_espacio
        }

        self.configurar()#Llama a la funcion configurar para activar los atajos 

    def configurar(self):
        for combinacion, funcion in self.atajos.items():#Bucle que itera en self.atajos, obteniendo la combinacion de teclas y la funcion asociada a esa combinacion
            shortcut = QShortcut(QKeySequence(combinacion), self.ventana)#Qshort.. clase, Qkeysequence.. interprete, 
            shortcut.activated.connect(funcion) 

    # FUNCIONES

    def salir(self):
        print("Saliendo...")
        self.ventana.close()

    def abrir_pomodoro(self):
        print("Abriendo Pomodoro ")
        self.gestor_pantallas.MostrarPantalla("Pomodoro")

    def abrir_admin_tareas(self):
        print("Abriendo Administrador ")
        self.gestor_pantallas.MostrarSobrepantalla("Administrador")

    def test_espacio(self):
        print("Espacio presionado")
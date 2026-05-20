# Es el gestor de atajos de la clase principal lotus

from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
from LogicaBash import EjecutorBash, TaskMGR_ScriptRuta


class GestorAtajos:
    def __init__(self, ventana, gestor_pantallas):
        self.ventana = ventana
        self.gestor_pantallas = gestor_pantallas
        self._ejecutor = EjecutorBash()

        self.atajos = {
            "Escape": self.pantalla_completa,
            "Ctrl+Q": self.salir,
            "Ctrl+P": self.abrir_pomodoro,
            "Ctrl+A": self.abrir_admin_tareas,
            "Space": self.test_espacio,
        }

        self.configurar()

    def configurar(self):
        for combinacion, funcion in self.atajos.items():
            shortcut = QShortcut(QKeySequence(combinacion), self.ventana)
            shortcut.activated.connect(funcion)

    def pantalla_completa(self):
        if self.ventana.isFullScreen():
            self.ventana.showNormal()
        else:
            self.ventana.showFullScreen()

    def salir(self):
        print("Saliendo...")
        self.ventana.close()

    def abrir_pomodoro(self):
        print("Abriendo Pomodoro ")

    def abrir_admin_tareas(self):
        print("Abriendo Administrador ")
        self._ejecutor.ejecutar_async(TaskMGR_ScriptRuta)

    def test_espacio(self):
        print("Espacio presionado")

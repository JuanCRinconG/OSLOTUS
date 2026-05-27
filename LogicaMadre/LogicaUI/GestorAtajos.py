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
        # 1. Verificar si la sobrepantalla ya está registrada y es visible
        if hasattr(self.gestor_pantallas, 'Sobrepantallas') and "MenuPomodoro" in self.gestor_pantallas.Sobrepantallas:
            sobrepantalla = self.gestor_pantallas.Sobrepantallas["MenuPomodoro"]
            if sobrepantalla.isVisible():
                print("DEBUG: Pomodoro detectado abierto. Cerrando vía atajo...")
                self.gestor_pantallas.OcultarSobrepantalla("MenuPomodoro")
                return

        # 2. Si no estaba abierta o visible, procedemos a abrirla normalmente
        print("Abriendo Pomodoro desde el Gestor de Atajos Global...")
        from PantallasSistema.Pantallas.PantallaPomodoro import PantallaPomodoro
        
        controlador = None
        if hasattr(self.ventana, 'Controlador'):
            controlador = self.ventana.Controlador
        elif hasattr(self.gestor_pantallas, 'Controlador'):
            controlador = self.gestor_pantallas.Controlador

        try:
            self.gestor_pantallas.AgregarSobrepantalla("MenuPomodoro", PantallaPomodoro, controlador, self.gestor_pantallas)
            self.gestor_pantallas.MostrarSobrepantalla("MenuPomodoro")
            print("DEBUG: Sobrepantalla Pomodoro renderizada con éxito.")
        except Exception as e:
            print(f"ERROR al renderizar Pomodoro desde el Gestor de Atajos: {e}")

    def abrir_admin_tareas(self):
        print("Abriendo Administrador ")
        self._ejecutor.ejecutar_async(TaskMGR_ScriptRuta)

    def test_espacio(self):
        print("Espacio presionado")

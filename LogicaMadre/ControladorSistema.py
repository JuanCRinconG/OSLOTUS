# Es el controlador de la logica madre del sistema
# Se encarga de controlar y comunicar la logica del Sistema Operativo
# Con la logica de la Interfaz de Usuario

from LogicaMadre.LogicaOS import GestorSesion, GestorUsuarios, ModeloUsuario
from PyQt5.QtCore import QTimer
from LogicaMadre.LogicaOS.GestorPomodoro import GestorPomodoro

class ControladorSistema:
    def __init__(self, gestor_pantallas):
        # 1. Unificamos la referencia al gestor
        self.Gestor = gestor_pantallas
        self.gestor_pantallas = gestor_pantallas
        
        # 2. Inicialización de servicios OS
        self.gestor_usuarios = GestorUsuarios()
        self.gestor_sesion = GestorSesion()
        
        # 3. Inicialización Pomodoro
        self.gestor_pomodoro = GestorPomodoro()
        self.timer = QTimer()
        self.timer.timeout.connect(self._ciclo_pomodoro)

    # --- MÉTODOS DE NAVEGACIÓN ---
    def IrPantalla(self, NombrePantalla):
        self.Gestor.MostrarPantalla(NombrePantalla)

    def IrSobrepantalla(self, NombreSobrepantalla):
        self.Gestor.MostrarSobrepantalla(NombreSobrepantalla)

    def BorrarTodasPantallas(self):
        self.Gestor.BorrarTodasPantallas()

    # --- MÉTODOS DE USUARIOS ---
    def obtener_usuarios(self) -> list[ModeloUsuario]:
        return self.gestor_usuarios.obtener_todos()

    def crear_usuario(self, nombre: str, avatar: str | None = None, pin: str | None = None) -> ModeloUsuario:
        return self.gestor_usuarios.crear_usuario(nombre, avatar, pin)

    def iniciar_sesion(self, usuario_id: str, pin_ingresado: str | None = None) -> bool:
        usuario = self.gestor_usuarios.obtener_por_id(usuario_id)
        if usuario is None:
            return False
        if usuario.pin is not None and not usuario.verificar_pin(pin_ingresado or ""):
            return False
        self.gestor_sesion.iniciar_sesion(usuario)
        self.gestor_usuarios.registrar_acceso(usuario_id)
        return True

    def cerrar_sesion(self) -> None:
        self.gestor_sesion.cerrar_sesion()

    def usuario_activo(self) -> ModeloUsuario | None:
        return self.gestor_sesion.usuario_activo

    # --- MÉTODOS POMODORO ---
    def iniciar_pomodoro(self, minutos, apps_seleccionadas):
        self.gestor_pomodoro.configurar_sesion(minutos, apps_seleccionadas)
        self.timer.start(1000) 
        self.gestor_pantallas.OcultarSobrepantalla("MenuPomodoro")

    def _ciclo_pomodoro(self):
        self.gestor_pomodoro.tiempo_restante_segundos -= 1
        print(f"Tiempo Pomodoro restante: {self.gestor_pomodoro.tiempo_restante_segundos}s") 

        if self.gestor_pomodoro.tiempo_restante_segundos <= 0:
            self.finalizar_pomodoro()

    def finalizar_pomodoro(self):
        self.timer.stop()
        self.gestor_pomodoro.finalizar_sesion()
        print("Sesión Pomodoro finalizada.")

    def intentar_abrir_aplicacion(self, app_nombre):
        if not self.gestor_pomodoro.permiso_concedido(app_nombre):
            print(f"Bloqueo Pomodoro: No te distraigas, {app_nombre} no está permitida.")
            return False
            
        print(f"Abriendo {app_nombre}...")
        return True
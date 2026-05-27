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
        
        # NUEVO: Mostrar el widget en la barra de tareas inmediatamente
        # Buscamos la pantalla principal para acceder a la barra
        pantalla_principal = self.gestor_pantallas.Pantallas.get("PantallaPrincipal")
        if pantalla_principal and hasattr(pantalla_principal, "barra_tareas"):
            # Pasamos los segundos iniciales formateados
            pantalla_principal.barra_tareas.mostrar_mini_pomodoro(f"{minutos}:00")

    def _ciclo_pomodoro(self):
        self.gestor_pomodoro.tiempo_restante_segundos -= 1
        segundos_totales = self.gestor_pomodoro.tiempo_restante_segundos
        
        # Formatear MM:SS
        minutos = segundos_totales // 60
        segundos = segundos_totales % 60
        tiempo_texto = f"{minutos:02d}:{segundos:02d}"
        
        print(f"Tiempo Pomodoro restante: {tiempo_texto}") 

        # NUEVO: Actualizar el texto en la barra de tareas en tiempo real
        pantalla_principal = self.gestor_pantallas.Pantallas.get("PantallaPrincipal")
        if pantalla_principal and hasattr(pantalla_principal, "barra_tareas"):
            pantalla_principal.barra_tareas.actualizar_mini_pomodoro(tiempo_texto)

        if segundos_totales <= 0:
            self.finalizar_pomodoro()

    def finalizar_pomodoro(self):
        self.timer.stop()
        self.gestor_pomodoro.finalizar_sesion()
        print("Sesión Pomodoro finalizada.")
        
        # NUEVO: Ocultar de la barra al terminar
        pantalla_principal = self.gestor_pantallas.Pantallas.get("PantallaPrincipal")
        if pantalla_principal and hasattr(pantalla_principal, "barra_tareas"):
            pantalla_principal.barra_tareas.ocultar_mini_pomodoro()

    def intentar_abrir_aplicacion(self, app_nombre):
        if not self.gestor_pomodoro.permiso_concedido(app_nombre):
            print(f"Bloqueo Pomodoro: No te distraigas, {app_nombre} no está permitida.")
            return False
            
        print(f"Abriendo {app_nombre}...")
        return True
    
    def pausar_pomodoro(self):
        # El QTimer real es self.timer
        if self.timer.isActive():
            self.timer.stop()
            print("POMODORO: Temporizador pausado.")
            return True  # Retorna True si quedó pausado
        else:
            self.timer.start(1000)
            print("POMODORO: Temporizador reanudado.")
            return False  # Retorna False si volvió a correr

    def reiniciar_pomodoro(self):
        self.timer.stop()
        self.gestor_pomodoro.tiempo_restante_segundos = 1500
        print("POMODORO: Temporizador restablecido.")
        
        # NUEVO: Ocultar el widget de la barra
        pantalla_principal = self.gestor_pantallas.Pantallas.get("PantallaPrincipal")
        if pantalla_principal and hasattr(pantalla_principal, "barra_tareas"):
            pantalla_principal.barra_tareas.ocultar_mini_pomodoro()
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
    def iniciar_pomodoro(self, minutos_enfoque, minutos_descanso, apps_permitidas):
        """Maneja el ciclo de vida del temporizador alternando enfoque y receso."""
        print(f"LOGICA: Iniciando Pomodoro. Enfoque: {minutos_enfoque}min, Descanso: {minutos_descanso}min")
        
        self.pomodoro_activo = True
        self.apps_permitidas = apps_permitidas
        self.minutos_descanso = minutos_descanso
        
        # Guardamos los segundos totales iniciales (Fase inicial: Enfoque)
        self.segundos_restantes = minutos_enfoque * 60
        self.estado_pomodoro = "Enfoque"  # Puede cambiar a "Receso"
        
        # Configurar el QTimer del sistema para que descuente cada 1000ms (1 segundo)
        if not hasattr(self, 'timer_pomodoro') or self.timer_pomodoro is None:
            from PyQt5.QtCore import QTimer
            self.timer_pomodoro = QTimer()
            self.timer_pomodoro.timeout.connect(self.descontar_segundo_pomodoro)
            
        self.timer_pomodoro.start(1000)

    def descontar_segundo_pomodoro(self):
        if self.segundos_restantes > 0:
            self.segundos_restantes -= 1
            
            mins, segs = divmod(self.segundos_restantes, 60)
            tiempo_str = f"{mins:02d}:{segs:02d}"
            
            gestor = self.gestor_pantallas
            
            # 1. ACTUALIZACIÓN DE LA SOBREPANTALLA FLOTANTE
            if "MenuPomodoro" in gestor.Sobrepantallas:
                ventana_ui = gestor.Sobrepantallas["MenuPomodoro"]
                if ventana_ui.isVisible():
                    ventana_ui.actualizar_cronometro(tiempo_str, self.estado_pomodoro)
                    
            # 2. RECURSIVIDAD CON LA BARRA DE TAREAS (Hace aparecer y cambiar el botón a azul)
            if "PantallaPrincipal" in gestor.Pantallas:
                escritorio = gestor.Pantallas["PantallaPrincipal"]
                if hasattr(escritorio, "barra_tareas") and escritorio.barra_tareas:
                    # Invocamos la función modificada pasándole el tiempo y la fase
                    escritorio.barra_tareas.actualizar_mini_pomodoro(tiempo_str, self.estado_pomodoro)
        else:
            # El tiempo llegó a 0: Cambiar de Fase (Enfoque <-> Receso)
            self.alternar_fase_pomodoro()

    def alternar_fase_pomodoro(self):
        """Intercambia el estado entre la fase de concentración y el receso."""
        if self.estado_pomodoro == "Enfoque":
            print("LOGICA: Tiempo de enfoque finalizado. Iniciando receso...")
            self.estado_pomodoro = "Receso"
            self.segundos_restantes = self.minutos_descanso * 60
            # Aquí puedes quitar restricciones de Firewall / bloqueo temporalmente si lo deseas
        else:
            print("LOGICA: Receso finalizado. Volviendo a modo Enfoque...")
            self.estado_pomodoro = "Enfoque"
            self.timer_pomodoro.stop()
            self.pomodoro_activo = False
            # Notificar al usuario mediante un QMessageBox o señal acústica

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

    def intentar_abrir_aplicacion(self, nombre_app):
        """
        Evalúa si una aplicación tiene permitido ejecutarse.
        Retorna True si se puede abrir, False si debe bloquearse.
        """
        # Si el Pomodoro no está corriendo, no hay ninguna restricción
        if not hasattr(self, 'pomodoro_activo') or not self.pomodoro_activo:
            return True

        # Si el Pomodoro está activo pero estamos en tiempo de RECESO, permitimos todo
        if hasattr(self, 'estado_pomodoro') and self.estado_pomodoro == "Receso":
            print(f"POMODORO: En tiempo de descanso. Se permite abrir {nombre_app}")
            return True

        # Si estamos en tiempo de ENFOQUE, verificamos de manera estricta la lista de permitidas
        if hasattr(self, 'apps_permitidas') and self.apps_permitidas is not None:
            if nombre_app in self.apps_permitidas:
                print(f"POMODORO: {nombre_app} está en la lista de aplicaciones permitidas.")
                return True
            else:
                print(f"POMODORO BLOQUEO: {nombre_app} NO está permitida durante el enfoque.")
                return False

        return True
    
    def pausar_pomodoro(self):
        """
        Alterna el estado de pausa del temporizador activo.
        Retorna True si quedó pausado, False si se reanudó.
        """
        if not hasattr(self, 'timer_pomodoro') or self.timer_pomodoro is None:
            print("POMODORO LOGICA: No hay un temporizador activo para pausar.")
            return False

        # Si el temporizador está corriendo, lo detenemos (Pausa)
        if self.timer_pomodoro.isActive():
            self.timer_pomodoro.stop()
            print("POMODORO LOGICA: Temporizador pausado de forma segura.")
            return True
        else:
            # Si estaba detenido, lo reactivamos (Reanudar)
            self.timer_pomodoro.start(1000)
            print("POMODORO LOGICA: Temporizador reanudado.")
            return False

    def reiniciar_pomodoro(self):
        self.timer.stop()
        self.gestor_pomodoro.tiempo_restante_segundos = 1500
        print("POMODORO: Temporizador restablecido.")
        
        # NUEVO: Ocultar el widget de la barra
        pantalla_principal = self.gestor_pantallas.Pantallas.get("PantallaPrincipal")
        if pantalla_principal and hasattr(pantalla_principal, "barra_tareas"):
            pantalla_principal.barra_tareas.ocultar_mini_pomodoro()
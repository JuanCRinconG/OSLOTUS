# LogicaMadre/LogicaOS/GestorPomodoro.py

class GestorPomodoro:
    def __init__(self):
        self.activo = False
        self.apps_permitidas = []
        self.tiempo_restante_segundos = 0

    def configurar_sesion(self, minutos, apps):
        """Define las reglas de la sesión actual."""
        self.activo = True
        self.apps_permitidas = apps
        self.tiempo_restante_segundos = minutos * 60

    def finalizar_sesion(self):
        """Limpia las restricciones."""
        self.activo = False
        self.apps_permitidas = []
        self.tiempo_restante_segundos = 0

    def permiso_concedido(self, app_nombre):
        """Valida si una app puede ejecutarse en este momento."""
        if not self.activo:
            return True # Si no hay pomodoro, todo está permitido
        
        return app_nombre in self.apps_permitidas
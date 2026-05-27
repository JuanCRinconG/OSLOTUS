"""Estado de sesión en memoria (usuario activo)."""

from LogicaMadre.LogicaOS.ModeloUsuario import ModeloUsuario
from LogicaMadre.LogicaOS.GestorSesionUsuario import GestorSesionUsuario 


class GestorSesion:
    def __init__(self):
        self._usuario_activo: ModeloUsuario | None = None
        self.sesion_usuario: GestorSesionUsuario | None = None

    def iniciar_sesion(self, usuario: ModeloUsuario) -> None:
        self._usuario_activo = usuario
        self.sesion_usuario = GestorSesionUsuario(usuario.id)

    def cerrar_sesion(self) -> None:
        self._usuario_activo = None
        self.sesion_usuario = None  

    @property
    def usuario_activo(self) -> ModeloUsuario | None:
        return self._usuario_activo

    def hay_sesion_activa(self) -> bool:
        return self._usuario_activo is not None

"""Estado de sesión en memoria (usuario activo)."""

from LogicaMadre.LogicaOS.ModeloUsuario import ModeloUsuario


class GestorSesion:
    def __init__(self):
        self._usuario_activo: ModeloUsuario | None = None

    def iniciar_sesion(self, usuario: ModeloUsuario) -> None:
        self._usuario_activo = usuario

    def cerrar_sesion(self) -> None:
        self._usuario_activo = None

    @property
    def usuario_activo(self) -> ModeloUsuario | None:
        return self._usuario_activo

    def hay_sesion_activa(self) -> bool:
        return self._usuario_activo is not None

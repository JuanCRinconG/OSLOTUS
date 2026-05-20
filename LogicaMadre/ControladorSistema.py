# Es el controlador de la logica madre del sistema
# Se encarga de controlar y comunicar la logica del Sistema Operativo
# Con la logica de la Interfaz de Usuario

from LogicaMadre.LogicaOS import GestorSesion, GestorUsuarios, ModeloUsuario


class ControladorSistema:
    def __init__(self, GestorPantallas):
        self.Gestor = GestorPantallas
        self.gestor_usuarios = GestorUsuarios()
        self.gestor_sesion = GestorSesion()

    def IrPantalla(self, NombrePantalla):
        self.Gestor.MostrarPantalla(NombrePantalla)

    def IrSobrepantalla(self, NombreSobrepantalla):
        self.Gestor.MostrarSobrepantalla(NombreSobrepantalla)

    def BorrarTodasPantallas(self):
        self.Gestor.BorrarTodasPantallas()

    def obtener_usuarios(self) -> list[ModeloUsuario]:
        return self.gestor_usuarios.obtener_todos()

    def crear_usuario(
        self,
        nombre: str,
        avatar: str | None = None,
        pin: str | None = None,
    ) -> ModeloUsuario:
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

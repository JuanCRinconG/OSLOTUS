from PyQt5.QtCore import Qt
from PantallasSistema.Componentes import ComponentesElegirUsuario
from PantallasSistema import PantallaBase
from Recursos import PC_AzulOSLotus


class PantallaElegirUsuario(PantallaBase):
    def __init__(self, Controlador=None):
        super().__init__()
        self.Controlador = Controlador

        self.componentes = ComponentesElegirUsuario(self)
        self.componentes.IngresarSistema.connect(self.IrPantallaPrincipal)
        self.componentes.solicitar_crear_usuario.connect(self._al_crear_usuario)

        self.setStyleSheet(f"""background-color:{PC_AzulOSLotus}; border: 2px solid black;""")
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.hide()

    def Entrada(self):
        if self.Controlador:
            usuarios = self.Controlador.obtener_usuarios()
            self.componentes.mostrar_usuarios(usuarios, self._al_seleccionar_usuario)
        print("Pantalla elegir usuario entered")

    def Salida(self):
        print("Pantalla elegir usuario exited")

    def _al_seleccionar_usuario(self, usuario_id: str, pin: str) -> bool:
        if not self.Controlador:
            return False
        if self.Controlador.iniciar_sesion(usuario_id, pin or None):
            self.IrPantallaPrincipal()
            return True
        return False

    def _al_crear_usuario(self, nombre: str, pin: str):
        if not self.Controlador:
            return
        self.Controlador.crear_usuario(nombre, avatar=None, pin=pin or None)
        usuarios = self.Controlador.obtener_usuarios()
        self.componentes.mostrar_usuarios(usuarios, self._al_seleccionar_usuario)

    def IrPantallaPrincipal(self):
        if self.Controlador:
            self.Controlador.IrPantalla("PantallaPrincipal")

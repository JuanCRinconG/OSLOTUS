from PyQt5.QtWidgets import QLabel, QMenu, QFileDialog
from PyQt5.QtCore    import Qt
from PyQt5.QtGui     import QPixmap

from PantallasSistema.PantallaBase   import PantallaBase
from PantallasSistema.Componentes    import ComponentesPrincipal, ComponentesBarraTareas
from PantallasSistema.Componentes.ComponentesBarraTareas import ALTURA_BARRA
from LogicaMadre.LogicaOS.GestorSesionUsuario import GestorSesionUsuario


class PantallaPrincipal(PantallaBase):

    def __init__(self, Controlador=None):
        super().__init__()
        self.Controlador = Controlador
        self._sesion_usuario = None
        self._fondo_label = QLabel(self)
        self._fondo_label.setScaledContents(True)

        self.componentes = ComponentesPrincipal(self)
        self.barra_tareas = ComponentesBarraTareas(self)

        self.setStyleSheet("background-color: #1a1a1a; border: none;")
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.hide()

    def CuadrarComponentes(self):
        self._fondo_label.setGeometry(0, 0, self.width(), self.height())
        self.componentes.setGeometry(0, 0, self.width(), self.height() - ALTURA_BARRA)
        self.barra_tareas.CuadrarBarraTareas()

    def Entrada(self):
        self.CuadrarComponentes()

        if self.Controlador:
            usuario = self.Controlador.usuario_activo()
            if usuario:
                self.componentes.label_bienvenida.setText(f"Bienvenido, {usuario.nombre} 👋")
                self._sesion_usuario = GestorSesionUsuario(usuario.id)
                self._cargar_fondo()

        print("Pantalla Principal entered")

    def Salida(self):
        print("Pantalla Principal exited")

    # ── Fondo ─────────────────────────────────────────────────

    def _cargar_fondo(self):
        if not self._sesion_usuario:
            return
        ruta = self._sesion_usuario.obtener("fondo")
        if ruta:
            self._aplicar_fondo(ruta)

    def _aplicar_fondo(self, ruta: str):
        pixmap = QPixmap(ruta)
        if not pixmap.isNull():
            pixmap_escalado = pixmap.scaled(
                self.width(), self.height(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )
            self._fondo_label.setPixmap(pixmap_escalado)
            self._fondo_label.lower()

    # ── Clic derecho ──────────────────────────────────────────

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.setStyleSheet("""
            QMenu {
                background-color: rgba(30, 30, 30, 220);
                color: white;
                border: 1px solid rgba(255,255,255,0.15);
                border-radius: 8px;
                padding: 4px;
            }
            QMenu::item:selected {
                background-color: rgba(39, 169, 245, 0.7);
                border-radius: 4px;
            }
        """)
        accion_fondo = menu.addAction("🖼️  Cambiar fondo de pantalla")
        accion = menu.exec_(event.globalPos())

        if accion == accion_fondo:
            self._elegir_fondo()

    def _elegir_fondo(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self, "Elegir fondo", "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp *.webp)"
        )
        if ruta and self._sesion_usuario:
            self._sesion_usuario.guardar("fondo", ruta)
            self._aplicar_fondo(ruta)
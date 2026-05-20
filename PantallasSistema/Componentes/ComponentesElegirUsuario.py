from __future__ import annotations

from typing import Callable

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal

from Recursos import AnimacionesPyQt5, MixinLayout, PC_Transparente

from PantallasSistema.Componentes._FondoElegirUsuario import _FondoElegirUsuario
from PantallasSistema.Componentes._VistaCarruselUsuarios import _VistaCarruselUsuarios
from PantallasSistema.Componentes._VistaCrearUsuario import _VistaCrearUsuario


class ComponentesElegirUsuario(QWidget, AnimacionesPyQt5, MixinLayout):
    IngresarSistema = pyqtSignal()
    usuario_seleccionado = pyqtSignal(str)
    solicitar_crear_usuario = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.inicializar_layout(self)
        self.setStyleSheet(f"background-color: {PC_Transparente}; border-radius: 2px;")

        self._on_seleccion: Callable[[str, str], bool] | None = None

        self._fondo = _FondoElegirUsuario(self)
        self._vista_carrusel = _VistaCarruselUsuarios(self)
        self._vista_crear = _VistaCrearUsuario(self)
        self._vista_crear.hide()

        self._vista_carrusel.raise_()
        self._vista_crear.raise_()

        self._vista_carrusel.usuario_ingresado.connect(self._al_intentar_ingresar)
        self._vista_carrusel.crear_nuevo.connect(self._mostrar_crear)
        self._vista_crear.confirmar.connect(self._al_confirmar_crear)
        self._vista_crear.cancelar.connect(self._mostrar_carrusel)

    def mostrar_usuarios(
        self,
        usuarios,
        on_seleccion: Callable[[str, str], bool] | None = None,
    ):
        self._on_seleccion = on_seleccion
        self._vista_carrusel.cargar_usuarios(usuarios)
        self._mostrar_carrusel()

    def mostrar_error_pin(self):
        self._vista_carrusel.mostrar_error_pin()

    def _al_intentar_ingresar(self, usuario_id: str, pin: str):
        self.usuario_seleccionado.emit(usuario_id)
        if self._on_seleccion:
            exito = self._on_seleccion(usuario_id, pin)
            if exito is False:
                self.mostrar_error_pin()

    def _mostrar_crear(self):
        self._vista_carrusel.hide()
        self._vista_crear.limpiar()
        self._vista_crear.show()

    def _mostrar_carrusel(self):
        self._vista_crear.hide()
        self._vista_carrusel.show()

    def _al_confirmar_crear(self, nombre: str, pin: str):
        self.solicitar_crear_usuario.emit(nombre, pin)

    def cuadrar(self):
        w = self.width()
        h = self.height()
        if w < 1 or h < 1:
            return
        for sub in (self._fondo, self._vista_carrusel, self._vista_crear):
            sub.setGeometry(0, 0, w, h)

    def CuadrarComponentesElegirUsuario(self):
        self.cuadrar()

    def showEvent(self, event):
        super().showEvent(event)
        print("Componente elegir usuario entered")

    def hideEvent(self, event):
        super().hideEvent(event)
        print("Componente elegir usuario exited")

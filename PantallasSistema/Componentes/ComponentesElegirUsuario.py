from __future__ import annotations

from typing import Callable

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal

from Recursos import AnimacionesPyQt5, MixinLayout, PC_Transparente

from PantallasSistema.Componentes._FondoElegirUsuario import _FondoElegirUsuario
from PantallasSistema.Componentes._VistaListaUsuarios import _VistaListaUsuarios
from PantallasSistema.Componentes._VistaCrearUsuario import _VistaCrearUsuario


class ComponentesElegirUsuario(QWidget, AnimacionesPyQt5, MixinLayout):
    IngresarSistema = pyqtSignal()
    usuario_seleccionado = pyqtSignal(str)
    solicitar_crear_usuario = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.inicializar_layout(self)
        self.setStyleSheet(f"background-color: {PC_Transparente}; border-radius: 2px;")

        self._on_seleccion: Callable[[str], None] | None = None

        self._fondo = _FondoElegirUsuario(self)
        self._vista_lista = _VistaListaUsuarios(self)
        self._vista_crear = _VistaCrearUsuario(self)
        self._vista_crear.hide()

        self._vista_lista.raise_()
        self._vista_crear.raise_()

        self._vista_lista.usuario_seleccionado.connect(self._al_seleccionar_usuario)
        self._vista_lista.crear_nuevo.connect(self._mostrar_crear)
        self._vista_crear.confirmar.connect(self._al_confirmar_crear)
        self._vista_crear.cancelar.connect(self._mostrar_lista)

    def mostrar_usuarios(self, usuarios, on_seleccion: Callable[[str], None] | None = None):
        self._on_seleccion = on_seleccion
        self._vista_lista.cargar_usuarios(usuarios)
        self._mostrar_lista()

    def _al_seleccionar_usuario(self, usuario_id: str):
        self.usuario_seleccionado.emit(usuario_id)
        if self._on_seleccion:
            self._on_seleccion(usuario_id)

    def _mostrar_crear(self):
        self._vista_lista.hide()
        self._vista_crear.limpiar()
        self._vista_crear.show()

    def _mostrar_lista(self):
        self._vista_crear.hide()
        self._vista_lista.show()

    def _al_confirmar_crear(self, nombre: str, pin: str):
        self.solicitar_crear_usuario.emit(nombre, pin)

    def cuadrar(self):
        w = self.width()
        h = self.height()
        if w < 1 or h < 1:
            return
        for sub in (self._fondo, self._vista_lista, self._vista_crear):
            sub.setGeometry(0, 0, w, h)

    def CuadrarComponentesElegirUsuario(self):
        self.cuadrar()

    def showEvent(self, event):
        super().showEvent(event)
        print("Componente elegir usuario entered")

    def hideEvent(self, event):
        super().hideEvent(event)
        print("Componente elegir usuario exited")

"""Carrusel de usuarios con navegación por flechas y PIN en la tarjeta."""

from __future__ import annotations

from typing import TYPE_CHECKING

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QPushButton, QWidget

from Recursos import (
    DR_Carrusel_Boton_Nuevo_Alto,
    DR_Carrusel_Boton_Nuevo_Ancho,
    DR_Carrusel_Boton_Nuevo_Y,
    DR_Carrusel_Flecha_H,
    DR_Carrusel_Flecha_W,
    DR_Carrusel_Flecha_X_Derecha,
    DR_Carrusel_Flecha_X_Izquierda,
    DR_Carrusel_Flecha_Y,
    DR_Carrusel_Tarjeta_H,
    DR_Carrusel_Tarjeta_W,
    DR_Carrusel_Tarjeta_Y,
    GothicNormal,
    MixinLayout,
    PC_AzulOSLotus,
    PC_Blanco,
    PC_Transparente,
)

from PantallasSistema.Componentes._TarjetaUsuario import _TarjetaUsuario

if TYPE_CHECKING:
    from LogicaMadre.LogicaOS.ModeloUsuario import ModeloUsuario

_ESTILO_FLECHA = f"""
QPushButton {{
    color: {PC_Blanco};
    background-color: rgba(0, 0, 0, 0.25);
    border: 2px solid rgba(255, 255, 255, 0.6);
    border-radius: 12px;
    font-size: 28px;
    font-weight: bold;
}}
QPushButton:hover {{
    background-color: {PC_AzulOSLotus};
}}
"""

_ESTILO_NUEVO = f"""
QPushButton {{
    color: {PC_Blanco};
    background-color: rgba(0, 0, 0, 0.35);
    border: 2px solid {PC_Blanco};
    border-radius: 8px;
    padding: 10px 20px;
}}
QPushButton:hover {{
    background-color: {PC_AzulOSLotus};
}}
"""


class _VistaCarruselUsuarios(QWidget, MixinLayout):
    usuario_ingresado = pyqtSignal(str, str)
    crear_nuevo = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(f"background-color: {PC_Transparente};")
        self.inicializar_layout(self)

        self._usuarios: list[ModeloUsuario] = []
        self._indice_actual = 0

        self._tarjeta = _TarjetaUsuario(self)
        self._boton_izquierda = QPushButton("<", self)
        self._boton_derecha = QPushButton(">", self)
        self._boton_nuevo_usuario = QPushButton("+ Nuevo usuario", self)

        for boton in (self._boton_izquierda, self._boton_derecha):
            boton.setStyleSheet(_ESTILO_FLECHA)
            boton.setCursor(Qt.PointingHandCursor)

        self._boton_nuevo_usuario.setFont(GothicNormal)
        self._boton_nuevo_usuario.setStyleSheet(_ESTILO_NUEVO)
        self._boton_nuevo_usuario.setCursor(Qt.PointingHandCursor)

        self._boton_izquierda.clicked.connect(self._usuario_anterior)
        self._boton_derecha.clicked.connect(self._usuario_siguiente)
        self._tarjeta.ingresar.connect(self._al_intentar_ingresar)
        self._boton_nuevo_usuario.clicked.connect(self.crear_nuevo.emit)

    def cargar_usuarios(self, usuarios: list[ModeloUsuario]):
        self._usuarios = list(usuarios)
        self._indice_actual = 0
        self._actualizar_tarjeta()

    def _actualizar_tarjeta(self):
        if not self._usuarios:
            self._tarjeta.hide()
            self._boton_izquierda.hide()
            self._boton_derecha.hide()
            return

        self._tarjeta.show()
        self._tarjeta.cargar_usuario(self._usuarios[self._indice_actual])

        if len(self._usuarios) <= 1:
            self._boton_izquierda.hide()
            self._boton_derecha.hide()
        else:
            self._boton_izquierda.show()
            self._boton_derecha.show()

    def _usuario_anterior(self):
        if not self._usuarios:
            return
        self._indice_actual = (self._indice_actual - 1) % len(self._usuarios)
        self._actualizar_tarjeta()

    def _usuario_siguiente(self):
        if not self._usuarios:
            return
        self._indice_actual = (self._indice_actual + 1) % len(self._usuarios)
        self._actualizar_tarjeta()

    def _al_intentar_ingresar(self):
        if not self._usuarios:
            return
        pin = self._tarjeta.obtener_pin_ingresado()
        usuario_id = self._usuarios[self._indice_actual].id
        self.usuario_ingresado.emit(usuario_id, pin)

    def mostrar_error_pin(self):
        self._tarjeta.mostrar_error_pin()

    def cuadrar(self):
        lr = self.layout_r

        lr.colocar_centrado_h(
            self._boton_nuevo_usuario,
            DR_Carrusel_Boton_Nuevo_Y,
            DR_Carrusel_Boton_Nuevo_Ancho,
            DR_Carrusel_Boton_Nuevo_Alto,
        )

        centro_x = (lr.ANCHO_DISENYO - DR_Carrusel_Tarjeta_W) / 2
        lr.colocar(
            self._tarjeta,
            centro_x,
            DR_Carrusel_Tarjeta_Y,
            DR_Carrusel_Tarjeta_W,
            DR_Carrusel_Tarjeta_H,
        )

        lr.colocar(
            self._boton_izquierda,
            DR_Carrusel_Flecha_X_Izquierda,
            DR_Carrusel_Flecha_Y,
            DR_Carrusel_Flecha_W,
            DR_Carrusel_Flecha_H,
        )
        lr.colocar(
            self._boton_derecha,
            DR_Carrusel_Flecha_X_Derecha,
            DR_Carrusel_Flecha_Y,
            DR_Carrusel_Flecha_W,
            DR_Carrusel_Flecha_H,
        )

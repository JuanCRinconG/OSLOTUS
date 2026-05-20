"""Tarjeta central del carrusel: avatar, nombre, PIN e ingreso."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING

from PyQt5.QtCore import Qt, QRegularExpression, pyqtSignal
from PyQt5.QtGui import (
    QBitmap,
    QFont,
    QPainter,
    QPixmap,
    QRegularExpressionValidator,
)
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget

from Recursos import (
    DR_Carrusel_Avatar_Diametro,
    DR_Carrusel_Avatar_Y,
    DR_Carrusel_Boton_Ingresar_H,
    DR_Carrusel_Boton_Ingresar_W,
    DR_Carrusel_Boton_Ingresar_Y,
    DR_Carrusel_Error_Alto,
    DR_Carrusel_Error_Y,
    DR_Carrusel_Nombre_Alto,
    DR_Carrusel_Nombre_Y,
    DR_Carrusel_PIN_Alto,
    DR_Carrusel_PIN_Ancho,
    DR_Carrusel_PIN_Y,
    GothicNormal,
    MixinLayout,
    PC_AzulOSLotus,
    PC_Blanco,
    PC_Rojo,
    PC_Transparente,
)

if TYPE_CHECKING:
    from LogicaMadre.LogicaOS.ModeloUsuario import ModeloUsuario

_ESTILO_CAMPO_PIN = f"""
QLineEdit {{
    color: {PC_Blanco};
    background-color: rgba(0, 0, 0, 0.35);
    border: 2px solid {PC_Blanco};
    border-radius: 6px;
    padding: 8px 12px;
}}
"""

_ESTILO_BOTON_INGRESAR = """
QPushButton {
    background-color: #2ecc71;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 22px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #27ae60;
}
QPushButton:pressed {
    background-color: #1e8449;
}
"""


def _pixmap_circular(pixmap: QPixmap, diametro: int) -> QPixmap:
    escalado = pixmap.scaled(
        diametro,
        diametro,
        Qt.KeepAspectRatioByExpanding,
        Qt.SmoothTransformation,
    )
    x = max(0, (escalado.width() - diametro) // 2)
    y = max(0, (escalado.height() - diametro) // 2)
    recorte = escalado.copy(x, y, diametro, diametro)

    mascara = QBitmap(diametro, diametro)
    mascara.fill(Qt.color0)
    pintor = QPainter(mascara)
    pintor.setBrush(Qt.color1)
    pintor.setPen(Qt.NoPen)
    pintor.drawEllipse(0, 0, diametro, diametro)
    pintor.end()
    recorte.setMask(mascara)
    return recorte


class _TarjetaUsuario(QWidget, MixinLayout):
    ingresar = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(f"background-color: {PC_Transparente};")
        self.inicializar_layout(self)

        self._usuario_actual: ModeloUsuario | None = None

        self._label_avatar = QLabel(self)
        self._label_avatar.setAlignment(Qt.AlignCenter)

        self._label_nombre = QLabel(self)
        self._label_nombre.setAlignment(Qt.AlignCenter)
        self._label_nombre.setFont(GothicNormal)
        self._label_nombre.setStyleSheet(f"color: {PC_Blanco}; background: transparent;")

        self._campo_pin = QLineEdit(self)
        self._campo_pin.setPlaceholderText("PIN")
        self._campo_pin.setEchoMode(QLineEdit.Password)
        self._campo_pin.setMaxLength(6)
        self._campo_pin.setAlignment(Qt.AlignCenter)
        self._campo_pin.setValidator(
            QRegularExpressionValidator(QRegularExpression(r"^\d{0,6}$"))
        )
        self._campo_pin.setStyleSheet(_ESTILO_CAMPO_PIN)
        self._campo_pin.returnPressed.connect(self._al_ingresar)

        self._label_error_pin = QLabel("PIN incorrecto", self)
        self._label_error_pin.setAlignment(Qt.AlignCenter)
        self._label_error_pin.setStyleSheet(f"color: {PC_Rojo}; background: transparent;")
        self._label_error_pin.hide()

        self._boton_ingresar = QPushButton("→", self)
        self._boton_ingresar.setStyleSheet(_ESTILO_BOTON_INGRESAR)
        self._boton_ingresar.setCursor(Qt.PointingHandCursor)
        self._boton_ingresar.clicked.connect(self._al_ingresar)

    def cargar_usuario(self, usuario: ModeloUsuario):
        self._usuario_actual = usuario
        self._label_nombre.setText(usuario.nombre)

        lr = self.layout_r
        diametro = lr.escalar_w(DR_Carrusel_Avatar_Diametro)
        self._label_avatar.setFixedSize(diametro, diametro)
        radio = diametro // 2

        if usuario.avatar and os.path.isfile(usuario.avatar):
            pixmap = QPixmap(usuario.avatar)
            if not pixmap.isNull():
                circular = _pixmap_circular(pixmap, diametro)
                self._label_avatar.setPixmap(circular)
                self._label_avatar.setStyleSheet(
                    f"background-color: transparent; border-radius: {radio}px;"
                )
            else:
                self._mostrar_inicial(usuario.nombre, diametro, radio)
        else:
            self._mostrar_inicial(usuario.nombre, diametro, radio)

        if usuario.pin is not None:
            self._campo_pin.show()
            self._campo_pin.clear()
        else:
            self._campo_pin.hide()

        self._label_error_pin.hide()
        self.cuadrar()
        if usuario.pin is not None:
            self._campo_pin.setFocus()

    def _mostrar_inicial(self, nombre: str, diametro: int, radio: int):
        inicial = nombre.strip()[:1].upper() if nombre.strip() else "?"
        self._label_avatar.setPixmap(QPixmap())
        self._label_avatar.setText(inicial)
        fuente = QFont(GothicNormal)
        fuente.setPixelSize(max(24, diametro // 3))
        self._label_avatar.setFont(fuente)
        self._label_avatar.setStyleSheet(
            f"""
            background-color: {PC_AzulOSLotus};
            color: {PC_Blanco};
            border-radius: {radio}px;
            """
        )

    def _al_ingresar(self):
        self.ingresar.emit()

    def obtener_pin_ingresado(self) -> str:
        return self._campo_pin.text().strip()

    def mostrar_error_pin(self):
        self._label_error_pin.show()
        self._campo_pin.clear()
        self._campo_pin.setFocus()
        self.cuadrar()

    def cuadrar(self):
        lr = self.layout_r
        ancho_tarjeta = self.width() if self.width() > 0 else lr.escalar_w(480)

        lr.colocar_centrado_h(
            self._label_avatar,
            DR_Carrusel_Avatar_Y,
            DR_Carrusel_Avatar_Diametro,
            DR_Carrusel_Avatar_Diametro,
        )

        lr.colocar_centrado_h(
            self._label_nombre,
            DR_Carrusel_Nombre_Y,
            ancho_tarjeta,
            DR_Carrusel_Nombre_Alto,
        )
        fuente_nombre = QFont(GothicNormal)
        fuente_nombre.setPixelSize(lr.escalar_fuente(28))
        self._label_nombre.setFont(fuente_nombre)

        if self._campo_pin.isVisible():
            lr.colocar_centrado_h(
                self._campo_pin,
                DR_Carrusel_PIN_Y,
                DR_Carrusel_PIN_Ancho,
                DR_Carrusel_PIN_Alto,
            )
            fuente_pin = QFont(self._campo_pin.font())
            fuente_pin.setPixelSize(lr.escalar_fuente(18))
            self._campo_pin.setFont(fuente_pin)

        if self._label_error_pin.isVisible():
            lr.colocar_centrado_h(
                self._label_error_pin,
                DR_Carrusel_Error_Y,
                DR_Carrusel_PIN_Ancho,
                DR_Carrusel_Error_Alto,
            )

        lr.colocar_centrado_h(
            self._boton_ingresar,
            DR_Carrusel_Boton_Ingresar_Y,
            DR_Carrusel_Boton_Ingresar_W,
            DR_Carrusel_Boton_Ingresar_H,
        )

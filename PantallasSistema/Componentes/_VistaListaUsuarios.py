"""Vista de lista de usuarios y acceso a creación de cuenta."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton, QWidget

from Recursos import (
    DR_ElegirUsuario_Avatar_Tamano,
    DR_ElegirUsuario_Boton_Alto,
    DR_ElegirUsuario_Boton_Ancho_Max,
    DR_ElegirUsuario_Separacion_Botones,
    DR_ElegirUsuario_Y_Inicio_Botones,
    GothicNormal,
    MixinLayout,
    PC_AzulOSLotus,
    PC_Blanco,
    PC_Transparente,
)

if TYPE_CHECKING:
    from LogicaMadre.LogicaOS.ModeloUsuario import ModeloUsuario

_ESTILO_BOTON = f"""
QPushButton {{
    color: {PC_Blanco};
    background-color: rgba(0, 0, 0, 0.35);
    border: 2px solid {PC_Blanco};
    border-radius: 8px;
    padding: 12px 24px;
}}
QPushButton:hover {{
    background-color: {PC_AzulOSLotus};
}}
"""


class _VistaListaUsuarios(QWidget, MixinLayout):
    usuario_seleccionado = pyqtSignal(str)
    crear_nuevo = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(f"background-color: {PC_Transparente};")
        self.inicializar_layout(self)

        self._botones: list[QPushButton] = []
        self._boton_nuevo = QPushButton("+ Nuevo usuario", self)
        self._boton_nuevo.setFont(GothicNormal)
        self._boton_nuevo.setCursor(Qt.PointingHandCursor)
        self._boton_nuevo.setStyleSheet(_ESTILO_BOTON)
        self._boton_nuevo.clicked.connect(self.crear_nuevo.emit)

    def cargar_usuarios(self, usuarios: list[ModeloUsuario]):
        self._limpiar_botones()

        for usuario in usuarios:
            boton = QPushButton(usuario.nombre, self)
            boton.setFont(GothicNormal)
            boton.setCursor(Qt.PointingHandCursor)
            boton.setStyleSheet(_ESTILO_BOTON)

            if usuario.avatar and os.path.isfile(usuario.avatar):
                tam = self.layout_r.escalar_w(DR_ElegirUsuario_Avatar_Tamano)
                pixmap = QPixmap(usuario.avatar).scaled(
                    tam, tam, Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
                boton.setIcon(QIcon(pixmap))
                boton.setIconSize(pixmap.size())

            boton.clicked.connect(
                lambda _checked=False, uid=usuario.id: self.usuario_seleccionado.emit(uid)
            )
            boton.show()
            self._botones.append(boton)

        self.cuadrar()

    def _limpiar_botones(self):
        for boton in self._botones:
            boton.deleteLater()
        self._botones.clear()

    def cuadrar(self):
        lr = self.layout_r
        w = self.width()
        if w < 1:
            return

        alto_boton = lr.escalar_h(DR_ElegirUsuario_Boton_Alto)
        separacion = lr.escalar_h(DR_ElegirUsuario_Separacion_Botones)
        ancho_boton = min(lr.escalar_w(DR_ElegirUsuario_Boton_Ancho_Max), w - lr.escalar_w(80))
        x = (w - ancho_boton) // 2
        y = lr.escalar_y(DR_ElegirUsuario_Y_Inicio_Botones)

        self._boton_nuevo.setGeometry(x, y, ancho_boton, alto_boton)
        y += alto_boton + separacion

        for boton in self._botones:
            boton.setGeometry(x, y, ancho_boton, alto_boton)
            y += alto_boton + separacion

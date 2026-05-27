"""Imagen de fondo de la pantalla elegir usuario."""

import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget

from Recursos import MixinLayout, PC_Transparente


class _FondoElegirUsuario(QWidget, MixinLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(f"background-color: {PC_Transparente};")
        self.inicializar_layout(self)

        ruta = os.path.join("Recursos", "PantallaElegirUsuarioImagen.png")
        self._pixmap = QPixmap(ruta)
        self._label = QLabel(self)
        self._label.setScaledContents(False)

    def cuadrar(self):
        w = self.width()
        h = self.height()
        if w < 1 or h < 1 or self._pixmap.isNull():
            return

        imagen = self._pixmap.scaled(w, h, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self._label.setPixmap(imagen)
        self._label.setGeometry(0, 0, w, h)

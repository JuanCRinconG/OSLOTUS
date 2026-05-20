from __future__ import annotations

from typing import Callable

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from Recursos import AnimacionesPyQt5, MixinLayout, GothicNormal
from Recursos import PC_Blanco, PC_Transparente, PC_AzulOSLotus
import os


class ComponentesElegirUsuario(QWidget, AnimacionesPyQt5, MixinLayout):
    IngresarSistema = pyqtSignal()
    usuario_seleccionado = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.inicializar_layout(self)

        self.setStyleSheet(
            f"background-color: {PC_Transparente}; border-radius: 2px;"
        )

        ruta = os.path.join("Recursos", "PantallaElegirUsuarioImagen.png")
        self.Imagen = QPixmap(ruta)
        self.LabelElegirUsuario = QLabel(self)
        self.LabelElegirUsuario.setScaledContents(False)

        self._contenedor_usuarios = QWidget(self)
        self._contenedor_usuarios.setStyleSheet("background: transparent;")
        self._botones_usuario: list[QPushButton] = []
        self._on_seleccion: Callable[[str], None] | None = None

    def mostrar_usuarios(self, usuarios, on_seleccion: Callable[[str], None] | None = None):
        self._on_seleccion = on_seleccion
        for boton in self._botones_usuario:
            boton.deleteLater()
        self._botones_usuario.clear()

        for usuario in usuarios:
            boton = QPushButton(usuario.nombre, self._contenedor_usuarios)
            boton.setFont(GothicNormal)
            boton.setCursor(Qt.PointingHandCursor)
            boton.setStyleSheet(
                f"""
                QPushButton {{
                    color: {PC_Blanco};
                    background-color: rgba(0, 0, 0, 0.35);
                    border: 2px solid {PC_Blanco};
                    border-radius: 8px;
                    padding: 12px 24px;
                    font-size: 16px;
                }}
                QPushButton:hover {{
                    background-color: {PC_AzulOSLotus};
                }}
                """
            )
            if usuario.avatar and os.path.isfile(usuario.avatar):
                pixmap = QPixmap(usuario.avatar).scaled(
                    48, 48, Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
                boton.setIcon(QIcon(pixmap))
            boton.clicked.connect(
                lambda _checked=False, uid=usuario.id: self._al_click_usuario(uid)
            )
            self._botones_usuario.append(boton)

        self.cuadrar()

    def _al_click_usuario(self, usuario_id: str):
        self.usuario_seleccionado.emit(usuario_id)
        if self._on_seleccion:
            self._on_seleccion(usuario_id)

    def cuadrar(self):
        lr = self.layout_r
        w = self.width()
        h = self.height()
        if w < 1 or h < 1:
            return

        if not self.Imagen.isNull():
            imagen_correcta = self.Imagen.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.LabelElegirUsuario.setPixmap(imagen_correcta)
            imagen_w = imagen_correcta.width()
            imagen_h = imagen_correcta.height()
            x_img = (w - imagen_w) // 2
            y_img = (h - imagen_h) // 2
            self.LabelElegirUsuario.setGeometry(x_img, y_img, imagen_w, imagen_h)

        cantidad = len(self._botones_usuario)
        if cantidad == 0:
            return

        ancho_boton = lr.escalar_w(320)
        alto_boton = lr.escalar_h(72)
        separacion = lr.escalar_h(16)
        alto_total = cantidad * alto_boton + (cantidad - 1) * separacion
        ancho_contenedor = min(w - lr.escalar_w(80), max(ancho_boton * 2, lr.escalar_w(640)))
        y_inicio = lr.escalar_y(780)

        self._contenedor_usuarios.setGeometry(
            (w - ancho_contenedor) // 2,
            y_inicio,
            ancho_contenedor,
            alto_total,
        )

        y = 0
        for boton in self._botones_usuario:
            boton.setGeometry(0, y, ancho_contenedor, alto_boton)
            y += alto_boton + separacion

    def CuadrarComponentesElegirUsuario(self):
        self.cuadrar()

    def showEvent(self, event):
        super().showEvent(event)
        self.cuadrar()
        print("Componente elegir usuario entered")

    def hideEvent(self, event):
        super().hideEvent(event)
        print("Componente elegir usuario exited")

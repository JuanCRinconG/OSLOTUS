from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import QTimer, Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QFontMetrics
from Recursos import AnimacionesPyQt5, MixinLayout
from Recursos import GothicNormal
from Recursos import PC_AzulOSLotus, PC_Blanco, PC_Transparente
from Recursos import (
    DR_ComponentesBootup_EspacioLogo_A_Titulo_Alto,
    DR_ComponentesBootup_Etiqueta_Titulo_Padding_Alto,
    DR_ComponentesBootup_Etiqueta_Padding_Min,
    DR_ComponentesBootup_Logo_Max,
    DR_ComponentesBootup_Logo_Min,
    DR_ComponentesBootup_OS_Divisor_Ancho_Interior,
    DR_ComponentesBootup_SeparacionLotusOS_Ancho,
    DR_ComponentesBootup_Titulo_Alto,
    DR_ComponentesBootup_Titulo_Ancho,
)

import os

# Coordenadas de diseño (1920×1080) equivalentes a las fracciones en DimensionesObjetos
_DISENO_MIN = 1080
_DISENO_TITULO_W = 1920 * DR_ComponentesBootup_Titulo_Ancho
_DISENO_TITULO_H = 1080 * DR_ComponentesBootup_Titulo_Alto
_DISENO_SEP_LOTUS_OS = 1920 * DR_ComponentesBootup_SeparacionLotusOS_Ancho
_DISENO_ESPACIO_LOGO_TITULO = 1080 * DR_ComponentesBootup_EspacioLogo_A_Titulo_Alto
_DISENO_LOGO_MAX = _DISENO_MIN * DR_ComponentesBootup_Logo_Max


class ComponentesBootup(QWidget, AnimacionesPyQt5, MixinLayout):
    CambiarPagina = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.inicializar_layout(self)

        self.setStyleSheet(
            f"background-color: {PC_Transparente}; border-radius: 2px;"
        )

        self.LabelLOTUS = QLabel(self, text="Lotus")
        self.LabelOS = QLabel(self, text="OS")
        self.LabelLOTUS.setStyleSheet(f"color: {PC_Blanco}")
        self.LabelOS.setStyleSheet(f"color: {PC_AzulOSLotus}; font-weight: bold;")
        self.LabelLOTUS.setFont(GothicNormal)
        self.LabelOS.setFont(GothicNormal)

        ruta = os.path.join("Recursos", "LotusOS_solid.png")

        self.Imagen = QPixmap(ruta)
        self.LogoLotus = QLabel(self)
        self.LogoLotus.setScaledContents(False)

        self.LabelLOTUS.setAlignment(Qt.AlignCenter)
        self.LabelOS.setAlignment(Qt.AlignCenter)

        self.LogoLotus.hide()
        self.LabelLOTUS.hide()
        self.LabelOS.hide()

    def cuadrar(self):
        lr = self.layout_r
        w = self.width()
        h = self.height()
        if w < 1 or h < 1:
            return

        cuadrado_max = max(
            lr.escalar_w(_DISENO_LOGO_MAX),
            lr.escalar_w(DR_ComponentesBootup_Logo_Min),
        )
        if self.Imagen.isNull():
            return
        imagen_correcta = self.Imagen.scaled(
            cuadrado_max, cuadrado_max, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.LogoLotus.setPixmap(imagen_correcta)
        imagen_w = imagen_correcta.width()
        imagen_h = imagen_correcta.height()
        self.LogoLotus.setGeometry((w - imagen_w) // 2, (h - imagen_h) // 2, imagen_w, imagen_h)

        titulo_w = lr.escalar_w(_DISENO_TITULO_W)
        titulo_h = lr.escalar_h(_DISENO_TITULO_H)
        espacio_entre = lr.escalar_w(_DISENO_SEP_LOTUS_OS)

        espacio_interior = titulo_w - espacio_entre
        os_w = max(
            espacio_interior // DR_ComponentesBootup_OS_Divisor_Ancho_Interior,
            1,
        )
        lotus_w = espacio_interior - os_w

        titulo_x = (w - titulo_w) // 2
        lotus_x = titulo_x
        os_x = titulo_x + lotus_w + espacio_entre

        logo_top = (h - imagen_h) // 2
        logo_bottom = logo_top + imagen_h
        titulo_y = logo_bottom + lr.escalar_h(_DISENO_ESPACIO_LOGO_TITULO)

        self.LabelLOTUS.setGeometry(lotus_x, titulo_y, lotus_w, titulo_h)
        self.LabelOS.setGeometry(os_x, titulo_y, os_w, titulo_h)
        self.AjustarFuente(self.LabelLOTUS, self.LabelLOTUS.text(), lotus_w, titulo_h)
        self.AjustarFuente(self.LabelOS, self.LabelOS.text(), os_w, titulo_h)

        espacio_restante = max(
            lr.escalar_h(DR_ComponentesBootup_Etiqueta_Padding_Min),
            int(titulo_h * DR_ComponentesBootup_Etiqueta_Titulo_Padding_Alto),
        )
        font_lotus = QFontMetrics(self.LabelLOTUS.font())
        font_os = QFontMetrics(self.LabelOS.font())
        lotus_w = max(
            1,
            min(
                font_lotus.horizontalAdvance(self.LabelLOTUS.text()) + 2 * espacio_restante,
                lotus_w,
            ),
        )
        os_w = max(
            1,
            min(
                font_os.horizontalAdvance(self.LabelOS.text()) + 2 * espacio_restante,
                os_w,
            ),
        )
        ancho_total = lotus_w + espacio_entre + os_w
        titulo_x_ajustado = (w - ancho_total) // 2
        self.LabelLOTUS.setGeometry(titulo_x_ajustado, titulo_y, lotus_w, titulo_h)
        self.LabelOS.setGeometry(
            titulo_x_ajustado + lotus_w + espacio_entre, titulo_y, os_w, titulo_h
        )

    def CuadrarComponentesBootup(self):
        self.cuadrar()

    def showEvent(self, event):
        super().showEvent(event)
        self.cuadrar()
        self.AnimacionInicio()
        print("Componente bootup entered")

    def AnimacionInicio(self):
        self.AnimacionTransparencia(self.LogoLotus, 3000)
        QTimer.singleShot(3000, lambda: self.AnimacionTransparencia(self.LabelLOTUS, 1000))
        QTimer.singleShot(4000, lambda: self.AnimacionTransparencia(self.LabelOS, 1000))
        QTimer.singleShot(8000, lambda: self.CambiarPagina.emit())

    def AjustarFuente(self, label, texto, max_ancho, max_alto):
        if max_ancho < 1 or max_alto < 1:
            return
        f = label.font()
        techo = min(max_alto, 200)
        for px in range(techo, 6, -1):
            f.setPixelSize(px)
            fm = QFontMetrics(f)
            if fm.horizontalAdvance(texto) <= max_ancho and fm.height() <= max_alto:
                label.setFont(f)
                return
        f.setPixelSize(6)
        label.setFont(f)

    def hideEvent(self, event):
        super().hideEvent(event)
        print("Componente bootup exited")

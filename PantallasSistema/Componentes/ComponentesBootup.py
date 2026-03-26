from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import QTimer, Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QFontMetrics
from Recursos import AnimacionesPyQt5
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

class ComponentesBootup(QWidget, AnimacionesPyQt5):
    CambiarPagina = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet(
            f"background-color: {PC_Transparente}; border-radius: 2px;"
        )

        #Elementos que van adentro de la pagina
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

        # Ocultos al inicio para animación de entrada (mostrar con show() cuando toque).
        self.LogoLotus.hide()
        self.LabelLOTUS.hide()
        self.LabelOS.hide()

    def CuadrarComponentesBootup(self):  
        w = self.width()
        h = self.height()
        if w < 1 or h < 1:
            return
        #Variables de altura y ancho para posicionar los elementos de forma relativa al tamaño del contenedor
        #Usar fracciones relacionadas a w y h para mantener la proporcion al redimensionar la ventana
        #Estructura de setGeometry: setGeometry(x, y, width, height)

        # Imagen del logo: como máximo COMPONENTES_BOOTUP_LOGO_FRACCION_MAX de min(w,h), mínimo COMPONENTES_BOOTUP_LOGO_MIN_PX px
        CuadradoMaximo = max(
            int(min(w, h) * DR_ComponentesBootup_Logo_Max),
            DR_ComponentesBootup_Logo_Min,
        )
        if self.Imagen.isNull():
            return
        ImagenCorrecta = self.Imagen.scaled(CuadradoMaximo, CuadradoMaximo, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.LogoLotus.setPixmap(ImagenCorrecta)
        ImagenW = ImagenCorrecta.width()
        ImagenH = ImagenCorrecta.height()
        self.LogoLotus.setGeometry((w - ImagenW) // 2, (h - ImagenH) // 2, ImagenW, ImagenH)


        # Labels de texto: ancho/alto relativos; separación Lotus/OS y espacio bajo el logo según DimensionesObjetos
        TituloW = int(DR_ComponentesBootup_Titulo_Ancho * w)
        TituloH = int(DR_ComponentesBootup_Titulo_Alto * h)
        EspacioEntreLotusOS = int(DR_ComponentesBootup_SeparacionLotusOS_Ancho * w)

        EspacioInterior = TituloW - EspacioEntreLotusOS
        OSW = int(
            max(
                EspacioInterior // DR_ComponentesBootup_OS_Divisor_Ancho_Interior,
                1,
            )
        )
        LotusW = int(EspacioInterior - OSW)  

        TituloX = (w - TituloW) // 2
        LotusX = int(TituloX)
        OSX = int(TituloX + LotusW + EspacioEntreLotusOS)

        logo_top = (h - ImagenH) // 2
        logo_bottom = logo_top + ImagenH
        TituloY = int(logo_bottom + int(DR_ComponentesBootup_EspacioLogo_A_Titulo_Alto * h))
        


        self.LabelLOTUS.setGeometry(LotusX, TituloY, LotusW, TituloH)
        self.LabelOS.setGeometry(OSX, TituloY, OSW, TituloH)
        self.AjustarFuente(self.LabelLOTUS, self.LabelLOTUS.text(), LotusW, TituloH)
        self.AjustarFuente(self.LabelOS, self.LabelOS.text(), OSW, TituloH)


        EspacioRestante = max(
            DR_ComponentesBootup_Etiqueta_Padding_Min,
            int(TituloH * DR_ComponentesBootup_Etiqueta_Titulo_Padding_Alto),
        )
        FontLotus = QFontMetrics(self.LabelLOTUS.font())
        FontOS = QFontMetrics(self.LabelOS.font())
        LotusW = max(1, min(FontLotus.horizontalAdvance(self.LabelLOTUS.text())+(2*EspacioRestante), LotusW))
        OSW = max(1, min(FontOS.horizontalAdvance(self.LabelOS.text())+(2*EspacioRestante), OSW))
        ancho_total = LotusW + EspacioEntreLotusOS + OSW
        TituloXAjustado = (w - ancho_total) // 2
        self.LabelLOTUS.setGeometry(TituloXAjustado, TituloY, LotusW, TituloH)
        self.LabelOS.setGeometry(TituloXAjustado + LotusW + EspacioEntreLotusOS, TituloY, OSW, TituloH)

    def showEvent(self, event):
        super().showEvent(event)
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
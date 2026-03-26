"""Recursos compartidos: animaciones, fuentes, imágenes referenciadas por código."""

from .AnimacionesPyQt5 import AnimacionesPyQt5

from .DimensionesObjetos import (
    DR_ComponentesBootup_EspacioLogo_A_Titulo_Alto,
    DR_ComponentesBootup_Etiqueta_Titulo_Padding_Alto,
    DR_ComponentesBootup_Etiqueta_Padding_Min,
    DR_ComponentesBootup_Logo_Max,
    DR_ComponentesBootup_Logo_Min,
    DR_ComponentesBootup_OS_Divisor_Ancho_Interior,
    DR_ComponentesBootup_SeparacionLotusOS_Ancho,
    DR_ComponentesBootup_Titulo_Alto,
    DR_ComponentesBootup_Titulo_Ancho,
    DR_OverlayEjemplo_Alto,
    DR_OverlayEjemplo_Ancho,
)

from .FuentesGothic import (
    GothicBold,
    GothicBoldItalic,
    GothicItalic,
    GothicLight,
    GothicLightItalic,
    GothicMedium,
    GothicMediumItalic,
    GothicNormal,
    GothicSemibold,
    GothicSemiboldItalic,
    GothicThin,
    GothicThinItalic,
)

from .PaletaColores import (
    PC_AzulOSLotus,
    PC_Blanco,
    PC_BordePanel,
    PC_FondoEscritorio,
    PC_GrisTextoClaro,
    PC_Negro,
    PC_Naranja,
    PC_Rojo,
    PC_Transparente,
)

__all__ = [
    "AnimacionesPyQt5",
    # Paleta de colores
    "PC_AzulOSLotus",
    "PC_Blanco",
    "PC_BordePanel",
    "PC_FondoEscritorio",
    "PC_GrisTextoClaro",
    "PC_Negro",
    "PC_Naranja",
    "PC_Rojo",
    "PC_Transparente",
    #Fuentes de la familia Gothic
    "GothicBold",
    "GothicBoldItalic",
    "GothicItalic",
    "GothicLight",
    "GothicLightItalic",
    "GothicMedium",
    "GothicMediumItalic",
    "GothicNormal",
    "GothicSemibold",
    "GothicSemiboldItalic",
    "GothicThin",
    "GothicThinItalic",
    #Dimensiones de los componentes de la pantalla Bootup
    "DR_ComponentesBootup_EspacioLogo_A_Titulo_Alto",
    "DR_ComponentesBootup_Etiqueta_Titulo_Padding_Alto",
    "DR_ComponentesBootup_Etiqueta_Padding_Min",
    "DR_ComponentesBootup_Logo_Max",
    "DR_ComponentesBootup_Logo_Min",
    "DR_ComponentesBootup_OS_Divisor_Ancho_Interior",
    "DR_ComponentesBootup_SeparacionLotusOS_Ancho",
    "DR_ComponentesBootup_Titulo_Alto",
    "DR_ComponentesBootup_Titulo_Ancho",
    #Dimensiones de la pantalla Overlay Ejemplo
    "DR_OverlayEjemplo_Alto",
    "DR_OverlayEjemplo_Ancho",
]

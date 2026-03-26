"""Fracciones y medidas relativas al padre para widgets de la UI."""
#Estas constantes son para definir las dimensiones de los componentes de la UI,
#para que sean reutilizables en diferentes pantallas y componentes.
#Y para evitar la creacion de numeros magicos en el codigo.

#Cuando son dimensiones relativas, se usan fracciones respecto al ancho o alto del padre.
#Utilizando numeros en el rango de 0 a 1. (ej. 0.5 = 50% del ancho o alto del padre)

#DR significan Dimensiones Relativas
#DR_OverlayEjemplo_Ancho y DR_OverlayEjemplo_Alto 

#son el ancho y alto de la pantalla de overlay ejemplo respecto al padre 
#(por ejemplo, GestorPantallas)

DR_OverlayEjemplo_Ancho = 0.7
DR_OverlayEjemplo_Alto = 0.3

# ComponentesBootup — CuadrarComponentesBootup (fracciones respecto a w/h del contenedor)
DR_ComponentesBootup_Logo_Max = 0.50
DR_ComponentesBootup_Logo_Min = 48

DR_ComponentesBootup_Titulo_Ancho = 0.5
DR_ComponentesBootup_Titulo_Alto = 0.2
DR_ComponentesBootup_SeparacionLotusOS_Ancho = 0.01

# Parte del ancho interior reservada para la etiqueta "OS" (resto para "Lotus")
DR_ComponentesBootup_OS_Divisor_Ancho_Interior = 3

DR_ComponentesBootup_EspacioLogo_A_Titulo_Alto = 0.03

DR_ComponentesBootup_Etiqueta_Padding_Min = 4
DR_ComponentesBootup_Etiqueta_Titulo_Padding_Alto = 1.0 / 12.0

__all__ = [
    "DR_OverlayEjemplo_Ancho",
    "DR_OverlayEjemplo_Alto",
    "DR_ComponentesBootup_Logo_Max",
    "DR_ComponentesBootup_Logo_Min",
    "DR_ComponentesBootup_Titulo_Ancho",
    "DR_ComponentesBootup_Titulo_Alto",
    "DR_ComponentesBootup_SeparacionLotusOS_Ancho",
    "DR_ComponentesBootup_OS_Divisor_Ancho_Interior",
    "DR_ComponentesBootup_EspacioLogo_A_Titulo_Alto",
    "DR_ComponentesBootup_Etiqueta_Padding_Min",
    "DR_ComponentesBootup_Etiqueta_Titulo_Padding_Alto",
]

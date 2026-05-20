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

# ElegirUsuario — vista de lista (px en espacio de diseño 1920×1080)
DR_ElegirUsuario_Boton_Alto = 72
DR_ElegirUsuario_Boton_Ancho_Max = 480
DR_ElegirUsuario_Separacion_Botones = 16
DR_ElegirUsuario_Y_Inicio_Botones = 680
DR_ElegirUsuario_Avatar_Tamano = 48

# ElegirUsuario — vista de creación
DR_ElegirUsuario_Campo_Alto = 56
DR_ElegirUsuario_Campo_Ancho = 560
DR_ElegirUsuario_Label_Alto = 32
DR_ElegirUsuario_Y_Titulo_Crear = 400
DR_ElegirUsuario_Separacion_Campos = 24
DR_ElegirUsuario_Boton_Confirmar_Y = 750

# Carrusel de usuarios (_VistaCarruselUsuarios)
DR_Carrusel_Boton_Nuevo_Y = 80
DR_Carrusel_Boton_Nuevo_Alto = 56
DR_Carrusel_Boton_Nuevo_Ancho = 320

DR_Carrusel_Tarjeta_Y = 280
DR_Carrusel_Tarjeta_W = 480
DR_Carrusel_Tarjeta_H = 500

DR_Carrusel_Flecha_X_Izquierda = 120
DR_Carrusel_Flecha_X_Derecha = 1680
DR_Carrusel_Flecha_Y = 480
DR_Carrusel_Flecha_W = 80
DR_Carrusel_Flecha_H = 120

# _TarjetaUsuario (coordenadas locales a la tarjeta)
DR_Carrusel_Avatar_Diametro = 180
DR_Carrusel_Avatar_Y = 60
DR_Carrusel_Nombre_Y = 270
DR_Carrusel_Nombre_Alto = 48
DR_Carrusel_PIN_Y = 340
DR_Carrusel_PIN_Alto = 56
DR_Carrusel_PIN_Ancho = 320
DR_Carrusel_Error_Y = 410
DR_Carrusel_Error_Alto = 32
DR_Carrusel_Boton_Ingresar_Y = 455
DR_Carrusel_Boton_Ingresar_W = 64
DR_Carrusel_Boton_Ingresar_H = 64

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
    "DR_ElegirUsuario_Boton_Alto",
    "DR_ElegirUsuario_Boton_Ancho_Max",
    "DR_ElegirUsuario_Separacion_Botones",
    "DR_ElegirUsuario_Y_Inicio_Botones",
    "DR_ElegirUsuario_Avatar_Tamano",
    "DR_ElegirUsuario_Campo_Alto",
    "DR_ElegirUsuario_Campo_Ancho",
    "DR_ElegirUsuario_Label_Alto",
    "DR_ElegirUsuario_Y_Titulo_Crear",
    "DR_ElegirUsuario_Separacion_Campos",
    "DR_ElegirUsuario_Boton_Confirmar_Y",
    "DR_Carrusel_Boton_Nuevo_Y",
    "DR_Carrusel_Boton_Nuevo_Alto",
    "DR_Carrusel_Boton_Nuevo_Ancho",
    "DR_Carrusel_Tarjeta_Y",
    "DR_Carrusel_Tarjeta_W",
    "DR_Carrusel_Tarjeta_H",
    "DR_Carrusel_Flecha_X_Izquierda",
    "DR_Carrusel_Flecha_X_Derecha",
    "DR_Carrusel_Flecha_Y",
    "DR_Carrusel_Flecha_W",
    "DR_Carrusel_Flecha_H",
    "DR_Carrusel_Avatar_Diametro",
    "DR_Carrusel_Avatar_Y",
    "DR_Carrusel_Nombre_Y",
    "DR_Carrusel_Nombre_Alto",
    "DR_Carrusel_PIN_Y",
    "DR_Carrusel_PIN_Alto",
    "DR_Carrusel_PIN_Ancho",
    "DR_Carrusel_Error_Y",
    "DR_Carrusel_Error_Alto",
    "DR_Carrusel_Boton_Ingresar_Y",
    "DR_Carrusel_Boton_Ingresar_W",
    "DR_Carrusel_Boton_Ingresar_H",
]

import sys
from PyQt5.QtWidgets import QApplication
from LogicaMadre.ClasePrincipalLotus import Lotus

if __name__ == "__main__":
    #A diferencia de tkinter, el motor de PyQt5 se ejecuta en un loop separado de la clase principal.
#por lo que se debe crear una instancia de QApplication para que sea el motor de las ventanas que creemos 
#y asi registrar cosas como inputs de mouse o teclado,
#y ejecutar el loop para que la aplicación funcione correctamente.
    MotorQT = QApplication(sys.argv)
    Lotus = Lotus()
    Lotus.show()
    sys.exit(MotorQT.exec_())

#Documentacion:
#El sistema empieza en la clase principal Lotus, que es la ventana principal del programa
#Desde esta clase se acceden dos componentes de logica madre, el gestor de pantallas y el controlador.

#1. Clase principal
#La clase principal es la ventana principal del programa, y todas las clases heredan de esta clase
#Ya que es la aplicacion principal, cualquier atajo de teclado aplica a esta clase


#2. Logica de pantallas
#El gestor de pantallas se encarga de manejar las diferentes pantallas del programa, con dos tipos
#Las pantallas normales, que son parte de un stackedWidget, que tiene la funcionalidad de solo mostrar una de estas a la vez
#Las sobrepantallas, que son ventanas que se muestran por encima de las pantallas normales


#3. Estructura de clases de UI
#La aplicacion como tal tiene dos capas de clase, primero es la clase principal QMainWindow
#Esta pantalla principal tiene un contenedor, que es el widget Gestor, que viene de la clase GestorPantallas
#En este gestor es donde se crean las pantallas normales y sobrepantallas, y se manejan sus cambios, eliminaciones y restauraciones.
#El gestor tiene un stackedWidget llamado FilaPantallas, que es donde se agregan las pantallas normales.
#El gestor como tal es una pantalla negra sin nada, y las pantallas normales se muestran dentro de este contenedor
#Mientras que las sobrepantallas se muestran por encima de este contenedor.
#Las sobrepantallas se muestran por encima de sus parientes cuando son llamadas, y se ocultan cuando son quitadas
#Las sobrepantallas pueden tener cualquier pariente, ahorita se recomienda esta estructura

#ClasePrincipal(QMainWindow)
#   |--GestorPantallas(QWidget)
#       |--QstackedWidget()
#       |       |--PantallaNormal(QWidget)
#       |
#       |--Sobrepantalla(QWidget)

#Es posible crear sobrepantallas que sean parientes de otras clases
#Pero se recomienda que sean parientes del gestor de pantallas para evitar problemas de visualizacion
#Las sobrepantallas pueden agarrar elementos de sus parientes, ya sean funciones o estructura visual
#Como el tamaño de la pantalla, o su color de fondo, etc


#4. Estructura de las pantallas
#Las pantallas normales y sobrepantallas tienen una estructura similar, ambas heredan de QWidget
#Una pantalla, sin importar su tipo, debe tener la estructura de la pantalla (dicta el tamaño, el fondo, etc)
#Y un contenedor para los elementos de la pantalla, que es un widget llamado ContenedorElementos (ej: ComponentesBootup)
#Esto permite una estructura similar a esto, en caso de que haya elementos importantes que tienen que siempre
#ser visibles en una pantalla, como una barra de tareas

#QstackedWidget()
#   |--PantallaNormal(QWidget)
#           |--ContenedorElementos(QWidget)
#           |--BarraDeTareas(QWidget)

#Los componentes heredan de sus padres Qwidget, y se encargan de crear los elementos visuales de la pantalla, como botones, labels, etc
#Los componentes pueden extraer datos de sus padres, como el tamaño de la pantalla, o el color de fondo, para crear elementos que se adapten a la pantalla
#Para casos complejos, una pantalla puede tener varios componentes
#Cada uno encargado de una parte de la pantalla, como un componente para la barra de tareas, otro para el fondo, etc
#Pero recordar definir tamaño y posicion de cada componente para evitar problemas de visualizacion
#Un componente se puede tratar como una sobrepantalla de la pantalla actual, y por ende se puede tratar de dos maneras
#Un espacio que una componente comparte con otro, es decir, se puede establecer una estructura asi:

#PantallaNormal()
#   |--Componente1(PantallaNormal)
#   |       |--Tamaño:(self.Parientewidth, self.Parienteheight*0.7)
#   |               #Este componente ocupa el 70% del espacio de la pantalla de forma vertical, y el 100% de forma horizontal
#   |--Componente2(PantallaNormal)
#           |--Tamaño:(self.Parientewidth, self.Parienteheight*0.3)
#                   #Este componente ocupa el 30% del espacio de la pantalla de forma vertical, y el 100% de forma horizontal

#En este caso, el componente1 y el componente2 comparten el espacio de la pantalla si se estructuran correctamente
#Incluso aunque la aplicacion cambie de tamaño
#Ya que su tamaño depende de un porcentaje del tamaño de la pantalla
#En vez de poner botones con funcionalidades adentro de los componentes, manejar un sistema de emision de señales
#Usando pyqtSignal(), y asi conectar estas señales a las pantallas como tal
#Y que estas pantallas se conecten con funciones del controlador


#5. Gestion de eventos de las pantallas
#Cada pantalla tiene una funcion llamada showEvent, que se ejecuta cada vez que la pantalla se muestra,
#Y una funcion llamada hideEvent, que se ejecuta cada vez que la pantalla se oculta, esto incluye cuando se cambia
#A otra aplicacion del sistema, o se minimiza la aplicacion, etc
#Estas funciones se pueden usar para ejecutar codigo cada vez que la pantalla se muestra o se oculta
#Como actualizar elementos de la pantalla, o guardar datos, etc
#Adicionalmente, cada pantalla tiene una funcion llamada CentrarComponentes y CentrarPantalla
#Y se ejecutan cada vez que el gestor de pantallas detecta un cambio de tamaño en la aplicacion, usando resizeEvent
#Lo que llama a las funciones sincronizarPantallas y sincronizarSobrepantallas
#Que a su vez llaman a las funciones de cada pantalla para centrar sus componentes o la pantalla en si
#showEvent se ejecuta cuando la pantalla se muestra por primera vez, lo que es util para centrar componentes o gestionar animaciones
#hideEvent se ejecuta cuando la pantalla ya no es visible, lo que no permite ejecutar animaciones de salida
#Por esto, es mejor usar el controlador para gestionar animaciones de salida y hideEvent para logica importante 


#6. Estructura de logica 
#El controlador manejara operaciones logicas, animaciones de salida y cosas adicionales
#El controlador se puede llamar de cualquier forma, tratar de mantener cosas logicas del sistema en el controlador
#Por ejemplo: Que usuario se elige y que el controlador almacene esos datos, o que el controlador maneje las animaciones de salida de las pantallas, etc
#Esto es para evitar que el Gestor de pantallas tenga mucha logica
#Y se encargue solo de manejar las pantallas, y que el controlador se encargue de manejar la logica del sistema


#7. Cosas que tener en cuenta:
#El gestor de pantallas tiene una funcion que se llama RestaurarPantalla, que se encarga de restaurar una pantalla 
#A su estado inicial, pero esto se hace usando una funcion llamada reset, 
#Que se debe definir en cada pantalla, y idealmente se usa para restaurar el estado de los elementos de la pantalla, como botones, labels, etc
#Adicionalmente, el gestor de pantallas por ahora solo elimina pantallas de la memoria si se usan las funciones
#BorrarSobrepantalla, BorrarPantalla, BorrarTodasPantallas, por que usan la funcion deleteLater()
#Por lo que hacen falta funciones que solo oculten las pantallas, para evitar perder datos importantes, como el usuario elegido, etc.


#8. Estructura de archivos
#La estructura de archivos es la siguiente:

#AplicacionSistemaOperativoLOTUS/
#   |--LogicaMadre/
#   |       |--ClasePrincipalLotus.py
#   |       |--ControladorPantallas.py
#   |       |--GestorPantallas.py
#   |--PantallasSistema/
#   |       |--Pantallas/
#   |       |       |--PantallaBootup.py
#   |       |       |--PantallaOverlayEjemplo.py
#   |       |--Componentes/
#   |               |--ComponentesBootup.py
#   |               |--ComponentesOverlayEjemplo.py
#   |--Recursos/
#           |--AnimacionesPyQt5
#           |--LotusOS_solid.png
#           |--LotusOS_transparent.png

#En esta estructura, es recomendable mantener componentes de logica madre en el archivo logica madre, en todo caso
#Se pueden crear folderes diferentes, en caso de querer separar la logica del motor de UI y la logica del sistema operativo
#Las diferentes pantallas del sistema y sus coponentes se pueden poner en sus respectivos folderes
#En este caso, se podria en logica madre hacer un folder de LogicaUI y LogicaOS
#En LogicaUI pueden ir cosas de la UI, y en LogicaOS cosas del OS
#En este caso, el controlador seria mas de la OS que de la UI, y serviria como un puente
#Mientras que en recursos pueden ir cosas estilizadas como imagenes y animaciones dedicadas

#9. Cosas por hacer
#Toda la logica del sistema operativo como tal, esto encapsula:

#Sistema de gestion y creacion de usuarios
#Sistema de gestion de archivos
#Sisetma de gestion de memoria
#Sistema de permisos y usuario
#Funcionalidad pomodoro
#Sistema de ajustes

#Mejoras de la estructura de la UI, si se te ocurren cambios, acuerdate de documentarlos
#Hacer mas funciones reusables, las funciones de centrado podrian ser heredadas usando el constructor de clases
#Pasar la fuente del sistema Century Gothic a recursos (podemos usar otra pero a mi me gusta mucho - Camilo)
#Pantallas estandarizadas? (Me parece que gastaria bastante tiempo hacer un sistema asi, pero ustedes deciden - Camilo)
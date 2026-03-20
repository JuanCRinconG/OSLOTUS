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
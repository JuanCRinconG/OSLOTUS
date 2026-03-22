#Núcleos de la UI: 
#Archivos en LogicaUI: GestorPantallas, GestorAtajos, ClasePrincipalLotus

#Nucleos de la OS: GestorUsuarios, GestorMemoria
#Archivos en LogicaOS: GestorUsuarios, GestorMemoria

#Controlador de la UI: ControladorSistema
#Archivos en ControladorSistema: ControladorSistema


# Orden: gestor y controlador antes que Lotus (ClasePrincipalLotus depende de ambos).
from LogicaMadre.LogicaUI.GestorPantallas import GestorPantallas
from LogicaMadre.ControladorSistema import ControladorSistema
from LogicaMadre.LogicaUI.ClasePrincipalLotus import Lotus 

#No se han creado los nucleos de la OS todavia, por eso estan comentados
#from LogicaMadre.LogicaOS import GestorUsuarios, GestorMemoria

__all__ = [
    "GestorPantallas", 
    "ControladorSistema", 
    "Lotus" 
    #"GestorUsuarios", 
    #"GestorMemoria"
    ]

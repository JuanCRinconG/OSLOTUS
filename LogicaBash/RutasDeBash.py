# DEPRECADO: usar EjecutorBash / resolver_bash en código nuevo.
# Se mantienen estas constantes para compatibilidad con GestorAtajos y código legacy.

import os
from pathlib import Path

from LogicaBash.ResolvedorBash import resolver_bash

_RUTA_PROYECTO = Path(__file__).resolve().parent

BashEjecutableRuta = resolver_bash() or r"C:\Program Files\Git\bin\bash.exe"
TaskMGR_ScriptRuta = str(_RUTA_PROYECTO / "ArchivosBash" / "AbrirTMGR.sh")
Explorer_ScriptRuta = './AbrirExplorer.sh' 
"""QPushButton que ejecuta un script .sh al hacer clic."""

from __future__ import annotations

import os

from PyQt5.QtCore import QSize, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton

from LogicaBash.EjecutorBash import EjecutorBash
from LogicaBash.ResolvedorBash import bash_disponible


class _HiloBash(QThread):
    terminado = pyqtSignal(int)
    error = pyqtSignal(str)

    def __init__(self, ejecutor: EjecutorBash, ruta_script: str, args: list[str] | None = None):
        super().__init__()
        self._ejecutor = ejecutor
        self._ruta_script = ruta_script
        self._args = args or []

    def run(self):
        try:
            resultado = self._ejecutor.ejecutar(self._ruta_script, self._args)
            if resultado is None:
                self.error.emit("Bash no disponible")
                return
            self.terminado.emit(resultado.returncode)
        except Exception as exc:
            self.error.emit(str(exc))


class BotonBash(QPushButton):
    script_iniciado = pyqtSignal(str)
    script_terminado = pyqtSignal(int)
    script_error = pyqtSignal(str)

    def __init__(
        self,
        ruta_script: str,
        imagen: str | None = None,
        texto: str = "",
        asincrono: bool = True,
        tamano_icono: int = 32,
        parent=None,
    ):
        super().__init__(parent)
        self.ruta_script = ruta_script
        self.asincrono = asincrono
        self._ejecutor = EjecutorBash()
        self._hilo: _HiloBash | None = None

        if imagen and os.path.isfile(imagen):
            icono = QIcon(QPixmap(imagen))
            self.setIcon(icono)
            self.setIconSize(QSize(tamano_icono, tamano_icono))

        if texto:
            self.setText(texto)

        if not bash_disponible():
            self.setEnabled(False)
            self.setToolTip("Bash no disponible en este sistema")
        else:
            self.clicked.connect(self._al_hacer_click)

    def _al_hacer_click(self):
        self.script_iniciado.emit(self.ruta_script)

        if self.asincrono:
            proceso = self._ejecutor.ejecutar_async(self.ruta_script)
            if proceso is None:
                self.script_error.emit("Bash no disponible")
            return

        if self._hilo is not None and self._hilo.isRunning():
            return

        self._hilo = _HiloBash(self._ejecutor, self.ruta_script)
        self._hilo.terminado.connect(self.script_terminado.emit)
        self._hilo.error.connect(self.script_error.emit)
        self._hilo.finished.connect(lambda: setattr(self, "_hilo", None))
        self._hilo.start()

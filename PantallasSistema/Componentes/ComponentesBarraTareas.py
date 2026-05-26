"""Barra de tareas inferior del escritorio LOTUS OS."""

import subprocess
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore    import Qt, QTimer, QDateTime

from Recursos.PaletaColores import (
    PC_AzulOSLotus, PC_Negro, PC_Blanco,
    PC_BordePanel, PC_Transparente
)

ALTURA_BARRA = 48

class ComponentesBarraTareas(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(ALTURA_BARRA)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f"""
            ComponentesBarraTareas {{
                background-color: rgba(15, 15, 15, 220);
                border-top: 1px solid {PC_BordePanel};
            }}
        """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 0, 12, 0)
        layout.setSpacing(8)

        # ── Botón Explorador ──────────────────────────────────
        self.btn_explorador = QPushButton("📁  Explorador")
        self.btn_explorador.setCursor(Qt.PointingHandCursor)
        self.btn_explorador.setFixedHeight(34)
        self.btn_explorador.setStyleSheet(f"""
            QPushButton {{
                background-color: rgba(255,255,255,0.07);
                color: {PC_Blanco};
                border: 1px solid rgba(255,255,255,0.15);
                border-radius: 6px;
                padding: 0 16px;
                font-size: 13px;
            }}
            QPushButton:hover {{
                background-color: {PC_AzulOSLotus};
                border-color: {PC_AzulOSLotus};
            }}
            QPushButton:pressed {{
                background-color: rgba(39,169,245,0.7);
            }}
        """)
        self.btn_explorador.clicked.connect(self.abrir_explorador)

        # ── Espaciador ────────────────────────────────────────
        layout.addWidget(self.btn_explorador)
        layout.addStretch()

        # ── Reloj (hora + fecha) ──────────────────────────────
        self.label_reloj = QLabel()
        self.label_reloj.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_reloj.setStyleSheet(f"color: {PC_Blanco}; font-size: 12px;")
        layout.addWidget(self.label_reloj)

        # Actualizar cada segundo
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._actualizar_reloj)
        self._timer.start(1000)
        self._actualizar_reloj()   # mostrar de inmediato sin esperar 1s

    # ── Slots ─────────────────────────────────────────────────

    def abrir_explorador(self):
        from LogicaBash import BashEjecutableRuta, Explorer_ScriptRuta
        import os
        script = os.path.join(
            os.path.dirname(__file__),
            '..', '..', 'LogicaBash', 'ArchivosBash', 'AbrirExplorer.sh'
        )
        subprocess.Popen([BashEjecutableRuta, os.path.normpath(script)])

    def _actualizar_reloj(self):
        ahora = QDateTime.currentDateTime()
        hora  = ahora.toString("hh:mm:ss")
        fecha = ahora.toString("dd/MM/yyyy")
        self.label_reloj.setText(f"{hora}  •  {fecha}")

    # ── Posicionamiento ───────────────────────────────────────

    def CuadrarBarraTareas(self):
        padre = self.parent()
        if padre:
            self.setGeometry(0, padre.height() - ALTURA_BARRA,
                             padre.width(), ALTURA_BARRA)
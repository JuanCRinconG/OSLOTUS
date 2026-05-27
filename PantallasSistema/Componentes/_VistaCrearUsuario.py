"""Formulario de creación de usuario."""

from PyQt5.QtCore import Qt, QRegularExpression, pyqtSignal
from PyQt5.QtGui import QFont, QRegularExpressionValidator
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget

from Recursos import (
    DR_ElegirUsuario_Boton_Alto,
    DR_ElegirUsuario_Campo_Alto,
    DR_ElegirUsuario_Campo_Ancho,
    DR_ElegirUsuario_Label_Alto,
    DR_ElegirUsuario_Separacion_Campos,
    DR_ElegirUsuario_Y_Titulo_Crear,
    DR_ElegirUsuario_Boton_Confirmar_Y,
    GothicNormal,
    MixinLayout,
    PC_Blanco,
    PC_Rojo,
    PC_Transparente,
)

_ESTILO_CAMPO = """
QLineEdit {
    color: #2c3e50;
    background-color: rgba(255, 255, 255, 1.0);
    border: none;
    border-radius: 6px;
    padding: 8px 12px;
}
"""

_ESTILO_BOTON = f"""
QPushButton {{
    color: {PC_Blanco};
    background-color: rgba(0, 0, 0, 0.35);
    border: 2px solid {PC_Blanco};
    border-radius: 8px;
    padding: 10px 20px;
}}
QPushButton:hover {{
    background-color: rgba(255, 255, 255, 0.15);
}}
"""


class _VistaCrearUsuario(QWidget, MixinLayout):
    confirmar = pyqtSignal(str, str)
    cancelar = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.20);
            border-radius: 18px;
            border: 1px solid rgba(255, 255, 255, 0.45);
        """)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.inicializar_layout(self)

        self._label_titulo = QLabel("Crear nuevo usuario", self)
        self._label_titulo.setFont(GothicNormal)
        self._label_titulo.setAlignment(Qt.AlignCenter)
        self._label_titulo.setStyleSheet("""
            color: #1a1a2e; 
            background-color: rgba(255, 255, 255, 0.45);
            border-radius: 6px;
            padding: 4px 8px;
        """)

        self._label_nombre = QLabel("Nombre", self)
        self._label_nombre.setStyleSheet("""
            color: #2c3e50; 
            background-color: rgba(255, 255, 255, 0.45);
            border-radius: 6px;
            padding: 4px 8px;
        """)

        self._campo_nombre = QLineEdit(self)
        self._campo_nombre.setPlaceholderText("Nombre de usuario")
        self._campo_nombre.setMaxLength(32)
        self._campo_nombre.setStyleSheet(_ESTILO_CAMPO)
        self._campo_nombre.setFont(GothicNormal)

        self._label_pin = QLabel("PIN de acceso (dejar vacío para no usar)", self)
        self._label_pin.setStyleSheet("""
            color: #2c3e50; 
            background-color: rgba(255, 255, 255, 0.45);
            border-radius: 6px;
            padding: 4px 8px;
        """)
        self._label_pin.setWordWrap(True)

        self._campo_pin = QLineEdit(self)
        self._campo_pin.setPlaceholderText("PIN (opcional)")
        self._campo_pin.setEchoMode(QLineEdit.Password)
        self._campo_pin.setMaxLength(6)
        self._campo_pin.setValidator(
            QRegularExpressionValidator(QRegularExpression(r"^\d{0,6}$"))
        )
        self._campo_pin.setStyleSheet(_ESTILO_CAMPO)
        self._campo_pin.setFont(GothicNormal)

        self._label_error = QLabel(self)
        self._label_error.setStyleSheet(f"color: {PC_Rojo}; background: transparent;")
        self._label_error.hide()

        self._boton_confirmar = QPushButton("Crear usuario", self)
        self._boton_confirmar.setStyleSheet(_ESTILO_BOTON)
        self._boton_confirmar.setFont(GothicNormal)
        self._boton_confirmar.clicked.connect(self._al_confirmar)

        self._boton_cancelar = QPushButton("Cancelar", self)
        self._boton_cancelar.setStyleSheet(_ESTILO_BOTON)
        self._boton_cancelar.setFont(GothicNormal)
        self._boton_cancelar.clicked.connect(self.cancelar.emit)

    def _al_confirmar(self):
        nombre = self._campo_nombre.text().strip()
        if not nombre:
            self._label_error.setText("El nombre no puede estar vacío")
            self._label_error.show()
            return
        self._label_error.hide()
        self.confirmar.emit(nombre, self._campo_pin.text().strip())

    def limpiar(self):
        self._campo_nombre.clear()
        self._campo_pin.clear()
        self._label_error.hide()

    def cuadrar(self):
        lr = self.layout_r
        ancho = DR_ElegirUsuario_Campo_Ancho
        alto_campo = DR_ElegirUsuario_Campo_Alto
        alto_label = DR_ElegirUsuario_Label_Alto
        sep = DR_ElegirUsuario_Separacion_Campos

        y = DR_ElegirUsuario_Y_Titulo_Crear
        lr.colocar_centrado_h(self._label_titulo, y, ancho, 48)
        y += 48 + sep

        lr.colocar_centrado_h(self._label_nombre, y, ancho, alto_label)
        y += alto_label + 8
        lr.colocar_centrado_h(self._campo_nombre, y, ancho, alto_campo)
        y += alto_campo + sep

        lr.colocar_centrado_h(self._label_pin, y, ancho, alto_label + 16)
        y += alto_label + 16 + 8
        lr.colocar_centrado_h(self._campo_pin, y, ancho, alto_campo)
        y += alto_campo + 8
        lr.colocar_centrado_h(self._label_error, y, ancho, alto_label)

        ancho_boton = 220
        centro_x = lr.ANCHO_DISENYO / 2
        y_botones = DR_ElegirUsuario_Boton_Confirmar_Y
        lr.colocar(
            self._boton_cancelar,
            centro_x - ancho_boton - 20,
            y_botones,
            ancho_boton,
            DR_ElegirUsuario_Boton_Alto,
        )
        lr.colocar(
            self._boton_confirmar,
            centro_x + 20,
            y_botones,
            ancho_boton,
            DR_ElegirUsuario_Boton_Alto,
        )

        fuente_px = lr.escalar_fuente(16)
        fuente = QFont(self._campo_nombre.font())
        fuente.setPixelSize(fuente_px)
        for widget in (
            self._campo_nombre,
            self._campo_pin,
            self._boton_confirmar,
            self._boton_cancelar,
        ):
            widget.setFont(fuente)

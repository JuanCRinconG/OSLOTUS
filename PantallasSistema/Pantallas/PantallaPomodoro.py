# PantallasSistema/Pantallas/PantallaPomodoro.py
from PantallasSistema.PantallaBase import PantallaBase
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QSpinBox, QListWidget, QLabel
from PyQt5.QtWidgets import QWidget, QVBoxLayout

class PantallaPomodoro(PantallaBase):
    # Ajustamos para recibir el Controlador y el Pariente (que pasa el Gestor)
    def __init__(self, controlador, pariente=None):
        super().__init__(pariente)
        self.controlador = controlador
        
        # FORZAR TAMAÑO VISIBLE: Esto evita que colapse a un cuadro negro pequeño
        self.setFixedSize(450, 400) 
        
        self.ContenedorElementos = QWidget(self)
        self.construir_ui()

    def construir_ui(self):
        layout = QVBoxLayout()
        self.ContenedorElementos.setLayout(layout)
        self.ContenedorElementos.setGeometry(0, 0, self.width(), self.height())
        self.ContenedorElementos.setStyleSheet("background-color: #2b2b2b; border-radius: 10px;")

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.ContenedorElementos)

        # 1. Input de Tiempo
        layout.addWidget(QLabel("Minutos de concentración:"))
        self.input_tiempo = QSpinBox()
        self.input_tiempo.setRange(1, 120)
        self.input_tiempo.setValue(25)
        layout.addWidget(self.input_tiempo)

        # 2. Selector de Apps Permitidas (Whitelist)
        layout.addWidget(QLabel("Selecciona apps requeridas:"))
        self.lista_apps = QListWidget()
        self.lista_apps.setSelectionMode(QListWidget.MultiSelection)
        self.lista_apps.addItems(["Terminal", "Editor de Texto", "Calculadora"]) # Extraer del sistema dinámicamente
        layout.addWidget(self.lista_apps)

        # 3. Botón Iniciar
        self.btn_iniciar = QPushButton("Iniciar Pomodoro")
        self.btn_iniciar.clicked.connect(self.procesar_inicio)
        layout.addWidget(self.btn_iniciar)

    def procesar_inicio(self):
        minutos = self.input_tiempo.value()
        apps_seleccionadas = [item.text() for item in self.lista_apps.selectedItems()]
        
        # Enviar al controlador
        self.controlador.iniciar_pomodoro(minutos, apps_seleccionadas)
        # La pantalla se oculta (minimiza) desde el controlador
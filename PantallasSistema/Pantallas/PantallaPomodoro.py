from PantallasSistema.PantallaBase import PantallaBase
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QSpinBox, QScrollArea, QCheckBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class PantallaPomodoro(PantallaBase):
    def __init__(self, controlador, pariente=None):
        super().__init__(pariente)
        self.controlador = controlador
        
        # Tamaño fijo del widget flotante ajustado para dar espacio a la lista
        self.setFixedSize(420, 480)
        
        self.ContenedorElementos = QWidget(self)
        self.checkboxes_apps = {} # Diccionario para rastrear los checkboxes de las apps
        self.construir_ui()

    def construir_ui(self):
        # Layout principal de la sobrepantalla
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(0, 0, 0, 0)
        
        # Configuración del contenedor con fondo oscuro y bordes estilizados
        self.ContenedorElementos.setGeometry(0, 0, self.width(), self.height())
        self.ContenedorElementos.setStyleSheet("""
            QWidget {
                background-color: #1e1e24;
                border: 2px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
            }
        """)
        
        # Layout interno del contenedor
        layout_interno = QVBoxLayout(self.ContenedorElementos)
        layout_interno.setContentsMargins(25, 15, 25, 25)
        layout_interno.setSpacing(12)
        
        # ── CABECERA ESTILO MACOS ─────────────────────────────
        layout_header = QHBoxLayout()
        layout_header.setContentsMargins(0, 0, 0, 5)
        layout_header.setSpacing(8)
        
        # Botón Cerrar/Ocultar (Rojo)
        self.btn_cerrar_macos = QPushButton()
        self.btn_cerrar_macos.setFixedSize(12, 12)
        self.btn_cerrar_macos.setCursor(Qt.PointingHandCursor)
        self.btn_cerrar_macos.setStyleSheet("""
            QPushButton {
                background-color: #ff5f56;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #e04f47;
            }
        """)
        self.btn_cerrar_macos.clicked.connect(self.minimizar_ventana)
        
        # Botones estéticos (Amarillo y Verde)
        btn_min_pasivo = QWidget()
        btn_min_pasivo.setFixedSize(12, 12)
        btn_min_pasivo.setStyleSheet("background-color: #ffbd2e; border-radius: 6px;")
        
        btn_max_pasivo = QWidget()
        btn_max_pasivo.setFixedSize(12, 12)
        btn_max_pasivo.setStyleSheet("background-color: #27c93f; border-radius: 6px;")
        
        layout_header.addWidget(self.btn_cerrar_macos)
        layout_header.addWidget(btn_min_pasivo)
        layout_header.addWidget(btn_max_pasivo)
        layout_header.addStretch()
        
        # ── COMPONENTES DE LA INTERFAZ ────────────────────────
        # Barra de título de la sobrepantalla
        self.label_titulo = QLabel("Pomodoro Focus Timer")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.label_titulo.setStyleSheet("""
            color: #ffffff;
            font-size: 16px;
            font-weight: bold;
            font-family: 'Segoe UI', sans-serif;
            border: none;
            background: transparent;
            padding-bottom: 5px;
        """)
        
        # Separador visual sutil
        linea_separadora = QWidget()
        linea_separadora.setFixedHeight(1)
        linea_separadora.setStyleSheet("background-color: rgba(255, 255, 255, 0.08); border: none;")
        
        # Configuración de Tiempo (Minutos)
        layout_tiempo = QHBoxLayout()
        layout_tiempo.setSpacing(10)
        
        label_minutos = QLabel("Duración (minutos):")
        label_minutos.setStyleSheet("color: #e0e0e0; font-size: 13px; font-family: 'Segoe UI'; border: none; background: transparent;")
        
        self.input_minutos = QSpinBox()
        self.input_minutos.setRange(1, 180)
        self.input_minutos.setValue(25)
        self.input_minutos.setAlignment(Qt.AlignCenter)
        self.input_minutos.setStyleSheet("""
            QSpinBox {
                color: white;
                background-color: rgba(0, 0, 0, 0.2);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 6px;
                padding: 5px;
                font-size: 13px;
                min-width: 70px;
            }
        """)
        
        layout_tiempo.addWidget(label_minutos)
        layout_tiempo.addWidget(self.input_minutos)
        layout_tiempo.addStretch()
        
        # Selección de Aplicaciones
        label_apps = QLabel("Selecciona las aplicaciones a permitir:")
        label_apps.setStyleSheet("color: #e0e0e0; font-size: 13px; font-family: 'Segoe UI'; border: none; background: transparent;")
        
        scroll_apps = QScrollArea()
        scroll_apps.setWidgetResizable(True)
        scroll_apps.setStyleSheet("""
            QScrollArea {
                background-color: rgba(0, 0, 0, 0.15);
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-radius: 8px;
            }
        """)
        
        contenedor_scroll = QWidget()
        contenedor_scroll.setStyleSheet("background-color: transparent; border: none;")
        layout_scroll = QVBoxLayout(contenedor_scroll)
        layout_scroll.setContentsMargins(10, 10, 10, 10)
        layout_scroll.setSpacing(8)
        
        # RECURSIVIDAD: Extraer nombres dinámicamente desde el escritorio principal
        lista_apps = []
        pantalla_principal = None
        
        if self.controlador and hasattr(self.controlador.gestor_pantallas, 'Pantallas'):
            pantalla_principal = self.controlador.gestor_pantallas.Pantallas.get("PantallaPrincipal")
            
        if pantalla_principal and hasattr(pantalla_principal, 'componentes'):
            lista_apps = [app.nombre for app in pantalla_principal.componentes.aplicaciones]
            
        if not lista_apps:
            lista_apps = ["Terminal", "Firefox", "Calculadora", "Editor de Texto", "Navegador de Archivos", "Configuración", "Captura de Pantalla", "Discos"]
        
        # Renderizado de los Checkboxes
        for app_name in lista_apps:
            chk = QCheckBox(app_name)
            chk.setStyleSheet("""
                QCheckBox {
                    color: #e0e0e0;
                    font-size: 12px;
                    font-family: 'Segoe UI';
                    background: transparent;
                    border: none;
                }
                QCheckBox::indicator {
                    width: 16px;
                    height: 16px;
                    background-color: rgba(255, 255, 255, 0.05);
                    border: 1px solid rgba(255, 255, 255, 0.2);
                    border-radius: 4px;
                }
                QCheckBox::indicator:checked {
                    background-color: #2e7d32;
                    border: 1px solid #388e3c;
                }
            """)
            layout_scroll.addWidget(chk)
            self.checkboxes_apps[app_name] = chk
            
        layout_scroll.addStretch()
        scroll_apps.setWidget(contenedor_scroll)
        
        # Display del Cronómetro
        self.label_cronometro = QLabel("25:00")
        self.label_cronometro.setAlignment(Qt.AlignCenter)
        self.label_cronometro.setStyleSheet("""
            color: #ffffff;
            font-size: 48px;
            font-weight: 600;
            font-family: 'Consolas', 'Monospace', sans-serif;
            background-color: rgba(0, 0, 0, 0.25);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 8px 0px;
            margin: 5px 0px;
        """)
        
        # Contenedor Horizontal para los Botones de Control
        layout_botones = QHBoxLayout()
        layout_botones.setSpacing(12)
        
        estilo_botones = """
            QPushButton {
                color: #ffffff;
                font-size: 13px;
                font-weight: 600;
                font-family: 'Segoe UI', sans-serif;
                border-radius: 8px;
                padding: 10px 20px;
                border: none;
            }
        """
        
        self.btn_iniciar = QPushButton("Iniciar")
        self.btn_iniciar.setStyleSheet(estilo_botones + """
            QPushButton { background-color: #2e7d32; }
            QPushButton:hover { background-color: #388e3c; }
            QPushButton:pressed { background-color: #1b5e20; }
        """)
        self.btn_iniciar.setCursor(Qt.PointingHandCursor)
        
        self.btn_pausa = QPushButton("Pausa")
        self.btn_pausa.setStyleSheet(estilo_botones + """
            QPushButton { background-color: #f57c00; }
            QPushButton:hover { background-color: #fb8c00; }
            QPushButton:pressed { background-color: #e65100; }
        """)
        self.btn_pausa.setCursor(Qt.PointingHandCursor)
        
        self.btn_reiniciar = QPushButton("Reiniciar")
        self.btn_reiniciar.setStyleSheet(estilo_botones + """
            QPushButton { background-color: #c62828; }
            QPushButton:hover { background-color: #d32f2f; }
            QPushButton:pressed { background-color: #b71c1c; }
        """)
        self.btn_reiniciar.setCursor(Qt.PointingHandCursor)
        
        self.btn_iniciar.clicked.connect(self.procesar_inicio)
        self.btn_pausa.clicked.connect(self.procesar_pausa)
        self.btn_reiniciar.clicked.connect(self.procesar_reiniciar)
        
        layout_botones.addWidget(self.btn_iniciar)
        layout_botones.addWidget(self.btn_pausa)
        layout_botones.addWidget(self.btn_reiniciar)
        
        # Ensamblar la jerarquía completa sin saltos de nombres
        layout_interno.addLayout(layout_header)
        layout_interno.addWidget(self.label_titulo)
        layout_interno.addWidget(linea_separadora)
        layout_interno.addLayout(layout_tiempo)
        layout_interno.addWidget(label_apps)
        layout_interno.addWidget(scroll_apps, 1) 
        layout_interno.addWidget(self.label_cronometro)
        layout_interno.addLayout(layout_botones)
        
        layout_principal.addWidget(self.ContenedorElementos)

    def minimizar_ventana(self):
        print("DEBUG: Ocultando ventana Pomodoro desde botones Mac")
        if self.controlador and hasattr(self.controlador, "gestor_pantallas"):
            self.controlador.gestor_pantallas.OcultarSobrepantalla("MenuPomodoro")
        else:
            self.hide()

    def procesar_inicio(self):
        print("DEBUG: Botón Iniciar presionado")
        minutos = self.input_minutos.value()
        apps_seleccionadas = [name for name, chk in self.checkboxes_apps.items() if chk.isChecked()]
        print(f"DEBUG: Enviando al controlador -> Minutos: {minutos}, Permitidas: {apps_seleccionadas}")
        if self.controlador:
            self.controlador.iniciar_pomodoro(minutos, apps_seleccionadas)

    def procesar_pausa(self):
        print("DEBUG: Botón Pausa presionado")
        if self.controlador:
            if hasattr(self.controlador, "pausar_pomodoro"):
                estado_pausado = self.controlador.pausar_pomodoro()
                if estado_pausado:
                    self.btn_pausa.setText("Reanudar")
                    self.btn_pausa.setStyleSheet(self.btn_pausa.styleSheet().replace("#f57c00", "#2e7d32").replace("#fb8c00", "#388e3c"))
                else:
                    self.btn_pausa.setText("Pausa")
                    self.btn_pausa.setStyleSheet(self.btn_pausa.styleSheet().replace("#2e7d32", "#f57c00").replace("#388e3c", "#fb8c00"))

    def procesar_reiniciar(self):
        print("DEBUG: Botón Reiniciar presionado")
        if self.controlador:
            if hasattr(self.controlador, "reiniciar_pomodoro"):
                self.controlador.reiniciar_pomodoro()
                self.label_cronometro.setText(f"{self.input_minutos.value()}:00")
                self.btn_pausa.setText("Pausa")
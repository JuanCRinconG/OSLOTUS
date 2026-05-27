from PantallasSistema.PantallaBase import PantallaBase
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QSpinBox, QScrollArea, QCheckBox
)
from PyQt5.QtCore import Qt

class PantallaPomodoro(PantallaBase):
    def __init__(self, controlador, pariente=None):
        super().__init__(pariente)
        self.controlador = controlador
        
        # Tamaño fijo ajustado para la interfaz
        self.setFixedSize(420, 520)
        
        self.ContenedorElementos = QWidget(self)
        self.checkboxes_apps = {}  # Diccionario para rastrear los checkboxes de las apps
        self.construir_ui()

    def construir_ui(self):
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(0, 0, 0, 0)
        
        self.ContenedorElementos.setGeometry(0, 0, self.width(), self.height())
        self.ContenedorElementos.setStyleSheet("""
            QWidget {
                background-color: #1e1e24;
                border: 2px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
            }
        """)
        
        layout_interno = QVBoxLayout(self.ContenedorElementos)
        layout_interno.setContentsMargins(25, 15, 25, 25)
        layout_interno.setSpacing(12)
        
        # ── CABECERA ESTILO MACOS (SOLO BOTÓN ROJO) ─────────────────────────────
        layout_header = QHBoxLayout()
        layout_header.setContentsMargins(0, 0, 0, 5)
        layout_header.setSpacing(8)
        
        self.btn_cerrar_macos = QPushButton()
        self.btn_cerrar_macos.setFixedSize(12, 12)
        self.btn_cerrar_macos.setCursor(Qt.PointingHandCursor)
        self.btn_cerrar_macos.setStyleSheet("""
            QPushButton { background-color: #ff5f56; border: none; border-radius: 6px; }
            QPushButton:hover { background-color: #e04f47; }
        """)
        self.btn_cerrar_macos.clicked.connect(self.minimizar_ventana)
        
        layout_header.addWidget(self.btn_cerrar_macos)
        layout_header.addStretch()
        
        # ── COMPONENTES DE LA INTERFAZ ────────────────────────
        self.label_titulo = QLabel("Pomodoro Focus Timer")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.label_titulo.setStyleSheet("color: #ffffff; font-size: 16px; font-weight: bold; font-family: 'Segoe UI'; border: none; background: transparent; padding-bottom: 5px;")
        
        linea_separadora = QWidget()
        linea_separadora.setFixedHeight(1)
        linea_separadora.setStyleSheet("background-color: rgba(255, 255, 255, 0.08); border: none;")
        
        layout_tiempos = QVBoxLayout()
        layout_tiempos.setSpacing(8)
        
        # Fila Tiempo Trabajo
        layout_trabajo = QHBoxLayout()
        label_minutos = QLabel("Tiempo de Enfoque (min):")
        label_minutos.setStyleSheet("color: #e0e0e0; font-size: 13px; font-family: 'Segoe UI'; border: none; background: transparent;")
        self.input_minutos = QSpinBox()
        self.input_minutos.setRange(1, 180)
        self.input_minutos.setValue(25)
        self.input_minutos.setAlignment(Qt.AlignCenter)
        self.input_minutos.setStyleSheet("QSpinBox { color: white; background-color: rgba(0, 0, 0, 0.2); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 6px; padding: 4px; min-width: 70px; }")
        layout_trabajo.addWidget(label_minutos)
        layout_trabajo.addWidget(self.input_minutos)
        
        # Fila Tiempo Descanso
        layout_descanso = QHBoxLayout()
        label_descanso = QLabel("Tiempo de Receso (min):")
        label_descanso.setStyleSheet("color: #e0e0e0; font-size: 13px; font-family: 'Segoe UI'; border: none; background: transparent;")
        self.input_descanso = QSpinBox()
        self.input_descanso.setRange(1, 60)
        self.input_descanso.setValue(5)
        self.input_descanso.setAlignment(Qt.AlignCenter)
        self.input_descanso.setStyleSheet("QSpinBox { color: white; background-color: rgba(0, 0, 0, 0.2); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 6px; padding: 4px; min-width: 70px; }")
        layout_descanso.addWidget(label_descanso)
        layout_descanso.addWidget(self.input_descanso)
        
        layout_tiempos.addLayout(layout_trabajo)
        layout_tiempos.addLayout(layout_descanso)
        
        label_apps = QLabel("Selecciona las aplicaciones a permitir:")
        label_apps.setStyleSheet("color: #e0e0e0; font-size: 13px; font-family: 'Segoe UI'; border: none; background: transparent;")
        
        self.scroll_apps = QScrollArea()
        self.scroll_apps.setWidgetResizable(True)
        self.scroll_apps.setStyleSheet("QScrollArea { background-color: rgba(0, 0, 0, 0.15); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 8px; }")
        
        contenedor_scroll = QWidget()
        contenedor_scroll.setStyleSheet("background-color: transparent; border: none;")
        layout_scroll = QVBoxLayout(contenedor_scroll)
        layout_scroll.setContentsMargins(10, 10, 10, 10)
        layout_scroll.setSpacing(8)
        
        lista_apps = []
        if self.controlador and hasattr(self.controlador.gestor_pantallas, 'Pantallas'):
            pantalla_principal = self.controlador.gestor_pantallas.Pantallas.get("PantallaPrincipal")
            if pantalla_principal and hasattr(pantalla_principal, 'componentes'):
                lista_apps = [app.nombre for app in pantalla_principal.componentes.aplicaciones]
        
        if not lista_apps:
            lista_apps = ["Terminal", "Firefox", "Calculadora", "Editor de Texto", "Navegador de Archivos", "Configuración", "Captura de Pantalla", "Discos"]
        
        for app_name in lista_apps:
            chk = QCheckBox(app_name)
            chk.setStyleSheet("QCheckBox { color: #e0e0e0; font-size: 12px; font-family: 'Segoe UI'; background: transparent; border: none; } QCheckBox::indicator { width: 16px; height: 16px; background-color: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 4px; } QCheckBox::indicator:checked { background-color: #2e7d32; border: 1px solid #388e3c; }")
            layout_scroll.addWidget(chk)
            self.checkboxes_apps[app_name] = chk
            
        layout_scroll.addStretch()
        self.scroll_apps.setWidget(contenedor_scroll)
        
        self.label_cronometro = QLabel("25:00")
        self.label_cronometro.setAlignment(Qt.AlignCenter)
        self.label_cronometro.setStyleSheet("color: #ffffff; font-size: 44px; font-weight: 600; font-family: 'Consolas'; background-color: rgba(0, 0, 0, 0.25); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 6px 0px;")
        
        layout_botones = QHBoxLayout()
        layout_botones.setSpacing(12)
        
        self.btn_iniciar = QPushButton("Iniciar")
        self.btn_iniciar.setCursor(Qt.PointingHandCursor)
        self.btn_iniciar.setStyleSheet("QPushButton { color: #ffffff; font-size: 13px; font-weight: 600; font-family: 'Segoe UI'; border-radius: 8px; padding: 10px 20px; border: none; background-color: #2e7d32; } QPushButton:hover { background-color: #388e3c; }")
        
        self.btn_pausa = QPushButton("Pausa")
        self.btn_pausa.setCursor(Qt.PointingHandCursor)
        self.btn_pausa.setStyleSheet("QPushButton { color: #ffffff; font-size: 13px; font-weight: 600; font-family: 'Segoe UI'; border-radius: 8px; padding: 10px 20px; border: none; background-color: #f57c00; } QPushButton:hover { background-color: #fb8c00; }")
        
        self.btn_reiniciar = QPushButton("Reiniciar")
        self.btn_reiniciar.setCursor(Qt.PointingHandCursor)
        self.btn_reiniciar.setStyleSheet("QPushButton { color: #ffffff; font-size: 13px; font-weight: 600; font-family: 'Segoe UI'; border-radius: 8px; padding: 10px 20px; border: none; background-color: #c62828; } QPushButton:hover { background-color: #d32f2f; }")
        
        self.btn_iniciar.clicked.connect(self.procesar_inicio)
        self.btn_pausa.clicked.connect(self.procesar_pausa)
        self.btn_reiniciar.clicked.connect(self.procesar_reiniciar)
        
        layout_botones.addWidget(self.btn_iniciar)
        layout_botones.addWidget(self.btn_pausa)
        layout_botones.addWidget(self.btn_reiniciar)
        
        layout_interno.addLayout(layout_header)
        layout_interno.addWidget(self.label_titulo)
        layout_interno.addWidget(linea_separadora)
        layout_interno.addLayout(layout_tiempos)
        layout_interno.addWidget(label_apps)
        layout_interno.addWidget(self.scroll_apps, 1) 
        layout_interno.addWidget(self.label_cronometro)
        layout_interno.addLayout(layout_botones)
        
        layout_principal.addWidget(self.ContenedorElementos)

    def mousePressEvent(self, event):
        """Detección estricta basada en herencia de widgets hijos de Qt."""
        widget_impactado = self.childAt(event.pos())
        
        # Si el clic se dio en la capa base transparente y no tocó ningún componente interno
        if widget_impactado is None or widget_impactado == self:
            print("DEBUG UI: Clic en zona muerta exterior detectado. Ocultando sobrepantalla.")
            self.minimizar_ventana()
            event.accept()
        else:
            super().mousePressEvent(event)

    def actualizar_cronometro(self, tiempo_str, estado_actual="Enfoque"):
        self.label_cronometro.setText(tiempo_str)
        if estado_actual == "Receso":
            self.label_titulo.setText("Pomodoro - ¡Tiempo de Receso!")
            self.label_titulo.setStyleSheet("color: #42a5f5; font-size: 16px; font-weight: bold; font-family: 'Segoe UI'; background: transparent;")
        else:
            self.label_titulo.setText("Pomodoro Focus Timer")
            self.label_titulo.setStyleSheet("color: #ffffff; font-size: 16px; font-weight: bold; font-family: 'Segoe UI'; background: transparent;")

    def minimizar_ventana(self):
        if self.controlador and hasattr(self.controlador, "gestor_pantallas"):
            self.controlador.gestor_pantallas.OcultarSobrepantalla("MenuPomodoro")
        else:
            self.hide()

    def procesar_inicio(self):
        minutos_enfoque = self.input_minutos.value()
        minutos_descanso = self.input_descanso.value()
        apps_seleccionadas = [name for name, chk in self.checkboxes_apps.items() if chk.isChecked()]
        
        if not apps_seleccionadas:
            from PyQt5.QtWidgets import QMessageBox
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Selección Requerida")
            msg.setText("Debes seleccionar al menos una aplicación para permitir durante el ciclo Pomodoro.")
            msg.setStyleSheet("QMessageBox { background-color: #1e1e24; border: 2px solid rgba(255, 255, 255, 0.1); border-radius: 12px; } QLabel { color: #ffffff; font-family: 'Segoe UI'; font-size: 13px; } QPushButton { color: #ffffff; background-color: #c62828; border: none; border-radius: 6px; padding: 6px 18px; }")
            msg.exec_()
            return

        if self.controlador:
            self.controlador.iniciar_pomodoro(minutos_enfoque, minutos_descanso, apps_seleccionadas)

    def procesar_pausa(self):
        """Maneja de forma síncrona el retorno booleano estricto del backend controlador."""
        if self.controlador and hasattr(self.controlador, "pausar_pomodoro"):
            # Almacenamos el retorno de la función lógica
            esta_pausado = self.controlador.pausar_pomodoro()
            
            if esta_pausado:
                print("DEBUG UI: Cambiando botón a modo REANUDAR (Verde)")
                self.btn_pausa.setText("Reanudar")
                self.btn_pausa.setStyleSheet("""
                    QPushButton { color: #ffffff; font-size: 13px; font-weight: 600; font-family: 'Segoe UI'; border-radius: 8px; padding: 10px 20px; border: none; background-color: #2e7d32; }
                    QPushButton:hover { background-color: #388e3c; }
                """)
            else:
                print("DEBUG UI: Cambiando botón a modo PAUSA (Naranja)")
                self.btn_pausa.setText("Pausa")
                self.btn_pausa.setStyleSheet("""
                    QPushButton { color: #ffffff; font-size: 13px; font-weight: 600; font-family: 'Segoe UI'; border-radius: 8px; padding: 10px 20px; border: none; background-color: #f57c00; }
                    QPushButton:hover { background-color: #fb8c00; }
                """)

    def procesar_reiniciar(self):
        if self.controlador and hasattr(self.controlador, "reiniciar_pomodoro"):
            self.controlador.reiniciar_pomodoro()
            self.label_cronometro.setText(f"{self.input_minutos.value()}:00")
            self.btn_pausa.setText("Pausa")
            self.btn_pausa.setStyleSheet("QPushButton { color: #ffffff; font-size: 13px; font-weight: 600; font-family: 'Segoe UI'; border-radius: 8px; padding: 10px 20px; border: none; background-color: #f57c00; } QPushButton:hover { background-color: #fb8c00; }")
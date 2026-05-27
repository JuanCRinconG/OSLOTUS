from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
    QScrollArea,
    QMessageBox,
    QSizePolicy,
)
from PyQt5.QtCore import Qt, QProcess, QSize, pyqtSignal
from PyQt5.QtGui import QPixmap, QFont, QDragEnterEvent, QDropEvent
from Recursos import MixinLayout
import os
import subprocess

class IconoAplicacion(QWidget):
    """Widget que representa un icono de aplicación en el escritorio"""
    ejecutar_aplicacion = pyqtSignal(dict)
    
    def __init__(self, nombre, comando, icono_ruta=None, parent=None):
        super().__init__(parent)
        self.nombre = nombre
        self.comando = comando
        self.icono_ruta = icono_ruta
        
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(5)
        
        self.icono_label = QLabel()
        self.icono_label.setAlignment(Qt.AlignCenter)
        self.icono_label.setFixedSize(64, 64)
        self.icono_label.setStyleSheet("""
            QLabel {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                padding: 5px;
            }
            QLabel:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        
        if icono_ruta and os.path.exists(icono_ruta):
            pixmap = QPixmap(icono_ruta)
            if not pixmap.isNull():
                self.icono_label.setPixmap(pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.icono_label.setText(nombre[0].upper())
            self.icono_label.setStyleSheet(self.icono_label.styleSheet() + """
                font-size: 32px;
                font-weight: bold;
                color: white;
            """)
        
        self.nombre_label = QLabel(nombre)
        self.nombre_label.setAlignment(Qt.AlignCenter)
        self.nombre_label.setWordWrap(True)
        self.nombre_label.setStyleSheet("color: white; font-size: 12px; background: transparent;")
        self.nombre_label.setMaximumWidth(80)
        
        layout.addWidget(self.icono_label)
        layout.addWidget(self.nombre_label)
        
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumSize(80, 100)
        self.setMaximumSize(100, 120)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.ejecutar_aplicacion.emit({
                "nombre": self.nombre,
                "comando": self.comando,
                "icono": self.icono_ruta
            })


class ComponentesPrincipal(QWidget, MixinLayout):
    """Escritorio principal con iconos de aplicaciones"""
    
    def __init__(self, controlador=None, parent=None):
        super().__init__(parent)
        self.controlador = controlador
        self.inicializar_layout(self)

        self.setAcceptDrops(True)
        self.aplicaciones = []
        self.procesos = {} 
        
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(20, 20, 20, 20)
        
        self.label_bienvenida = QLabel("Bienvenido a LOTUS OS")
        self.label_bienvenida.setAlignment(Qt.AlignCenter)
        self.label_bienvenida.setStyleSheet("""
            color: white;
            font-size: 24px;
            font-weight: bold;
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.5);
            border-radius: 10px;
        """)
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("QScrollArea { background-color: transparent; border: none; }")
        
        self.contenedor_iconos = QWidget()
        self.contenedor_iconos.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.contenedor_iconos.setStyleSheet("background-color: transparent;")
        
        self.layout_iconos = QGridLayout(self.contenedor_iconos)
        self.layout_iconos.setSpacing(20)
        self.layout_iconos.setContentsMargins(20, 20, 20, 20)
        
        scroll_area.setWidget(self.contenedor_iconos)
        
        self.label_estado = QLabel("Listo")
        self.label_estado.setStyleSheet("color: rgba(255, 255, 255, 0.7); padding: 5px;")
        
        layout_principal.addWidget(self.label_bienvenida)
        layout_principal.addWidget(scroll_area, 1)
        layout_principal.addWidget(self.label_estado)
        
        self.cargar_aplicaciones_predeterminadas()
    
    def cargar_aplicaciones_predeterminadas(self):
        aplicaciones = [
            {"nombre": "Terminal", "comando": "cmd", "icono": self.buscar_icono("terminal")},
            {"nombre": "Firefox", "comando": "firefox", "icono": self.buscar_icono("firefox")},
            {"nombre": "Calculadora", "comando": "calc", "icono": self.buscar_icono("calculator")},
            {"nombre": "Editor de Texto", "comando": "notepad", "icono": self.buscar_icono("gedit")},
            {"nombre": "Navegador de Archivos", "comando": "explorer", "icono": self.buscar_icono("nautilus")},
            {"nombre": "Configuración", "comando": "control", "icono": self.buscar_icono("settings")},
            {"nombre": "Captura de Pantalla", "comando": "snippingtool", "icono": self.buscar_icono("screenshot")},
            {"nombre": "Discos", "comando": "diskmgmt.msc", "icono": self.buscar_icono("disks")},
            {"nombre": "Pomodoro", "comando": "abrir_pomodoro", "icono": self.buscar_icono("pomodoro")},
        ]
        
        for app in aplicaciones:
            self.agregar_aplicacion(app["nombre"], app["comando"], app["icono"])
    
    def buscar_icono(self, nombre_icono):
        posibles_ubicaciones = [
            f"/usr/share/icons/hicolor/48x48/apps/{nombre_icono}.png",
            f"/usr/share/icons/hicolor/64x64/apps/{nombre_icono}.png",
            f"/usr/share/pixmaps/{nombre_icono}.png",
            f"/usr/share/icons/gnome/48x48/apps/{nombre_icono}.png",
        ]
        for ubicacion in posibles_ubicaciones:
            if os.path.exists(ubicacion): return ubicacion
        ruta_local = os.path.join("Recursos", f"{nombre_icono}.png")
        if os.path.exists(ruta_local): return ruta_local
        return None
    
    def agregar_aplicacion(self, nombre, comando, icono_ruta=None):
        icono = IconoAplicacion(nombre, comando, icono_ruta)
        print(f"DEBUG: Conectando icono {nombre} a ejecutar_comando_bash")
        icono.ejecutar_aplicacion.connect(self.ejecutar_comando_bash)
        
        num_aplicaciones = len(self.aplicaciones)
        fila = num_aplicaciones // 4
        columna = num_aplicaciones % 4
        
        self.layout_iconos.addWidget(icono, fila, columna, Qt.AlignTop | Qt.AlignLeft)
        self.aplicaciones.append(icono)
        self.contenedor_iconos.adjustSize()
    
    def ejecutar_comando_bash(self, app_info):
        print(f"DEBUG: Enlace de ejecución activado para: {app_info['nombre']}")
        nombre = app_info["nombre"]
        comando = app_info["comando"]

        # DEBUG: Verificar estado del controlador en el escritorio
        print(f"DEBUG: ¿Instancia de controlador disponible? {hasattr(self, 'controlador') and self.controlador is not None}")
        
        if hasattr(self, 'controlador') and self.controlador:
            if nombre == "Pomodoro":
                print("DEBUG: Inicializando flujo de renderizado de Pomodoro...")
                from PantallasSistema.Pantallas.PantallaPomodoro import PantallaPomodoro
                
                # CORRECCIÓN: El pariente no es 'self' (el contenedor de iconos), 
                # pasamos el gestor de pantallas directamente para que actúe como contenedor global.
                gestor = self.controlador.gestor_pantallas
                gestor.AgregarSobrepantalla("MenuPomodoro", PantallaPomodoro, self.controlador, gestor)
                
                gestor.MostrarSobrepantalla("MenuPomodoro")
                return

            if not self.controlador.intentar_abrir_aplicacion(nombre):
                QMessageBox.warning(self, "Bloqueo Activo", f"Pomodoro activo. {nombre} no está permitida.")
                self.label_estado.setText(f"Bloqueado: {nombre}")
                return
        
        self.label_estado.setText(f"Ejecutando: {nombre}...")
        try:
            proceso = QProcess(self)
            proceso.start(comando)
            self.procesos[nombre] = proceso
        except Exception:
            subprocess.Popen(comando, shell=True)
    
    def proceso_terminado(self, nombre):
        self.label_estado.setText(f"{nombre}: Cerrado")
        if nombre in self.procesos: del self.procesos[nombre]
    
    def error_proceso(self, nombre, error):
        self.label_estado.setText(f"{nombre}: Error")
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls(): event.accept()
        else: event.ignore()
    
    def dropEvent(self, event):
        for url in event.mimeData().urls():
            archivo = url.toLocalFile()
            if os.path.isfile(archivo):
                self.agregar_aplicacion(os.path.basename(archivo), f'xdg-open "{archivo}"')
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.reorganizar_iconos()
    
    def reorganizar_iconos(self):
        ancho = self.width()
        columnas = 6 if ancho >= 800 else (4 if ancho >= 600 else 2)
        for i, icono in enumerate(self.aplicaciones):
            fila = i // columnas
            columna = i % columnas
            self.layout_iconos.addWidget(icono, fila, columna, Qt.AlignTop | Qt.AlignLeft)

    def cuadrar(self):
        if self.parent():
            self.setGeometry(0, 0, self.parent().width(), self.parent().height())
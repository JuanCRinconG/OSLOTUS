from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
    QScrollArea,
    QMessageBox,
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
        
        # Icono
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
        
        # Cargar icono
        if icono_ruta and os.path.exists(icono_ruta):
            pixmap = QPixmap(icono_ruta)
            if not pixmap.isNull():
                self.icono_label.setPixmap(pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            # Icono por defecto (texto)
            self.icono_label.setText(nombre[0].upper())
            self.icono_label.setStyleSheet(self.icono_label.styleSheet() + """
                font-size: 32px;
                font-weight: bold;
                color: white;
            """)
        
        # Nombre de la aplicación
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
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.inicializar_layout(self)

        self.setAcceptDrops(True)
        self.aplicaciones = []
        self.procesos = {}  # Para mantener referencia a procesos en ejecución
        
        # Layout principal
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(20, 20, 20, 20)
        
        # Área de bienvenida
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
        
        # Área de iconos (scrollable)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: transparent;
                border: none;
            }
            QScrollBar:vertical {
                background-color: rgba(255, 255, 255, 0.1);
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background-color: #00aaff;
                border-radius: 5px;
            }
        """)
        
        self.contenedor_iconos = QWidget()
        self.layout_iconos = QGridLayout(self.contenedor_iconos)
        self.layout_iconos.setSpacing(20)
        self.layout_iconos.setContentsMargins(20, 20, 20, 20)
        
        scroll_area.setWidget(self.contenedor_iconos)
        
        # Barra de estado inferior
        self.label_estado = QLabel("Listo")
        self.label_estado.setStyleSheet("color: rgba(255, 255, 255, 0.7); padding: 5px;")
        
        # Agregar todo al layout
        layout_principal.addWidget(self.label_bienvenida)
        layout_principal.addWidget(scroll_area, 1)
        layout_principal.addWidget(self.label_estado)
        
        # Cargar aplicaciones predefinidas
        self.cargar_aplicaciones_predeterminadas()
    
    def cargar_aplicaciones_predeterminadas(self):
        """Cargar aplicaciones con comandos bash"""
        aplicaciones = [
            {
                "nombre": "Terminal",
                "comando": "gnome-terminal",
                "icono": self.buscar_icono("terminal")
            },
            {
                "nombre": "Firefox",
                "comando": "firefox",
                "icono": self.buscar_icono("firefox")
            },
            {
                "nombre": "Calculadora",
                "comando": "gnome-calculator",
                "icono": self.buscar_icono("calculator")
            },
            {
                "nombre": "Editor de Texto",
                "comando": "gedit",
                "icono": self.buscar_icono("gedit")
            },
            {
                "nombre": "Navegador de Archivos",
                "comando": "nautilus",
                "icono": self.buscar_icono("nautilus")
            },
            {
                "nombre": "Configuración",
                "comando": "gnome-control-center",
                "icono": self.buscar_icono("settings")
            },
            {
                "nombre": "Captura de Pantalla",
                "comando": "gnome-screenshot",
                "icono": self.buscar_icono("screenshot")
            },
            {
                "nombre": "Discos",
                "comando": "gnome-disks",
                "icono": self.buscar_icono("disks")
            }
        ]
        
        for app in aplicaciones:
            self.agregar_aplicacion(app["nombre"], app["comando"], app["icono"])
    
    def buscar_icono(self, nombre_icono):
        """Buscar icono del sistema"""
        posibles_ubicaciones = [
            f"/usr/share/icons/hicolor/48x48/apps/{nombre_icono}.png",
            f"/usr/share/icons/hicolor/64x64/apps/{nombre_icono}.png",
            f"/usr/share/pixmaps/{nombre_icono}.png",
            f"/usr/share/icons/gnome/48x48/apps/{nombre_icono}.png",
        ]
        
        for ubicacion in posibles_ubicaciones:
            if os.path.exists(ubicacion):
                return ubicacion
        
        # Iconos personalizados en Recursos
        ruta_local = os.path.join("Recursos", f"{nombre_icono}.png")
        if os.path.exists(ruta_local):
            return ruta_local
        
        return None
    
    def agregar_aplicacion(self, nombre, comando, icono_ruta=None):
        """Agregar una aplicación al escritorio"""
        icono = IconoAplicacion(nombre, comando, icono_ruta)
        icono.ejecutar_aplicacion.connect(self.ejecutar_comando_bash)
        
        # Posicionar en grid (máximo 4 columnas)
        num_aplicaciones = len(self.aplicaciones)
        fila = num_aplicaciones // 4
        columna = num_aplicaciones % 4
        
        self.layout_iconos.addWidget(icono, fila, columna, Qt.AlignTop | Qt.AlignLeft)
        self.aplicaciones.append(icono)
    
    def ejecutar_comando_bash(self, app_info):
        """Ejecutar comando bash en segundo plano"""
        comando = app_info["comando"]
        nombre = app_info["nombre"]
        
        self.label_estado.setText(f"Ejecutando: {nombre}...")
        
        try:
            # Método 1: Usar QProcess (recomendado para PyQt)
            proceso = QProcess(self)
            proceso.start(comando)
            
            # Guardar referencia para evitar garbage collection
            self.procesos[nombre] = proceso
            
            # Conectar señales para monitorear
            proceso.started.connect(lambda: self.label_estado.setText(f"{nombre}: Iniciado"))
            proceso.finished.connect(lambda: self.proceso_terminado(nombre))
            proceso.errorOccurred.connect(lambda error: self.error_proceso(nombre, error))
            
            self.label_estado.setText(f"{nombre}: Ejecutando...")
            
        except Exception as e:
            # Método 2: Usar subprocess como alternativa
            try:
                subprocess.Popen(comando, shell=True)
                self.label_estado.setText(f"{nombre}: Ejecutando en segundo plano")
            except Exception as e2:
                QMessageBox.warning(self, "Error", f"No se pudo ejecutar {nombre}\nError: {str(e2)}")
                self.label_estado.setText(f"Error al ejecutar {nombre}")
    
    def proceso_terminado(self, nombre):
        """Manejar cuando un proceso termina"""
        self.label_estado.setText(f"{nombre}: Cerrado")
        if nombre in self.procesos:
            del self.procesos[nombre]
    
    def error_proceso(self, nombre, error):
        """Manejar errores de proceso"""
        errores = {
            QProcess.FailedToStart: "No se pudo iniciar",
            QProcess.Crashed: "El programa se cerró inesperadamente",
            QProcess.Timedout: "Tiempo de espera agotado"
        }
        mensaje = errores.get(error, "Error desconocido")
        self.label_estado.setText(f"{nombre}: {mensaje}")
    
    def dragEnterEvent(self, event):
        """Aceptar archivos arrastrados"""
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event):
        """Manejar archivos arrastrados al escritorio"""
        for url in event.mimeData().urls():
            archivo = url.toLocalFile()
            if os.path.isfile(archivo):
                # Preguntar si quiere agregar como acceso directo
                reply = QMessageBox.question(self, "Agregar acceso directo", 
                                            f"¿Deseas agregar {os.path.basename(archivo)} al escritorio?",
                                            QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    nombre = os.path.basename(archivo)
                    comando = f'xdg-open "{archivo}"' if os.name != 'nt' else f'start "" "{archivo}"'
                    self.agregar_aplicacion(nombre, comando)
    
    def resizeEvent(self, event):
        """Reorganizar iconos al redimensionar"""
        super().resizeEvent(event)
        self.reorganizar_iconos()
    
    def reorganizar_iconos(self):
        """Reorganizar iconos según ancho disponible"""
        ancho = self.width()
        # Calcular número de columnas
        if ancho >= 800:
            columnas = 6
        elif ancho >= 600:
            columnas = 4
        else:
            columnas = 2
        
        # Reorganizar
        for i, icono in enumerate(self.aplicaciones):
            fila = i // columnas
            columna = i % columnas
            self.layout_iconos.addWidget(icono, fila, columna, Qt.AlignTop | Qt.AlignLeft)

    def cuadrar(self):
        if self.parent():
            self.setGeometry(0, 0, self.parent().width(), self.parent().height())

    def CuadrarComponentesPrincipal(self):
        self.cuadrar()

    def showEvent(self, event):
        super().showEvent(event)
        print("ComponentesPrincipal entered")

    def hideEvent(self, event):
        super().hideEvent(event)
        print("ComponentesPrincipal exited")
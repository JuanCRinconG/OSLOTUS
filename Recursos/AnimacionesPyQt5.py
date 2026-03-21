from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve

class AnimacionesPyQt5:
    def __init__(self):
        pass

    def AnimacionTransparencia(self, WidgetParaAnimar=None, Duracion=None):
        EfectoTransparencia = QGraphicsOpacityEffect(WidgetParaAnimar)
        WidgetParaAnimar.setGraphicsEffect(EfectoTransparencia)
        EfectoTransparencia.setOpacity(0.0)
        WidgetParaAnimar.show()
        Animacion = QPropertyAnimation(EfectoTransparencia, b"opacity", self)
        Animacion.setDuration(Duracion)  # ms
        Animacion.setStartValue(0.0)
        Animacion.setEndValue(1.0)
        Animacion.setEasingCurve(QEasingCurve.InOutQuad)
        Animacion.start(QPropertyAnimation.DeleteWhenStopped)
        
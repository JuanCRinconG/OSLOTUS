"""Escala coordenadas de diseño (1920×1080) al tamaño real del contenedor."""

from PyQt5.QtWidgets import QWidget


class LayoutRelativo:
    ANCHO_DISENYO = 1920
    ALTO_DISENYO = 1080

    def __init__(self, padre: QWidget):
        self._padre = padre

    def escalar_x(self, x_disenyo: float) -> int:
        if self._padre.width() < 1:
            return 0
        return int(x_disenyo / self.ANCHO_DISENYO * self._padre.width())

    def escalar_y(self, y_disenyo: float) -> int:
        if self._padre.height() < 1:
            return 0
        return int(y_disenyo / self.ALTO_DISENYO * self._padre.height())

    def escalar_w(self, w_disenyo: float) -> int:
        return self.escalar_x(w_disenyo)

    def escalar_h(self, h_disenyo: float) -> int:
        return self.escalar_y(h_disenyo)

    def colocar(self, widget: QWidget, x: float, y: float, w: float, h: float) -> None:
        widget.setGeometry(
            self.escalar_x(x),
            self.escalar_y(y),
            self.escalar_w(w),
            self.escalar_h(h),
        )

    def colocar_centrado_h(self, widget: QWidget, y: float, w: float, h: float) -> None:
        ancho = self.escalar_w(w)
        x = (self._padre.width() - ancho) // 2
        widget.setGeometry(x, self.escalar_y(y), ancho, self.escalar_h(h))

    def colocar_centrado_v(self, widget: QWidget, x: float, w: float, h: float) -> None:
        alto = self.escalar_h(h)
        y = (self._padre.height() - alto) // 2
        widget.setGeometry(self.escalar_x(x), y, self.escalar_w(w), alto)

    def colocar_centrado(self, widget: QWidget, w: float, h: float) -> None:
        ancho = self.escalar_w(w)
        alto = self.escalar_h(h)
        x = (self._padre.width() - ancho) // 2
        y = (self._padre.height() - alto) // 2
        widget.setGeometry(x, y, ancho, alto)

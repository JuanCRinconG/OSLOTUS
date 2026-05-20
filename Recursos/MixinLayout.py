"""Mixin para que los componentes expongan self.layout_r y reescalen al redimensionar."""

from PyQt5.QtCore import QEvent

from .LayoutRelativo import LayoutRelativo


class MixinLayout:
    layout_r: LayoutRelativo
    _padre_layout: object

    def inicializar_layout(self, padre) -> None:
        self.layout_r = LayoutRelativo(padre)
        self._padre_layout = padre
        padre.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj is self._padre_layout and event.type() == QEvent.Resize:
            self.cuadrar()
        return False

    def cuadrar(self) -> None:
        raise NotImplementedError(
            f"{type(self).__name__} debe implementar cuadrar() usando self.layout_r"
        )

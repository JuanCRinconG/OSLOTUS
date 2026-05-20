"""Mixin para que los componentes expongan self.layout_r y el método cuadrar()."""

from .LayoutRelativo import LayoutRelativo


class MixinLayout:
    layout_r: LayoutRelativo

    def inicializar_layout(self, padre) -> None:
        self.layout_r = LayoutRelativo(padre)

    def cuadrar(self) -> None:
        raise NotImplementedError(
            f"{type(self).__name__} debe implementar cuadrar() usando self.layout_r"
        )

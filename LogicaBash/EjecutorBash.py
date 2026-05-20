"""Ejecución de scripts .sh con bash resuelto de forma cross-platform."""

from __future__ import annotations

import logging
import subprocess
from pathlib import Path

from LogicaBash.ResolvedorBash import resolver_bash

logger = logging.getLogger(__name__)


class EjecutorBash:
    def __init__(self):
        self._bash = resolver_bash()
        if self._bash is None:
            logger.warning("Bash no disponible en este sistema.")

    def _comando(self, ruta_script: str, args: list[str]) -> list[str] | None:
        if self._bash is None:
            return None
        ruta = str(Path(ruta_script).resolve())
        if self._bash == "wsl":
            return ["wsl", "bash", ruta, *args]
        return [self._bash, ruta, *args]

    def ejecutar(
        self, ruta_script: str, args: list[str] | None = None
    ) -> subprocess.CompletedProcess | None:
        args = args or []
        comando = self._comando(ruta_script, args)
        if comando is None:
            return None
        return subprocess.run(
            comando,
            capture_output=True,
            text=True,
        )

    def ejecutar_async(
        self, ruta_script: str, args: list[str] | None = None
    ) -> subprocess.Popen | None:
        args = args or []
        comando = self._comando(ruta_script, args)
        if comando is None:
            return None
        return subprocess.Popen(comando)

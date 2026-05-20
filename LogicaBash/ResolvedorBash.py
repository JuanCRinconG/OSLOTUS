"""Detecta el ejecutable bash disponible según el sistema operativo."""

from __future__ import annotations

import os
import platform
import shutil
from pathlib import Path


def resolver_bash() -> str | None:
    """
    Retorna la ruta al ejecutable bash disponible en el sistema actual.
    """
    sistema = platform.system()

    if sistema in ("Linux", "Darwin"):
        ruta = shutil.which("bash")
        return ruta if ruta else None

    if sistema == "Windows":
        candidatos_git = [
            Path(r"C:/Program Files/Git/bin/bash.exe"),
            Path(r"C:/Program Files (x86)/Git/bin/bash.exe"),
        ]
        local_app = os.environ.get("LOCALAPPDATA")
        if local_app:
            candidatos_git.append(
                Path(local_app) / "Programs" / "Git" / "bin" / "bash.exe"
            )
        for ruta in candidatos_git:
            if ruta.is_file():
                return str(ruta)

        if shutil.which("wsl"):
            return "wsl"

    return None


def bash_disponible() -> bool:
  return resolver_bash() is not None

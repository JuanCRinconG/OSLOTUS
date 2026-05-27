"""Gestor de archivos y preferencias por sesión de usuario."""

import os
import json

RUTA_SESIONES = os.path.join("datos", "sesiones")

class GestorSesionUsuario:

    def __init__(self, usuario_id: str):
        self.usuario_id = usuario_id
        self.ruta = os.path.join(RUTA_SESIONES, usuario_id)
        self._preferencias = {}
        self._crear_carpeta_si_no_existe()
        self._cargar_preferencias()

    # ── Carpeta ───────────────────────────────────────────────

    def _crear_carpeta_si_no_existe(self):
        os.makedirs(self.ruta, exist_ok=True)

    # ── Preferencias ──────────────────────────────────────────

    def _ruta_preferencias(self):
        return os.path.join(self.ruta, "preferencias.json")

    def _cargar_preferencias(self):
        ruta = self._ruta_preferencias()
        if os.path.exists(ruta):
            with open(ruta, "r", encoding="utf-8") as f:
                self._preferencias = json.load(f)
        else:
            self._preferencias = {
                "fondo": None,
                "apps_fijadas": []
            }
            self._guardar_preferencias()

    def _guardar_preferencias(self):
        with open(self._ruta_preferencias(), "w", encoding="utf-8") as f:
            json.dump(self._preferencias, f, indent=2, ensure_ascii=False)

    def obtener(self, clave: str, default=None):
        return self._preferencias.get(clave, default)

    def guardar(self, clave: str, valor):
        self._preferencias[clave] = valor
        self._guardar_preferencias()
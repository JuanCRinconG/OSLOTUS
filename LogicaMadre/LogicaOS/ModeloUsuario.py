"""Modelo de datos de un usuario del sistema (sin dependencias de PyQt)."""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from typing import Any


def _ahora_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _hash_pin(pin: str) -> str:
    return hashlib.sha256(pin.encode("utf-8")).hexdigest()


class ModeloUsuario:
    def __init__(
        self,
        id: str,
        nombre: str,
        avatar: str | None = None,
        pin: str | None = None,
        creado_en: str | None = None,
        ultimo_acceso: str | None = None,
    ):
        self.id = id
        self.nombre = nombre
        self.avatar = avatar
        self.pin = pin
        self.creado_en = creado_en or _ahora_iso()
        self.ultimo_acceso = ultimo_acceso

    def verificar_pin(self, pin_ingresado: str) -> bool:
        if self.pin is None:
            return True
        return _hash_pin(pin_ingresado) == self.pin

    def a_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "avatar": self.avatar,
            "pin": self.pin,
            "creado_en": self.creado_en,
            "ultimo_acceso": self.ultimo_acceso,
        }

    @staticmethod
    def desde_dict(d: dict[str, Any]) -> ModeloUsuario:
        return ModeloUsuario(
            id=d["id"],
            nombre=d["nombre"],
            avatar=d.get("avatar"),
            pin=d.get("pin"),
            creado_en=d.get("creado_en"),
            ultimo_acceso=d.get("ultimo_acceso"),
        )

    @staticmethod
    def pin_desde_texto(pin_texto: str | None) -> str | None:
        if pin_texto is None or pin_texto == "":
            return None
        return _hash_pin(pin_texto)

"""Persistencia de usuarios en datos/usuarios.json."""

from __future__ import annotations

import json
import uuid
from pathlib import Path

from LogicaMadre.LogicaOS.ModeloUsuario import ModeloUsuario, _ahora_iso

_RUTA_PROYECTO = Path(__file__).resolve().parents[2]


class GestorUsuarios:
    RUTA_DATOS = _RUTA_PROYECTO / "datos" / "usuarios.json"

    def __init__(self):
        self._usuarios: dict[str, ModeloUsuario] = {}
        self.RUTA_DATOS.parent.mkdir(parents=True, exist_ok=True)
        if not self.RUTA_DATOS.exists():
            self._escribir_vacio()
        self._cargar()

    def _escribir_vacio(self) -> None:
        self.RUTA_DATOS.write_text(
            json.dumps({"usuarios": []}, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def _cargar(self) -> None:
        self._usuarios.clear()
        try:
            datos = json.loads(self.RUTA_DATOS.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            datos = {"usuarios": []}
        for entrada in datos.get("usuarios", []):
            usuario = ModeloUsuario.desde_dict(entrada)
            self._usuarios[usuario.id] = usuario

    def _guardar(self) -> None:
        lista = [u.a_dict() for u in sorted(self._usuarios.values(), key=lambda u: u.nombre.lower())]
        self.RUTA_DATOS.write_text(
            json.dumps({"usuarios": lista}, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def obtener_todos(self) -> list[ModeloUsuario]:
        return sorted(self._usuarios.values(), key=lambda u: u.nombre.lower())

    def obtener_por_id(self, id: str) -> ModeloUsuario | None:
        return self._usuarios.get(id)

    def crear_usuario(
        self,
        nombre: str,
        avatar: str | None = None,
        pin: str | None = None,
    ) -> ModeloUsuario:
        pin_hash = ModeloUsuario.pin_desde_texto(pin)
        usuario = ModeloUsuario(
            id=str(uuid.uuid4()),
            nombre=nombre,
            avatar=avatar,
            pin=pin_hash,
        )
        self._usuarios[usuario.id] = usuario
        self._guardar()
        return usuario

    def eliminar_usuario(self, id: str) -> bool:
        if id not in self._usuarios:
            return False
        del self._usuarios[id]
        self._guardar()
        return True

    def actualizar_usuario(self, id: str, **campos) -> bool:
        usuario = self._usuarios.get(id)
        if usuario is None:
            return False
        if "nombre" in campos and campos["nombre"] is not None:
            usuario.nombre = campos["nombre"]
        if "avatar" in campos:
            usuario.avatar = campos["avatar"]
        if "pin" in campos:
            pin_val = campos["pin"]
            if pin_val is None or pin_val == "":
                usuario.pin = None
            elif len(pin_val) == 64 and all(c in "0123456789abcdef" for c in pin_val.lower()):
                usuario.pin = pin_val
            else:
                usuario.pin = ModeloUsuario.pin_desde_texto(pin_val)
        if "ultimo_acceso" in campos:
            usuario.ultimo_acceso = campos["ultimo_acceso"]
        self._guardar()
        return True

    def registrar_acceso(self, id: str) -> None:
        self.actualizar_usuario(id, ultimo_acceso=_ahora_iso())

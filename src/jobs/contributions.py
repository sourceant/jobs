from __future__ import annotations

from typing import Any


class Contributions:
    """The smallest registry a worker needs: things contributed under a type, in the order they came."""

    def __init__(self) -> None:
        self._items: dict[Any, list[Any]] = {}

    def contribute(self, type: Any, item: Any, source: str = "") -> None:
        self._items.setdefault(type, []).append(item)

    def contributions(self, type: Any) -> tuple[Any, ...]:
        return tuple(self._items.get(type, ()))

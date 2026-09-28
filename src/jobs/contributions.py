from __future__ import annotations

from typing import Any


class Contributions:
    """The smallest registry a worker needs: things contributed under a kind, in the order they came."""

    def __init__(self) -> None:
        self._items: dict[Any, list[Any]] = {}

    def contribute(self, kind: Any, item: Any, source: str = "") -> None:
        self._items.setdefault(kind, []).append(item)

    def contributions(self, kind: Any) -> tuple[Any, ...]:
        return tuple(self._items.get(kind, ()))

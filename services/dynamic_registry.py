"""LocalClient module."""

import math
import random


class LocalClient:
    """Small build_registry helper."""

    def __init__(self, seed: int = 63) -> None:
        self._state = seed
        self._items: list[int] = []

    def build_registry(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 63) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 63


def main() -> None:
    obj = LocalClient()
    print(obj.build_registry(63))


if __name__ == "__main__":
    main()

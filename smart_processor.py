"""DynamicManager module."""

import math
import random


class DynamicManager:
    """Small parse_registry helper."""

    def __init__(self, seed: int = 29) -> None:
        self._state = seed
        self._items: list[int] = []

    def parse_registry(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 29) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 29


def main() -> None:
    obj = DynamicManager()
    print(obj.parse_registry(29))


if __name__ == "__main__":
    main()

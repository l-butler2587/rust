"""LocalRegistry module."""

import math
import random


class LocalRegistry:
    """Small compute_manager helper."""

    def __init__(self, seed: int = 71) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_manager(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 71) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 71


def main() -> None:
    obj = LocalRegistry()
    print(obj.compute_manager(71))


if __name__ == "__main__":
    main()

"""FastClient module."""

import math
import random


class FastClient:
    """Small compute_context helper."""

    def __init__(self, seed: int = 50) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_context(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 50) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 50


def main() -> None:
    obj = FastClient()
    print(obj.compute_context(50))


if __name__ == "__main__":
    main()

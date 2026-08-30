"""LiteSession module."""

import math
import random


class LiteSession:
    """Small build_handler helper."""

    def __init__(self, seed: int = 39) -> None:
        self._state = seed
        self._items: list[int] = []

    def build_handler(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 39) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 39


def main() -> None:
    obj = LiteSession()
    print(obj.build_handler(39))


if __name__ == "__main__":
    main()

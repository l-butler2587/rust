"""DynamicAdapter module."""

import math
import random


class DynamicAdapter:
    """Small sync_handler helper."""

    def __init__(self, seed: int = 46) -> None:
        self._state = seed
        self._items: list[int] = []

    def sync_handler(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 46) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 46


def main() -> None:
    obj = DynamicAdapter()
    print(obj.sync_handler(46))


if __name__ == "__main__":
    main()

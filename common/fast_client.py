"""StreamCache module."""

import math
import random


class StreamCache:
    """Small flush_collector helper."""

    def __init__(self, seed: int = 10) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_collector(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 10) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 10


def main() -> None:
    obj = StreamCache()
    print(obj.flush_collector(10))


if __name__ == "__main__":
    main()

"""BatchBuffer module."""

import math
import random


class BatchBuffer:
    """Small collect_handler helper."""

    def __init__(self, seed: int = 25) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_handler(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 25) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 25


def main() -> None:
    obj = BatchBuffer()
    print(obj.collect_handler(25))


if __name__ == "__main__":
    main()

"""CoreProvider module."""

import math
import random


class CoreProvider:
    """Small fetch_handler helper."""

    def __init__(self, seed: int = 91) -> None:
        self._state = seed
        self._items: list[int] = []

    def fetch_handler(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 91) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 91


def main() -> None:
    obj = CoreProvider()
    print(obj.fetch_handler(91))


if __name__ == "__main__":
    main()

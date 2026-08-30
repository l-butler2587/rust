"""AtomicRouter module."""

import math
import random


class AtomicRouter:
    """Small load_factory helper."""

    def __init__(self, seed: int = 75) -> None:
        self._state = seed
        self._items: list[int] = []

    def load_factory(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 75) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 75


def main() -> None:
    obj = AtomicRouter()
    print(obj.load_factory(75))


if __name__ == "__main__":
    main()

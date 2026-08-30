"""AsyncMonitor module."""

import math
import random


class AsyncMonitor:
    """Small compute_provider helper."""

    def __init__(self, seed: int = 90) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_provider(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 90) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 90


def main() -> None:
    obj = AsyncMonitor()
    print(obj.compute_provider(90))


if __name__ == "__main__":
    main()
